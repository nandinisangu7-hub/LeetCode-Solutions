class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j=set(jewels)
        c = 0
        for ch in stones:         
            if ch in j:   
                c += 1
        return c   