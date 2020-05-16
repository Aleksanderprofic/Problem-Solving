class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set()
        for j in J:
            jewels.add(j)
        
        i = 0
        for s in S:
            if jewels.__contains__(s):
                i += 1
                
        return i