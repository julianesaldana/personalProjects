#include <iostream>
#include <vector>

using namespace std;

int maximumWealth(vector<vector<int>> &accounts) {
    int totals[accounts.size()];
    for (int i = 0; i < accounts.size(); i++) {
        int counter = 0;
        for (int j = 0; j < accounts[i].size(); j++) {
            counter += accounts[i][j];
        }
        totals[i] = counter;
    }
    int maximum = totals[0];
    for (int i = 0; i < accounts.size(); i++) {
        if (totals[i] > maximum)
            maximum = totals[i];
    }
    return maximum;
}

int main() {
    vector<vector<int>> accounts = {{2, 8, 7},
                                    {7, 1, 3},
                                    {1, 9, 5}};

    cout << maximumWealth(accounts);
}