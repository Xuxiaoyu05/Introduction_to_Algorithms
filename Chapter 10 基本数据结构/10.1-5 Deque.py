# 习题 10.1-5：栈插入和删除元素都只能在同一端进行，队列的插入操作和删除操作分别在两端进行，与它们不同的，有一种双端队列（deque:double-ended queue），
#             其插入和删除操作都可以在两端进行。写出 4 个时间均为 O(1) 的过程，分别实现在双端队列的两端插入和删除元素的操作，该队列是用一个数组实现的。


# 实现双端队列
class Deque:
  def __init__(self):
    self.deque = []
  
  def is_empty(self):
    return self.deque == []
    
  def enqueue_tail(self, x):
    self.deque.append(x)
  
  def enqueue_head(self, x):
    self.deque.insert(0, x)
  
  def dequeue_head(self):
    if self.is_empty():
      return "Deque underflow"
    else:
      return self.deque.pop(0)
  
  def dequeue_tail(self):
    if self.is_empty():
      return "Deque underflow"
    else:
      return self.deque.pop()
  
myDeque = Deque()
myDeque.enqueue_tail(3)
myDeque.enqueue_tail(4)
myDeque.enqueue_head(5)
myDeque.enqueue_head(6)
print(myDeque.dequeue_head())
print(myDeque.dequeue_tail())
print(myDeque.dequeue_tail())
print(myDeque.dequeue_head())
print(myDeque.dequeue_head()) 
