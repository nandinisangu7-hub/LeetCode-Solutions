class MyCircularQueue:
    def __init__(self, k: int):
        self.q=[-1]*k
        self.front=-1
        self.rear=-1
        self.c=0
        self.k=k
    def enQueue(self, value: int) -> bool:
        if self.isFull()==True:
            return False
        else:
            self.rear=(self.rear+1)%self.k
            self.q[self.rear]=value
            self.c+=1
            if self.front==-1:
                self.front=0
            return True
    def deQueue(self) -> bool:
        if self.isEmpty()==True:
            return False
        else:
            self.q[self.front]=-1
            self.front=(self.front+1)%self.k
            self.c-=1
            return True
    def Front(self) -> int:
        return self.q[self.front]
        

    def Rear(self) -> int:
        return self.q[self.rear]
        

    def isEmpty(self) -> bool:
        return self.c==0

    def isFull(self) -> bool:
        return self.c==self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()