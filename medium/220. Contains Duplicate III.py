'''
Given an array of integers, find out whether there are two distinct indices i and j in the array 
such that the absolute difference between nums[i] and nums[j] is at most t 
and the absolute difference between i and j is at most k.

SOL: https://leetcode-cn.com/problems/contains-duplicate-iii/solution/220-cun-zai-zhong-fu-yuan-su-iii-cong-on2-dao-on-p/

kind of bucket sort:

divide nums into M buckets
each nums[i] in one bucket

the rule of deviding: nums[i]// (t+1)
so that adjacent bucket would have max different: 2t +1

Therefore, if nth fit the bucket -> True
else: compare nth + 1 and nth -1, if diff <= t -> True

maintain a certain number of buckets so that it meet the windows "k" in the requirement of index

我们将数据分到 M 个桶 中。
每个数字nums[i] 都被我们分配到一个桶中
分配的依据就是 nums[i] // (t + 1)
这样相邻桶内的数字最多相差2 * t + 1
不相邻的桶一定不满足相差小于等于t
同一个桶内的数字最多相差t
因此如果命中同一个桶内，那么直接返回True
如果命中相邻桶，我们再判断一下是否满足 相差 <= t
否则返回False
需要注意的是，由于题目有索引相差k的要求，因此要维护一个大小为k的窗口，定期清除桶中过期的数字。


'''
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket = {}
        
        for i in range(len(nums)):
            nth = nums[i] // (t+1)
            if nth in bucket:
                return 1
            if nth - 1 in bucket and abs(nums[i] - bucket[nth - 1]) <= t:
                return 1
            if nth + 1 in bucket and abs(nums[i] - bucket[nth + 1]) <= t:
                return 1
            bucket[nth] = nums[i]
            if i>=k:
                bucket.pop(nums[i-k]//(t+1))
            
        return 0