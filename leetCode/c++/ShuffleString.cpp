//
// Created by julian on 5/20/21.
//

#include <iostream>
#include <vector>

using namespace std;

string restoreString(string s, vector<int>& indices) {
    string result = s;
    for (int i = 0; i < indices.size(); i++) {
        result[i] = s[indices[i]];
    }
    return result;
}

int main() {
    string s = "codeleet";
    vector<int> indices = {4,5,6,7,0,2,1,3};
    cout << restoreString(s, indices);
    return 0;
}