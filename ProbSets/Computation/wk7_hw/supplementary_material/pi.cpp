#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <mpi.h>

using namespace std;

int main(int argc, char *argv[]) {
int rank, p;
int sum;
int iter;
MPI_Init(&argc, &argv);
MPI_Comm_rank(MPI_COMM_WORLD, &rank);
MPI_Comm_size(MPI_COMM_WORLD, &p);

int npoints = 10000000;
double pi;
double z;
double x, y;
int i;
int count = 0;
double points = npoints/p;

if (rank != 0)
{
for (i = 0; i<points; ++i) {
    srand48(time(NULL));
    x = (double) random()/RAND_MAX;
    y = (double) random()/RAND_MAX;
    z = sqrt((x*x)+(y*y));
    if (z<=1) {
       ++count;
    } 
}
}

MPI_Reduce(&count, &sum, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    if (rank==0){
      pi = ((double)sum/(double)npoints)*4.0;
      printf("pi = %d\n", pi);
    }

    MPI_Finalize();
    return 0;
}   


