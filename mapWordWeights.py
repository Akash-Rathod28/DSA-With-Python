class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        lis1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z']

        lis2 = [25,24,23,22,21,20,19,18,17,16,15,14,13,
                12,11,10,9,8,7,6,5,4,3,2,1,0]

        dic = dict(zip(lis2, lis1))

        s = ""

        for i in words:
            total = 0

            for j in i:
                total += weights[ord(j) - ord('a')]

            a = total % 26
            s += dic[a]

        return s
