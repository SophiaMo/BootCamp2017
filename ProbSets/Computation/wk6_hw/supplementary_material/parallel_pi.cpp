#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>
#include <iostream>
using namespace std;

int main() {
    double x,y;
    int i;
    int count=0;
    double z;
    double pi;
    double time = -omp_get_wtime();

    //main loop
    #pragma omp parallel private(x, y, z)
    {
    #pragma omp parallel for reduction(+:count)
    for (i=0; i<10000000; ++i)
        {
        //get random points
        x = (double)random()/RAND_MAX;
        y = (double)random()/RAND_MAX;
        z = sqrt((x*x)+(y*y));
        //check to see if point is in unit circle
        count += (z<=1);  
        time += omp_get_wtime();
        pi = ((double)count/(double)10000000)*4.0;          //p = 4(m/n)
        }  
    }
    cout << "pi " << pi;
    cout << "it  took " << time << " seconds" << endl;
    return 0;
    }

