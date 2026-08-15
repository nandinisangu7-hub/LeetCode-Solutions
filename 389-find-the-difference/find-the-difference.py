class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ss=sum(ord(ch) for ch in s)
        tt=sum(ord(ch) for ch in t)
        diff=tt-ss
        return chr(diff)

        