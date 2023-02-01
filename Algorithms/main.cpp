#include <iostream>
#include <vector>

using namespace std;    // standard c++ library

// searching algorithms

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



// sorting algorithms

vector<int> bubbleSort(vector<int> numbers){
    for (int i = 0; i < numbers.size() - 1; i++) {  // iterate through list
        for (int j = 0; j < numbers.size() - i - 1; j++) {  // iterate through list again for each index, n*n, n^2 running time
            if (numbers[j] > numbers[j + 1]) {  // if value left is greater than value to the right
                swap(numbers[j], numbers[j + 1]);   // swap STL built-in function to swap value of two variables
            }
        }
    }
    return numbers;
}

vector<int> selectionSort(vector<int> numbers) {
    for (int i = 0; i < numbers.size() - 1; i++) {  // using this loop to loop through each item, represents the ordered portion
        int min = i;    // starting at first index
        for (int j = i + 1; j < numbers.size(); j++) {  // checking every other element besides current, represents unordered portion
            if (numbers[j] < numbers[min]) {    // setting min if element is smaller than current
                min = j;
            }
        }
        if (numbers[i] > numbers[min]) {    // after find min, if it is smaller than current element, swap
            swap(numbers[i], numbers[min]);
        }   // after this, the vector will have two portions, sorted left side, unsorted on the right side
    }
    return numbers;
}

void merge(vector<int> leftArray, vector<int> rightArray, vector<int> numbers) {
    int leftSize = numbers.size() / 2;  // max size of left sub array is half
    int rightSize = numbers.size() - leftSize;  // right side is left over amount on the right
    int index = 0;  // for original array, represents index
    int l = 0, r = 0;   // separate indices for sub-arrays, as a subarray may contain larger amount of smaller elements than the other subarray, thus need to keep track

    // checking conditions for merging
    while (l < leftSize && r < rightSize) {     // while the indexes are smaller than the subarray length, i.e, checking to see if each subarray still contains elements needed to be added
        if (leftArray[l] < rightArray[r]) {     // if left array element is smaller, add it first
            numbers[index] = leftArray[l];
            l++;
        } else {
            numbers[index] = rightArray[r];     // same for right
            r++;                                // increment indexes for each subarray only if it gets added, keeps track of subarray elements that need to be added
        }
        index++;
    }

    while (l < leftSize) {      // add leftover elements from left subarray
        numbers[index] = leftArray[l];
        index++;
        l++;
    }

    while (r < rightSize) {
        numbers[index] = rightArray[r];     // add leftover elements from right subarray
        index++;
        r++;
    }
}

void mergeSort(vector<int> numbers) {
    int length = numbers.size();    // based on splitting array into 2 sub-arrays each time
    if (length <= 1) {  // if subarray length is less than 2, that means no more splitting, finished with subarray
        return;
    }

    // if not done splitting, calculated middle of subarray
    int middle = length / 2;

    // initialize two sub-arrays, one for left, one for right
    vector<int> leftArray;
    vector<int> rightArray;

    int l = 0;  // left array
    int r = 0;  // right array

    // split each subarray down the middle and separate into left and right
    for (int i = 0; i < middle; i++) {
        leftArray[l] = numbers[i];
        l++;
    }
    for (int i = middle; i < length; i++) {
        rightArray[r] = numbers[i];
        r++;
    }

    // after splitting, keep splitting down left and right
    mergeSort(leftArray);
    mergeSort(rightArray);
    merge(leftArray, rightArray, numbers);  // finally merge all the sub-arrays together using helper method
}


int main() {
    //////////////////////////////////////////////////////////////////////////////////////////////
    // ALGORITHMS
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


    cout << "//////////////////////////////////////////////////////////////////////////////////////////" << endl;
    // SEARCHING algorithms
    cout << "Searching algos" << endl;


    // LINEAR/SEQUENTIAL SEARCH
    // search entire list in sequential order
    // O(n)

    cout << "\nLINEAR SEARCH" << endl;
    int numbers[10] = {4, 6, 2, 8, 10, 451, 43, 1, 53, 23};
    int wantToFind = 451;
    cout << wantToFind << " found at index " << linearSearch(numbers, wantToFind) << endl;

    
    // BINARY SEARCH
    // requires list to be in sorted order
    // compares values of list by > or < desired value, similar to binary tree
    // iterative and recursive approach
    // O(logn)

    cout << "\nBINARY SEARCH" << endl;
    vector<int> numbers2 = {1, 3, 7, 23, 76, 264, 735, 2647, 27457, 76535};
    wantToFind = 23;
    
    cout << "iterative binary search" << endl;
    cout << wantToFind << " found at index " << binarySearch(numbers2, wantToFind) << endl;
    
    cout << "recursive binary search" << endl;
    cout << wantToFind << " found at index " << binarySearchRec(numbers2, 0, numbers2.size() - 1, wantToFind) << endl;
   

    cout << "\n//////////////////////////////////////////////////////////////////////////////////////////" << endl;
    cout << "Sorting algos\n" << endl;
    // SORTING ALGORITHMS
    // internal sorting preferred if data to be sorted can be adjusted at a time in main memory
    // external sorting preferred if data cannot be accommodated in main memory and is kept in auxiliary memory ex. hard disks
    // choice of sorting method depends on
        // amount of machine time needed
        // amount of memory needed
        // time needed for programming sorting method and its complexity
    // each sorting method has a best, worst and amortized running time


    // BUBBLE SORT
    // not suitable for large data sets, avg and worst case time complexity is high
    // repeatedly swaps adjacent elements until sorted
    // O(n^2)
    // not stable, elements with same key value may not maintain their relative order in the sorted output
    cout << "BUBBLE SORT" << endl;
    vector<int> unSorted = {7,2,8,23,5,4,1,6,64,3};
    cout << "before sort" << endl;
    for (int i : unSorted) {
        cout << i << " ";
    }
    cout << "\nafter sort" << endl;
    vector<int> sorted = bubbleSort(unSorted);
    for (int i : sorted) {
        cout << i << " ";
    }
    cout << endl;


    // SELECTION SORT
    // not suitable for large data sets, worst and average case time complexity high
    // repeatedly select smallest or largest element from unsorted portion of list
        // splits array into two subarrays (not literally but figuratively), moves min/max of unsorted elements to left side of list
    // O(n^2)
    // stable sorting algorithm, preservers the relative order of items with equal keys

    cout << "\nSELECTION SORT" << endl;
    cout << "before sort" << endl;
    for (int i : unSorted) {
        cout << i << " ";
    }
    cout << endl;
    cout << "after sort" << endl;
    sorted = selectionSort(unSorted);
    for (int i : sorted) {
        cout << i << " ";
    }
    cout << endl;


    // MERGE SORT
    // in simple terms, divide the array into two halves, sort each half, and merge them back together
    // divide and conquer, recursive
    // run time complexity = O(n logn), space time complexity = O(n)
    // sorts large arrays relatively quickly and easy to implement, popular for large data sets
    // sometimes used with quicksort to improve performance

    cout << "\nMERGE SORT" << endl;
    cout << "before sort" << endl;
    for (int i : unSorted) {
        cout << i << " ";
    }
    cout << endl;
    cout << "after sort" << endl;
    mergeSort(unSorted);
    for (int i : unSorted) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
