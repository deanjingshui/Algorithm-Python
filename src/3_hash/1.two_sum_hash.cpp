#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> ret;

        // 构建映射关系
        map<int,int> nums_map;
        for(int i=0;i<n;i++)
        {   
            nums_map[nums[i]] = i;
        }

        // 遍历映射表
        map<int,int>::iterator iter;
        for(int i=0;i<n-1;i++)
        {
            iter = nums_map.find(target-nums[i]);
            if(iter != nums_map.end())
            {
                ret = {i,iter->second};
                return ret;
            }
        }

        ret.push_back(0);
        return ret;
    }
};


int main(){

    // 创建整数数组
    int numsSize = 4;
    vector<int> nums = {1,7,1,2};

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
