#include <iostream>
#include <vector>

using namespace std;    // standard c++ library

int binarySearch(int arr[], int l, int r, int x) {  // recursive binary search approach
    if (r >= l) {
        int mid = l + (r - l) / 2;

        if (arr[mid] == x)  // if element is at the middle
            return mid;

        if (arr[mid] > x)   // if element is less than mid, search left half, set limits to l and mid - 1
            return binarySearch(arr, l, mid - 1, x);

        // element is greater than mid, search right half
        return binarySearch(arr, mid + 1, r, x);
    }

    // We reach here when element is not
    // present in array
    return -1;
}

int main() {
    cout << "Algorithms" << endl;

    //////////////////////////////////////////////////////////////////////////////////////////////
    // general info regarding algorithms


    // TOP-DOWN APPROACH
    //  identify major components of system, break them down into lower level components until desired complexity is achieved
    //  fine tune each component until desired


    // BOTTOM-UP APPROACH
    //  start with designing basic components and go up to higher components till final stage is reached


    // BIG-O NOTATION
    // analysis used to measure efficiency of an algorithm with regard to time and space complexity
    // based on how many steps a machine must go through with N inputs to reach desired goal of speed
    // O(n), O(logn), O(1), O(nlogn), etc...
    // time complexity of an algorithm is a measure of min time required for n inputs
    // each algorithm has a best and worst case time complexity, depending on how the data is handled in specific cases
    // also consists of average/amortized time analysis, in most case scenarios


    //////////////////////////////////////////////////////////////////////////////////////////
    // SEARCHING algorithms

    // LINEAR/SEQUENTIAL SEARCH
    // search entire list in sequential order
    // O(n)

    int numbers[10] = {4, 6, 2, 8, 10, 451, 43, 1, 53, 23};

    cout << "\nLINEAR SEARCH" << endl;
    int wantToFind = 451;

    for (int i = 0 ; i < sizeof(numbers) / sizeof(numbers[0]); i++) {   // look through data structure
        if (wantToFind == numbers[i]) {     // if item matches what is needed to find
            cout << wantToFind << " found at index " << i << endl;
            break;
        }   // if item is not found, iterates through data until found or not found, hence O(n)
    }

    //////////////////////////////////////////////////////////////////////////////////////////

    // BINARY SEARCH
    // requires list to be in sorted order
    // iterative approach, recursive implementation can be seen at top of file

    cout << "\nBINARY SEARCH" << endl;

    vector<int> numbers2 = {1, 3, 7, 23, 76, 264, 735, 2647, 27457, 76535};
    wantToFind = 23;

    int l = 0, r = numbers2.size() - 1; // left and right correspond to beginning and end of vector
    int mid;

    while (r - l > 1) { // while the difference between indexes is greater than 1, i.e 3 or more indexes to choose from
        mid = (l + r) / 2;  // set mid
        if (numbers2[mid] < wantToFind) {   // if number is greater than mid-value
            l = mid + 1;    // number must be on the right half of vector, increment to search right half
        } else {
            r = mid;
        }
    }

    if (numbers2[l] == wantToFind) {
        cout << wantToFind << " found at index " << r << endl;
    } else if (numbers2[r] == wantToFind){
        cout << wantToFind << " found at index " << r << endl;
    } else {
        cout << wantToFind << " not found!" << endl;
    }

    //////////////////////////////////////////////////////////////////////////////////////////



    return 0;
}
