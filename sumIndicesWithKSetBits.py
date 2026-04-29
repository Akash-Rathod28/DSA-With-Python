class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
       #count = 0
       #for i in range(len(nums)):
           #a = str(bin(i)[2:])
           #if a.count("1") == k:
               #count += nums[i]
       #return count
       
        binary = []
        add = []
        result = []
        for i in range(len(nums)):
            binary.append(bin(i)[2:])
        for idx,val in enumerate(binary):
            a = str(val)
            if a.count("1") == k:
                add.append(idx)
        for res in add:
            result.append(nums[res])
        return sum(result)
       
       
