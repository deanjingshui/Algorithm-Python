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