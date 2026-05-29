class Solution:
    def minElement(self, nums: List[int]) -> int:
        # result = []
        # for i in nums:
        #     a = len(str(i))
        #     count= 0
        #     for j in str(i):
        #         count += int(j)
        #     result.append(count)
        # return min(result)
        
        minimum = 0
        a = nums[0]
        for i in str(a):
            minimum += int(i)

        for i in nums:
            a = len(str(i))
            count= 0
            for j in str(i):
                count += int(j)
            if minimum > count:
                minimum = count

        return minimum




        
