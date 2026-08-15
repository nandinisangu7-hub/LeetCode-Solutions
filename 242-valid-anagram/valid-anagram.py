class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        f={}
        for val in s:
            f[val]=f.get(val,0)+1
        ft={}
        for val in t:
            ft[val]=ft.get(val,0)+1
        return f==ft