class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        
        def get_min_total_time(start1: list[int], dur1: list[int], start2: list[int], dur2: list[int]) -> int:
            min_end = min(s + d for s, d in zip(start1, dur1))
            return min(max(min_end, s) + d for s, d in zip(start2, dur2))
        
        land_first = get_min_total_time(landStartTime, landDuration, waterStartTime, waterDuration)
        water_first = get_min_total_time(waterStartTime, waterDuration, landStartTime, landDuration)
        
        return min(land_first, water_first)
