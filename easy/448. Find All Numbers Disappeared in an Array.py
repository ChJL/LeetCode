class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        for ele in nums:
            if ele != i +1:
                # first go through all elements, if position doesn't match replace with 0
                nums[i] = 0
                # then use while loop put the ele into correct position, until (1) the ele is already in right pos, 
                # or (2) the value in that index is 0 which is replaced before
                # for these two cases -> while loop end
                while nums[ele -1] != ele:
                    # judge the 0 
                    if nums[ele-1]:
                        tmp = nums[ele-1]
                        nums[ele -1] = ele
                        ele = tmp
                    else: 
                        # 0 case
                        nums[ele -1] = ele
            i+=1
        
        # Finally, the position with zero in it are the disappeared one
        res = []
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                res.append(j+1)
            j+=1
        return res