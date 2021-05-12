"""
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. 
All the scores are guaranteed to be unique.

Return an array answer of size n where answer[i] is the rank of the ith athlete.

Example 1:
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

Example 2:
Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

SOL: simple dict(hash table)
"""
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = sorted(score, reverse=True)
        d = {}
        pos = 1
        for i in rank:
            if pos ==1:
                d[i] = "Gold Medal"
            elif pos ==2:
                d[i] = "Silver Medal"
            elif pos ==3:
                d[i] = "Bronze Medal"
            else:
                d[i] = str(pos)
            pos+=1
        
        res=[]
        for i in score:
            res.append(d[i])
        return res
        