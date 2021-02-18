/*
  利用开源库 uthash.h
  https://troydhanson.github.io/uthash/
*/
#include <stdio.h>   // printf
#include <stdlib.h>  // malloc
#include "uthash.h"  // 开源第三方hash头文件


/*
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/two-sum/solution/liang-shu-zhi-he-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/

struct hashTable {
    int key;
    int val;
    UT_hash_handle hh;
};

struct hashTable* hashtable;

struct hashTable* find(int ikey) {
    struct hashTable* tmp;
    HASH_FIND_INT(hashtable, &ikey, tmp);
    return tmp;
}

void insert(int ikey, int ival) {
    struct hashTable* it = find(ikey);
    if (it == NULL) {
        struct hashTable* tmp = malloc(sizeof(struct hashTable));
        tmp->key = ikey, tmp->val = ival;
        HASH_ADD_INT(hashtable, key, tmp);
    } else {
        it->val = ival;
    }
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    hashtable = NULL;
    for (int i = 0; i < numsSize; i++) {
        struct hashTable* it = find(target - nums[i]);
        if (it != NULL) {
            int* ret = malloc(sizeof(int) * 2);
            ret[0] = it->val, ret[1] = i;
            *returnSize = 2;
            return ret;
        }
        insert(nums[i], i);
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