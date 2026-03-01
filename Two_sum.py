class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] + nums[j] == target:
        #             return [j, i]
        hash1 = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in hash1:
                return [hash1[rem],i]
            hash1[nums[i]] = i
       
                
