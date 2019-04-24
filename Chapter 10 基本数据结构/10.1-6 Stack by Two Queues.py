# 习题 10.1-6：说明如何用两个队列实现一个栈，并分析相关栈操作的运行时间。

class Stack:
  def __init__(self):
    self.queue1 = []
    self.queue2 = []
  
  def push(self, x):
    if len(self.queue2) == 0:
      self.queue1.append(x)
    else:
      self.queue2.append(x)
      
  def pop(self):
    if len(self.queue1) == 0 and len(self.queue2) == 0:
      return "Stack underflow"
      
    if len(self.queue2) == 0:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        return self.queue1.pop(0)
    
    if len(self.queue1) == 0:
      while len(self.queue2) > 1:
        self.queue1.append(self.queue2.pop(0))
      return self.queue2.pop(0)
 
myStack = Stack()
myStack.push(1)
myStack.push(3)
myStack.push(4)
myStack.push(6)
print(myStack.pop())
myStack.push(5)
myStack.push(8)
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
