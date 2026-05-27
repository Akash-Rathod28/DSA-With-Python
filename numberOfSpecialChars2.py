

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_occurrence = {}
        last_occurrence = {}
        
        for i, char in enumerate(word):
            if char not in first_occurrence:
                first_occurrence[char] = i
            last_occurrence[char] = i
            
        count = 0
        for lower, upper in zip(string.ascii_lowercase, string.ascii_uppercase):
            if lower in last_occurrence and upper in first_occurrence:
                if last_occurrence[lower] < first_occurrence[upper]:
                    count += 1
                    
        return count
