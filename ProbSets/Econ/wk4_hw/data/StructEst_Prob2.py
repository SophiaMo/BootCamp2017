'''
------------------------------------------------------------------------
This script computes the solution to the Brock and Mirman MLE exercise
in the OSM Lab Boot Camp structural estimation problem set
------------------------------------------------------------------------
'''
# import pacakges
import numpy as np
import pandas as pd
import scipy.stats as sts
import scipy.optimize as opt
import os

# import data
data = pd.read_csv('MacroSeries.txt', header=None,
                   names=['ct', 'kt', 'wt', 'rt'])

# set the directory for saving images
cur_path = os.path.split(os.path.abspath(__file__))[0]
output_fldr = 'images'
output_dir = os.path.join(cur_path, output_fldr)
if not os.access(output_dir, os.F_OK):
    os.makedirs(output_dir)

'''
------------------------------------------------------------------------
2.(a) Use the data (wt, kt) and equations (3) and (5) to estimate the
four parameters (α, ρ, μ, σ) by maximum likelihood. Given a guess for
the parameters (α,ρ,μ,σ), you can use the two variables from the data
(wt,kt) and (3) to back out a series for zt. You can then use equation
(5) to compute the probability of each zt ∼ N ρzt−1 + (1 − ρ)μ, σ2. The
maximum likelihood estimate (αˆ,ρˆ,μˆ,σˆ) maximizes the likelihood
function of that normal distribution of zt’s. Report your estimates and
the inverse Hessian variance-covariance matrix of your estimates.
------------------------------------------------------------------------
'''


def log_lik_BrMir_w(df, alpha, rho, mu, sigma):
    '''
    --------------------------------------------------------------------
    Compute the log likelihood function given time series for w_t and
    k_t using firm's first order condition for labor demand and the law
    of motion for productivity shocks given parameters alpha, rho, mu,
    and sigma.
    --------------------------------------------------------------------
    INPUTS:
    df    = DataFrame, (k_t, w_t)
    alpha = scalar > 0, capital share of income
    rho   = scalar in (0, 1), persistence parameter in productivity
            process
    mu    = scalar, mean in productivity process
    sigma = scalar > 0, standard deviation in productivity process

    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None

    OBJECTS CREATED WITHIN FUNCTION:
    kt          = (N,) Series, time series of capital stock
    wt          = (N,) Series, time series of wage
    eps_t       = (N-1,) Series, time series of shocks to productivity
                  process
    pdf_vals    = (N-1,) vector, normal PDF values given data and
                  parameters
    ln_pdf_vals = (N-1,) vector, natural logarithm of normal PDF values
                  for data and parameters
    log_lik_val = scalar, value of the log likelihood function

    FILES CREATED BY THIS FUNCTION: None

    RETURNS: log_lik_val
    --------------------------------------------------------------------
    '''
    kt, wt = df['kt'], df['wt']
    zt = np.log(wt) - np.log(1 - alpha) - alpha * np.log(kt)
    eps_t = zt - rho * zt.shift(1) - (1 - rho) * mu
    eps_t = eps_t[1:]
    pdf_vals = sts.norm.pdf(eps_t, loc=0, scale=sigma)
    ln_pdf_vals = np.log(pdf_vals)
    log_lik_val = ln_pdf_vals.sum()

    return log_lik_val


def crit_BrMir_w(params, *args):
    '''
    --------------------------------------------------------------------
    This function computes the negative of the log likelihood function
    given parameters and data. This is the minimization problem version
    of the maximum likelihood optimization problem
    --------------------------------------------------------------------
    INPUTS:
    params = (4,) vector, ([alpha, rho, mu, sigma])
    args   = DataFrame, (k_t, w_t)

    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION:
        log_lik_BrMir_w()

    OBJECTS CREATED WITHIN FUNCTION:
    alpha           = scalar > 0, capital share of income
    rho             = scalar in (0, 1), persistence parameter in
                      productivity process
    mu              = scalar, mean in productivity process
    sigma           = scalar > 0, standard deviation in productivity
                      process
    log_lik_val     = scalar, value of the log likelihood function
    neg_log_lik_val = scalar, negative of log_lik_val

    FILES CREATED BY THIS FUNCTION: None

    RETURNS: neg_log_lik_val
    --------------------------------------------------------------------
    '''
    alpha, rho, mu, sigma = params
    df = args[0]
    log_lik_val = log_lik_BrMir_w(df, alpha, rho, mu, sigma)
    neg_log_lik_val = -log_lik_val

    return neg_log_lik_val


# initial guesses
alpha_BR1_init = 0.35
zt_BR1_init = (np.log(data['wt']) - np.log(1 - alpha_BR1_init) -
               alpha_BR1_init * np.log(data['kt']))
rho_BR1_init = 0.8
mu_BR1_init = zt_BR1_init.mean()
sigma_BR1_init = np.std(zt_BR1_init)
params_BR1_init = np.array([alpha_BR1_init, rho_BR1_init, mu_BR1_init,
                            sigma_BR1_init])
mle_BR1_args = data[['kt', 'wt']]

# optimization
BR1_results = \
    opt.minimize(crit_BrMir_w, params_BR1_init, args=(mle_BR1_args),
                 method='L-BFGS-B',
                 bounds=((1e-10, 1.0 - 1e-10),
                         (-1.0 + 1e-10, 1.0 - 1e-10),
                         (None, None), (1e-10, None)))
# estimated parameters
alpha_BR1_mle, rho_BR1_mle, mu_BR1_mle, sigma_BR1_mle = BR1_results.x
print('PROBLEM 2A SOLUTIONS')
print('alpha: ', alpha_BR1_mle, 'rho: ', rho_BR1_mle,
      'mu: ', mu_BR1_mle, 'sigma', sigma_BR1_mle)
print('VCV inv Hess: ', BR1_results.hess_inv.todense())
print(BR1_results)


'''
------------------------------------------------------------------------
2.(b) Now we will estimate the parameters another way. Use the data
(rt,kt) and equations (4) and (5) to estimate the four parameters
(α,ρ,μ,σ) by maximum likelihood. Given a guess for the parameters
(α, ρ, μ, σ), you can use the two variables from the data (rt,kt) and
(4) to back out a series for zt. You can then use equation (5) to
compute the probability of each zt ∼ N ρzt−1 + (1 − ρ)μ, σ2. The maximum
likelihood estimate (αˆ,ρˆ,μˆ,σˆ) maximizes the likelihood function of
that normal distribution of zt’s. Report your estimates and the inverse
Hessian variance-covariance matrix of your estimates.
------------------------------------------------------------------------
'''

def log_lik_BrMir_r(df, alpha, rho, mu, sigma):
    '''
    --------------------------------------------------------------------
    Compute the log likelihood function given time series for r_t and
    k_t using firm's first order condition for capital and the law
    of motion for productivity shocks given parameters alpha, rho, mu,
    and sigma.
    --------------------------------------------------------------------
    INPUTS:
    df    = DataFrame, (k_t, r_t)
    alpha = scalar > 0, capital share of income
    rho   = scalar in (0, 1), persistence parameter in productivity
            process
    mu    = scalar, mean in productivity process
    sigma = scalar > 0, standard deviation in productivity process

    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None

    OBJECTS CREATED WITHIN FUNCTION:
    kt          = (N,) Series, time series of capital stock
    rt          = (N,) Series, time series of interest rate
    eps_t       = (N-1,) Series, time series of shocks to productivity
                  process
    pdf_vals    = (N-1,) vector, normal PDF values given data and
                  parameters
    ln_pdf_vals = (N-1,) vector, natural logarithm of normal PDF values
                  for data and parameters
    log_lik_val = scalar, value of the log likelihood function

    FILES CREATED BY THIS FUNCTION: None

    RETURNS: log_lik_val
    --------------------------------------------------------------------
    '''
    kt, rt = df['kt'], df['rt']
    zt = np.log(rt) - np.log(alpha) - (alpha - 1) * np.log(kt)
    eps_t = zt - rho * zt.shift(1) - (1 - rho) * mu
    eps_t = eps_t[1:]
    pdf_vals = sts.norm.pdf(eps_t, loc=0, scale=sigma)
    ln_pdf_vals = np.log(pdf_vals)
    log_lik_val = ln_pdf_vals.sum()

    return log_lik_val


def crit_BrMir_r(params, *args):
    '''
    --------------------------------------------------------------------
    This function computes the negative of the log likelihood function
    given parameters and data. This is the minimization problem version
    of the maximum likelihood optimization problem
    --------------------------------------------------------------------
    INPUTS:
    params = (4,) vector, ([alpha, rho, mu, sigma])
    args   = DataFrame, (k_t, r_t)

    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION:
        log_lik_BrMir_r()

    OBJECTS CREATED WITHIN FUNCTION:
    alpha           = scalar > 0, capital share of income
    rho             = scalar in (0, 1), persistence parameter in
                      productivity process
    mu              = scalar, mean in productivity process
    sigma           = scalar > 0, standard deviation in productivity
                      process
    log_lik_val     = scalar, value of the log likelihood function
    neg_log_lik_val = scalar, negative of log_lik_val

    FILES CREATED BY THIS FUNCTION: None

    RETURNS: neg_log_lik_val
    --------------------------------------------------------------------
    '''
    alpha, rho, mu, sigma = params
    df = args[0]
    log_lik_val = log_lik_BrMir_r(df, alpha, rho, mu, sigma)
    neg_log_lik_val = -log_lik_val

    return neg_log_lik_val


# initial guesses
alpha_BR2_init = 0.35
zt_BR2_init = (np.log(data['rt']) - np.log(alpha_BR2_init) -
               (alpha_BR2_init - 1) * np.log(data['kt']))
rho_BR2_init = 0.7
mu_BR2_init = zt_BR2_init.mean()
sigma_BR2_init = np.std(zt_BR2_init)
params_BR2_init = np.array([alpha_BR2_init, rho_BR2_init, mu_BR2_init,
                            sigma_BR2_init])
mle_BR2_args = data[['kt', 'rt']]

# optimization
BR2_results = \
    opt.minimize(crit_BrMir_r, params_BR2_init, args=(mle_BR2_args),
                 method='L-BFGS-B',
                 bounds=((1e-10, 1.0 - 1e-10),
                         (-1.0 + 1e-10, 1.0 - 1e-10),
                         (None, None), (1e-10, None)))
# estimated parameters
alpha_BR2_mle, rho_BR2_mle, mu_BR2_mle, sigma_BR2_mle = BR2_results.x
print('PROBLEM 2B SOLUTIONS')
print('alpha: ', alpha_BR2_mle, 'rho: ', rho_BR2_mle,
      'mu: ', mu_BR2_mle, 'sigma', sigma_BR2_mle)
print('VCV inv Hess: ', BR2_results.hess_inv.todense())
print(BR2_results)


'''
------------------------------------------------------------------------
2.(c) According to your estimates from part (a), if investment/savings
in the current period is kt = 7,500,000 and the productivity shock in
the previous period was z_{t−1} = 10, what is the probability that the
interest rate this period will be greater than rt = 1. That is, solve
for P r(rt > 1|θ, kt, zt−1). [HINT: Use equation (4) to solve for the
zt = z* such that rt = 1. Then use (5) to solve for the probability that
zt > z*.]
------------------------------------------------------------------------
'''
kt_fixed = 7500000.
ztm1_fixed = 10.
z_star = -np.log(alpha_BR1_mle) - (alpha_BR1_mle - 1) * np.log(kt_fixed)
eps_star = (z_star - rho_BR1_mle * ztm1_fixed -
            (1 - rho_BR1_mle) * mu_BR1_mle)
Pr_r_gt_1 = 1 - sts.norm.cdf(eps_star, loc=0, scale=sigma_BR1_mle)
print('PROBLEM 2C SOLUTIONS')
print('Pr(rt > 1 | theta-hat, kt = 7500000, z_lag = 10) = ', Pr_r_gt_1)
