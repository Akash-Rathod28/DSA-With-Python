class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # num = []
        # num1 = []
        # for i in range((len(nums)//2)):
        #     num.append(nums[i])
        # for i in range((len(nums)//2),len(nums)):
        #     num1.append(nums[i])
        # i = 1
        # for j in range(len(num1)):
        #     num.insert(i,num1[j])
        #     i += 2
        # return num
        result = []
        for i in range(n):
            result.append(nums[i])     # Element from first half: x1, x2...
            result.append(nums[i + n]) # Element from second half: y1, y2...
        return result


        
