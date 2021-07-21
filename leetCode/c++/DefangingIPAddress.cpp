#include <iostream>

using namespace std;

string defangIPaddr(string address) {
    string newString;
    for (int i = 0; i < address.size(); i++) {
        if (address[i] == '.') {
            newString += "[.]";
        } else {
            newString += address[i];
        }
    }

    return newString;
}

int main() {
    cout << defangIPaddr("255.100.50.0") << endl;
    return 0;
}
