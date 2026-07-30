from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        freqs = sorted(counts.values(), reverse=True)
        
        total_pushes = 0
        for i, freq in enumerate(freqs):
            total_pushes += freq * ((i // 8) + 1)
            
        return total_pushes
