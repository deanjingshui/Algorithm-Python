#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ret;
        for(int i=0;i<nums.size()-1;i++)
        {   
            for(int j=i+1;j<nums.size();j++)
            {
                if((nums[i] + nums[j]) == target)
                {   
                    ret.push_back(i);
                    ret.push_back(j);
                    return ret;
                }
            }
        }
        ret.push_back(0);
        return ret;
    }
};


int main(){

    // 创建整数数组
    int numsSize = 4;
    vector<int> nums = {1,7,1,1};

    int target = 9;
    vector<int> ret;

    Solution mySolution;
    ret = mySolution.twoSum(nums,target);
    if (ret.size()==2)
    {
        cout << "the result is: " << ret[0] << "," <<ret[1] << endl;
    }
    else
    {
        cout << "the result is NULL" << endl;
    }
}
