#include <iostream>
#include <cctype>
#include <string>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        string trans;
        for(char c : s){
            if(isalnum(c)){
                trans += tolower(c);
            }
        }
        int left = 0;
        int right = trans.size() -1;
        while(left < right){
            if(trans[left]!=trans[right]){
                return false;
            }
            left+=1;
            right-=1;
        }
        return true;
    }
};
