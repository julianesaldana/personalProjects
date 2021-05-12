#include <iostream>
#include <vector>

using namespace std;

vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
    vector<bool> results;
    int maximum = candies[0];
    for (int i = 0; i < candies.size(); i++) {
        if (candies[i] + extraCandies >= maximum) {
            results.push_back(true);
        } else {
            results.push_back(false);
        }
    }
    return results;
}

/* given an array, where the ith element represents the amount of candies the ith kid has, given
   an amount of extra candies, could the ith kid with the extra candies have the most candies out of everyone
   else in the list?
*/
int main() {
    vector<int> candies = {1,2,3,4,5};
    int extraCandies = 3;
    vector<bool> results = kidsWithCandies(candies, extraCandies);
    for (int i = 0; i < results.size(); i++) {
        cout << results[i] << endl;
    }
    return 0;
}
