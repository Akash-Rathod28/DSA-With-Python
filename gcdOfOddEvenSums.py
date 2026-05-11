class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_numbers = []
        even_numbers = [1]
        for i in range(1,n+1):
            odd_numbers.append(i*2)
        for j in range(n-1):
            even_numbers.append(even_numbers[-1]+2)
        return gcd(sum(odd_numbers),sum(even_numbers))
        
