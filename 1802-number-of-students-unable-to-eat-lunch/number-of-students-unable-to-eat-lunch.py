class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        d=deque(students)
        i=0
        c=0
        while i<len(sandwiches):
            if sandwiches[i]==d[0]:
                i+=1
                d.popleft()
                c=0
            else:
                x=d.popleft()
                d.append(x)
                c+=1
            if c==len(d):
                return len(d)
        return 0



        