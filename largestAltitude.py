class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # alt = [0]
        # for res in gain:
        #     alt.append(alt[-1] + res)
        # return max(alt)
        i = 1
        while i<len(gain):
            gain[i] += gain[i-1]
            i += 1
        gain.insert(0,0)
        return max(gain)
        
