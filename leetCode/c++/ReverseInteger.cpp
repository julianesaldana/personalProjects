#include <iostream>
#include <math.h>

using namespace std;

int reverse(int x) {
    int temp = x;
    int counter = 0;

    // counting number of digits
    while (temp > 0) {
        temp /= 10;
        counter++;
    }

    return temp;
}

int main() {
    int num = 123;
    reverse(num);
    return 0;
}