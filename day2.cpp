#include <iostream>
using namespace std;

int main() {
    char ch;
    cout << "Enter a character: "<<endl;
    cin >> ch;

    if (ch >= 'a' && ch <= 'z') {
        cout << "LowerCase"<<endl;
    }
    else if (ch >= 'A' && ch <= 'Z') {
        cout << "UpperCase"<<endl;
    }

    else{}
    cout << "Invalid alphabet or character" << endl;
return 0;
}
