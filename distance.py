class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # num = []
        # add = 0
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j]:
        #             add += abs(i-j)
        #     num.append(add)
        #     add = 0
        # return num

        
        result = []

        for i in range(len(nums)):
            total = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    total += abs(i - j)
            result.append(total)

        return result
                
            
                

        
