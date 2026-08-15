class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        d=deque(range(1,n+1))
        while(len(d)>1):
            for i in range(k-1):
                d.append(d.popleft())
            d.popleft()
        return d[0] 