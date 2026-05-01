class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
            seenA = set()
            seenB = set()
            res = []
            count = 0

            for i in range(len(A)):
                seenA.add(A[i])
                seenB.add(B[i])

                if A[i] in seenB:
                    count += 1
                if B[i] in seenA and A[i] != B[i]:
                    count += 1

                res.append(count)

            return res
