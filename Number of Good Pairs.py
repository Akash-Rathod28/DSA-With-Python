class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # num = []
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j] and i < j :
        #             num.append((i,j))
        # return len(num)

        count = {}
        res = 0
        
        for num in nums:
            if num in count:
                res += count[num]
                count[num] += 1
            else:
                count[num] = 1
        
        return res
        
