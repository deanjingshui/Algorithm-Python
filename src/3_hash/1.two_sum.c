#include <stdio.h>   // printf
#include <stdlib.h>  // malloc

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
/* 本题难点在对函数参数的理解上
 * 建议nums加const修饰，表示入参不可修改
 * returnSize这个应该是出参
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


/* 本题涉及C语言知识点：函数如何返回数组（指针）
    参考：https://segmentfault.com/q/1010000018689506/a-1020000018689706
    数组名实际上就是指针，因此返回数组就是返回一个指针。但有一点要特别注意的是：不要返回指向局部变量的指针或引用
    局部变量的生命周期仅限于定义它的函数作用域内，离开函数局部变量就无效了，此时再通过指针访问该变量将导致不可预
    知的结果。
    通常解决这个问题的方式有两种：
     1.将数组声明为静态的
     2.使用malloc()动态分配内存
 */