class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s={}
        for num in arr:
            s[num]=s.get(num,0)+1
        return len(s.values())==len(set(s.values()))            
            
