#include <iostream>
using namespace std;

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;
    
    // If remainder is 0 when divided by 2
    if (num % 2 == 0) {
        cout << num << " is Even." << endl;
    } else {
        cout << num << " is Odd." << endl;
    }
    
    return 0;
}