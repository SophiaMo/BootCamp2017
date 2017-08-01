#include <iostream>
#include <random>
#include <stdlib.h>  
using namespace std;
 
int main() {
    const double N[ ] = {1e2, 1e3, 1e4};
    for (int i = 0; i < (sizeof(N)/sizeof(N[0])); i++) {
        int c = 0;
        for (int j =0; j < N[i]; j++) {
            double x = static_cast<double>(rand())/static_cast<double>(RAND_MAX);
            double y = static_cast<double>(rand())/static_cast<double>(RAND_MAX);
            if (x * x + y * y <= 1) c ++;
            }
        cout << "Pi estimated using" << N[i] << "is " << 4.0 *  (double)c/N[i] << endl;
    }
    return 0;
 }
