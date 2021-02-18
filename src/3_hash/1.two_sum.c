/* 
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]

提示：
2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
*/

#include <stdio.h>   // printf
#include <stdlib.h>  // malloc

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
/* 本题难点在对函数参数的理解上
   建议nums加const修饰，表示入参不可修改
   returnSize这个应该是出参
*/
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    for(int i=0;i<numsSize-1;i++)
    {   
        for(int j=i+1;j<numsSize;j++)
        {
            if((nums[i] + nums[j]) == target)
            {   
                int* ret = malloc(sizeof(int)*2);
                ret[0] = i;
                ret[1] = j;
                *returnSize = 2;
                return ret;
            }
        }
    }
    *returnSize = 0;
    return NULL;
}


int main(){

    // 创建整数数组
    int numsSize = 4;
    int nums[4] = {1,7,1,2};

    int target = 20;
    int* ret;
    int returnSize;

    ret = twoSum(nums,numsSize,target,&returnSize);
    if (ret!=NULL)
    {
        printf("the result is: %d,%d\n",ret[0],ret[1]);  // the result is: 1,3
        // printf("the result is: %d,%d\n",*ret,*(ret++));  // the result is: 3,1
    }
    else
    {
        printf("the result is NULL\n");
    }
}