class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        
       
   
        for _ in range(len(score)):  # run multiple passes
            for i in range(len(score) - 1):
                if score[i][k] < score[i + 1][k]:
                    score[i], score[i + 1] = score[i + 1], score[i]
        return score

        
