# 栈和队列

# 基本概念：栈和队列都是动态集合。
# （1）栈：后进先出（Last-In, First-Out，LIFO），即在栈中，被删除的是最近插入的元素。
# （2）队列：先进先出（First-In, First-Out, FIFO），即在队列中，被删除的总是在集合中存在时间最长的那个元素。

# 栈
# 可以用一个数组 S[1..n] 来实现一个最多可容纳 n 个元素的栈。该数组有一个属性 S.top，指向最新插入的元素。栈中包含的元素 S[1...S.top]，
# 其中 S[1] 是栈底元素，S[S.top] 是栈顶元素。当 S.top = 0 时，栈中不包含任何元素，即栈是空的。
# 出栈，入栈等操作的执行时间均为 O(1)

class Stack:
  def __init__(self):
    self.stack = []
  
  def is_empty(self):
    return self.stack == []
    # return stack.top == 0
   
  # 入栈
  def Push(self, x):
    self.stack.append(x)
    # S.top += 1
    # S[S.top] = x
  
  # 出栈
  def Pop(self):
    if self.is_empty():
      return "underflow"
    return self.stack.pop()
    
    # else:
    #   S.top -= 1
    #   return S[S.top+1]
  
  # 返回栈顶元素
  def Peek(self):
    return self.stack[-1]
  
  # 返回栈的大小
  def Size(self):
    return len(self.stack)
    
# 初始化一个栈对象
myStack = Stack()

print(myStack.is_empty())
myStack.Push(3)
myStack.Push(4)
myStack.Push(5)
myStack.Push(6)
print(myStack.Size())
print(myStack.Peek())
print(myStack.Pop())
myStack.Push(8)
print(myStack.Pop())
print(myStack.is_empty())
