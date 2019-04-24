# 习题 10.1-6：说明如何用两个栈实现一个队列，并分析相关队列操作的运行时间。

class Queue:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []
  
  def enqueue(self, x):
    self.stack1.append(x)

  def dequeue(self):
    if len(self.stack1) == 0 and len(self.stack2) == 0:  # 别忘了判断下溢条件
      return "underflow"
      
    if len(self.stack2) == 0:
      while len(self.stack1) != 0:
        self.stack2.append(self.stack1.pop())
        
    return self.stack2.pop()


myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(3)
myQueue.enqueue(4)
print(myQueue.dequeue())
myQueue.enqueue(6)
myQueue.enqueue(8)
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
