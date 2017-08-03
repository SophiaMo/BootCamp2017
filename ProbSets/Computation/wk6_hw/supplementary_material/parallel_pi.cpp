#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>
#include <iostream>
#include <random>
using namespace std;
unsigned seed;
int main() {
    double x,y;
    int i;
    int count=0;
    double z;
    double pi;
    double time_parallel = -omp_get_wtime();

    //main loop
    #pragma omp parallel default(none), private(x, y, z, seed), shared(count)
    {
    seed = 25234 + 17 * omp_get_thread_num();
    
    #pragma omp for reduction(+:count) 
    for (i=0; i<10000000; ++i)
        {
        //get random points
        x = (double) rand_r(&seed)/(double)RAND_MAX;
        y = (double) rand_r(&seed)/(double)RAND_MAX;
        z = sqrt((x*x)+(y*y));
        //check to see if point is in unit circle
        count += (z<=1);  
        }
        }
    pi = ((double)count/(double)10000000)*4.0;          //p = 4(m/n)  
    time_parallel += omp_get_wtime();
    printf("Pi: %f\n", pi);
    printf("Time: %f\n", time_parallel);
    }

