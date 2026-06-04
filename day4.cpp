#include <iostream>
using namespace std;

int findFactorial(int n) {
    int fact = 1;
    for (int i = 1; i <= n; i++) {
        fact *= i;
    }
    return fact;
}

int main() {
    // Calling the function with the input 5
    int result = findFactorial(5);
    cout << "Factorial of 5 is: " << result << endl;
    return 0;
}