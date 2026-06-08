class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arrless = []
        arrequal = []
        arrmore = []
        for i in nums:
            if i < pivot:
                arrless.append(i)
            elif i == pivot:
                arrequal.append(i)
            else:
                arrmore.append(i)
        return arrless + arrequal + arrmore
        
        
