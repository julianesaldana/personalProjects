#include <iostream>
#include <vector>

using namespace std;    // standard c++ library

int linearSearch(int numbers[], int wantToFind) {
    for (int i = 0 ; i < sizeof(numbers) / sizeof(numbers[0]); i++) {   // look through data structure
        if (wantToFind == numbers[i]) {     // if item matches what is needed to find
            return i;
        }
    }
    return -1;  // if element not found in array, return index = -1
}

int binarySearch(vector<int> numbers, int wantToFind) { // iterative approach to binary search
    int l = 0, r = numbers.size() - 1; // left and right correspond to beginning and end of vector
    int mid;

    while (r - l > 1) { // while the difference between indexes is greater than 1, i.e 3 or more indexes to choose from
        mid = (l + r) / 2;  // set mid to middle of vector
        if (numbers[mid] < wantToFind) {   // if number is greater than mid-value
            l = mid + 1;    // number must be on the right half of vector, set lower limit to mid + 1
        } else {
            r = mid;    // set upper limit to mid, number must be in the left half
        }
    }

    if (numbers[l] == wantToFind) { // returns whichever limit corresponds to index of value found
        return l;
    } else if (numbers[r] == wantToFind){
        return r;
    } else {
        return -1;  // return -1 if element not found in vector
    }
}

int binarySearchRec(vector<int> numbers, int l, int r, int wantToFind) {  // recursive binary search approach
    if (r >= l) {
        int mid = l + (r - l) / 2;

        if (numbers[mid] == wantToFind)  // if element is at the middle
            return mid;

        if (numbers[mid] > wantToFind)   // if element is less than mid, search left half, set limits to l and mid - 1
            return binarySearchRec(numbers, l, mid - 1, wantToFind);

        // element is greater than mid, search right half
        return binarySearchRec(numbers, mid + 1, r, wantToFind);
    }

    // if element not in vector, return index -1
    return -1;
}

int main() {
    //////////////////////////////////////////////////////////////////////////////////////////////
    cout << "Algorithms" << endl;
    // here contains general info regarding algorithms
    // all algos will be implemented in separate classes above, main will contain data input and output


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
    cout << "\nSearching algos" << endl;

    // LINEAR/SEQUENTIAL SEARCH
    // search entire list in sequential order
    // O(n)

    cout << "\nLINEAR SEARCH" << endl;
    int numbers[10] = {4, 6, 2, 8, 10, 451, 43, 1, 53, 23};
    int wantToFind = 451;
    cout << wantToFind << " found at index " << linearSearch(numbers, wantToFind) << endl;
    
    
    //////////////////////////////////////////////////////////////////////////////////////////
    // BINARY SEARCH
    // requires list to be in sorted order
    // iterative and recursive approach
    // O(logn)

    cout << "\nBINARY SEARCH" << endl;
    vector<int> numbers2 = {1, 3, 7, 23, 76, 264, 735, 2647, 27457, 76535};
    wantToFind = 23;
    
    cout << "iterative binary search" << endl;
    cout << wantToFind << " found at index " << binarySearch(numbers2, wantToFind) << endl;
    
    cout << "\nrecursive binary search" << endl;
    cout << wantToFind << " found at index " << binarySearchRec(numbers2, 0, numbers2.size() - 1, wantToFind) << endl;
   

    //////////////////////////////////////////////////////////////////////////////////////////
    // SORTING ALGORITHMS
    cout << "\nSorting" << endl;

    
    return 0;
}
