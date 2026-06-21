class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # nums = [0]
        # for i in costs:
        #     if sum(nums) + i <= coins:
        #         nums.append(i)
        # nums.pop(nums[0])
        # return len(nums)
        costs.sort()
        count = 0
        val = 0
        for i in costs:
            if count + i <= coins:
                count += i
                val += 1
            else:
                break
        return val

        
