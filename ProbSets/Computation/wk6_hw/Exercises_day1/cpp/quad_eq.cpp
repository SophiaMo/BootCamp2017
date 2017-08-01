#include <iostream>
#include <cmath>

int main()
{
    using namespace std;
    float a, b, c, root1, root2;
    cout << "a is: ";
    cin >> a;
    cout << "b is: ";
    cin >> b;
    cout << "c is: ";
    cin >> c;
    root1 = (-b + sqrt(pow(b, 2) - 4*a*c))/(2*a);
    root2 = (-b - sqrt(pow(b, 2) - 4*a*c))/(2*a);
    cout << "Root 1 is "<< root1;
    cout << "Root 2 is "<< root2;
    return 0;
}

