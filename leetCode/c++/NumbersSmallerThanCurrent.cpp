//
// Created by julian on 5/20/21.
//

#include <iostream>
#include <vector>

using namespace std;

vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
    vector<int> results;
    int counter = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = 0; j < nums.size(); j++) {
            if (nums[j] < nums[i]) {
                counter++;
            }
        }
        results.push_back(counter);
        counter = 0;
    }

    return results;
}

int main() {
    vector<int> test = {8,1,2,2,3};
    vector<int> results = smallerNumbersThanCurrent(test);
    for (int i = 0; i < results.size(); i++) {
        cout << results[i] << " ";
    }
    return 0;
}