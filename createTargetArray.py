class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
       
        # for i in range(len(nums)):
        #     if nums[i] == index[i]:
        #         target.append(nums[i])
        #     elif len(target) == 0:
        #         target.append(nums[i])
                
        #     else:
        #         if nums[i] != index[i]:
        #             target.insert(index[i],nums[i])
                
        # return target
        target = [0] * len(nums)
        for i in range(len(index)):
            
            target.insert(index[i],nums[i])
            
        return target[:len(nums)]


        
