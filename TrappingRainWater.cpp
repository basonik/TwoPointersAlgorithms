//You are given an array of non - negative integers height which represent an elevation map.Each value height[i] represents the height of a bar, which has a width of 1.
//
//Return the maximum area of water that can be trapped between the bars.
//
//Example 1:
//
//
//
//Input: height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
//
//Output : 9

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int max_area = 0;
        int left =0 ;
        int right = height.size() - 1;
        int left_max = 0;
        int right_max = 0;

        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= left_max) {
                    left_max = height[left];
                }
                else {
                    max_area += left_max - height[left];
                }
                left += 1;
            }
            else {
                if (height[right] >= right_max) {
                    right_max = height[right];
                }
                else {
                    max_area += right_max - height[right];
                }
                right -= 1;
            }
            
        }
        return max_area;
    }
};