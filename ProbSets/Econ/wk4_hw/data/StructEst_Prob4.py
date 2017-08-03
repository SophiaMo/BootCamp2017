'''
------------------------------------------------------------------------
This script computes the solution to the Brock and Mirman GMM exercise
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
ct, kt, wt, rt = data['ct'], data['kt'], data['wt'], data['rt']

# set the directory for saving images
cur_path = os.path.split(os.path.abspath(__file__))[0]
output_fldr = 'images'
output_dir = os.path.join(cur_path, output_fldr)
if not os.access(output_dir, os.F_OK):
    os.makedirs(output_dir)

'''
------------------------------------------------------------------------
4.(a) Estimate α, β, ρ, and μ by GMM using the unconditional moment
conditions that E[εt] = 0 and E[βrt+1ct/ct+1 − 1] = 0. Use the identity
matrix I(4) as your estimator of the optimal weighting matrix. Use the
following four moment conditions to estimate the four parameters.
------------------------------------------------------------------------
'''


def data_moments(df, alpha, beta, rho, mu):
    '''
    --------------------------------------------------------------------
    This function computes the vector of data moments for GMM.
    --------------------------------------------------------------------
    INPUTS:
    df     = DataFrame, (ct, kt, wt, rt)
    alpha  = scalar in (0, 1), capital share of income
    beta   = scalar in (0, 1), discount factor
    rho    = scalar in (-1, 1), persistence of productivity process
    mu     = scalar, mean of productivity process

    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None

    OBJECTS CREATED WITHIN FUNCTION:
    moms_data = (42,) Series, percent of population in each of 42 income
                bin from data
    moms_mod  = (42,) vector, percent of population in each of 42 income
                bins implied by the model
    err_vec   = (42,) vector, errors between model and data moments

    FILES CREATED BY THIS FUNCTION: None

    RETURNS: err_vec
    --------------------------------------------------------------------
    '''
    ct, kt, wt, rt = df['ct'], df['kt'], df['wt'], df['rt']
    zt = np.log(rt) - np.log(alpha) - (alpha - 1) * np.log(kt)
    eps_t = zt - rho * zt.shift(1) - (1 - rho) * mu
    eps_t = eps_t[1:]
    mom1 = eps_t.mean()
    mom2 = (eps_t * zt[1:]).mean()
    mom3 = (beta * rt[1:] * (ct[:-1] / ct[1:]) - 1).mean()
    mom4 = ((beta * rt[1:] * (ct[:-1] / ct[1:]) - 1) * wt[:-1]).mean()
    data_moments = np.array([mom1, mom2, mom3, mom4])

    return data_moments


def err_vec(df, alpha, beta, rho, mu, simple):
    '''
    --------------------------------------------------------------------
    This function computes the vector of moment errors (in percent
    deviation from the data moment vector) for GMM.
    --------------------------------------------------------------------
    INPUTS:
    df     = DataFrame, (ct, kt, wt, rt)
    alpha  = scalar in (0, 1), capital share of income
    beta   = scalar in (0, 1), discount factor
    rho    = scalar in (-1, 1), persistence of productivity process
    mu     = scalar, mean of productivity process
    simple = boolean, =True if errors are simple difference, =False if
             errors are percent deviation from data moments

    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION:
        data_moments()

    OBJECTS CREATED WITHIN FUNCTION:
    moms_data = (42,) Series, percent of population in each of 42 income
                bin from data
    moms_mod  = (42,) vector, percent of population in each of 42 income
                bins implied by the model
    err_vec   = (42,) vector, errors between model and data moments

    FILES CREATED BY THIS FUNCTION: None

    RETURNS: err_vec
    --------------------------------------------------------------------
    '''
    moms_data = data_moments(df, alpha, beta, rho, mu)
    moms_model = np.zeros(4)
    if simple:
        err_vec = moms_model - moms_data
    else:
        err_vec = 100 * ((moms_model - moms_data) / moms_data)

    return err_vec


def crit(params, *args):
    '''
    --------------------------------------------------------------------
    This function computes the weighted sum of squared deviations
    criterion function for the GMM estimator fitting 42 income moments
    --------------------------------------------------------------------
    INPUTS:
    params = (4,) vector, ([alpha, beta, rho, mu])
    args   = length 2 tuple, (DataFrame, W_hat)

    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION:
        err_vec_LN()

    OBJECTS CREATED WITHIN FUNCTION:
    alpha    = scalar in (0, 1), capital share of income
    beta     = scalar in (0, 1), discount factor
    rho      = scalar in (-1, 1), persistence parameter in log
               productivity process
    mu       = scalar, mean in log productivity process
    data     = DataFrame, (ct, kt, wt, rt)
    W        = (4, 4) matrix, weighting matrix in criterion function
    errs     = (4,) vector, errors between data and model moments
    crit_val = scalar > 0, value of the criterion function

    FILES CREATED BY THIS FUNCTION: None

    RETURNS: crit_val
    --------------------------------------------------------------------
    '''
    alpha, beta, rho, mu = params
    data, W = args
    errs = err_vec(data, alpha, beta, rho, mu, simple=True)
    crit_val = np.dot(np.dot(errs.T, W), errs)

    return crit_val


# Estimate alpha, beta, rho, and mu of Brock and Mirman model using GMM
alpha_init = 0.3
beta_init = 0.9
rho_init = 0.7
mu_init = 9.0
params_init = np.array([alpha_init, beta_init, rho_init, mu_init])
W_hat = np.eye(4)
gmm_args = (data, W_hat)
results = opt.minimize(crit, params_init, args=(gmm_args),
                       method='Nelder-Mead')
alpha_gmm, beta_gmm, rho_gmm, mu_gmm = results.x
print('alpha=', alpha_gmm, ', beta_gmm=', beta_gmm, ', rho=', rho_gmm,
      ', mu=', mu_gmm)
print('GMM criterion value: ', results.fun)
print(results)
