# 队列

# 实现过程：利用数组 Q[1...n] 来实现一个最多容纳 n-1 个元素的队列的一种方式。
#          该队列有一个属性 Q.head 指向队头元素，而属性 Q.tail 则指向下一个新元素将要插入的位置。队列中的元素存放在位置 Q.head,Q.head+1,...,Q.tail-1。
#          当 Q.head = Q.tail 时，队列为空。初始时有 Q.head = Q.tail = 1
#          当 Q.head = Q.tail + 1 时，队列是满的
#          出队，入队操作的执行时间均为 O(1)

class Queue:
  def __init__(self):
    self.queue = []
  
  def is_empty(self):
    return self.queue == []
  
  def enqueue(self, x):
    self.queue.append(x)
    
    # if Q.head == Q.tail:
    #   return "Queue overflow"
    # Q[Q.tail] = x
    # if Q.head == None:
    #   Q.head = Q.tail
    # if Q.tail == Q.length:
    #   Q.tail = 1
    # else:
    #   Q.tail = Q.tail + 1
    
  def dequeue(self):
    if self.is_empty():
      return "underflow"
    return self.queue.pop(0)
    
    # if Q.head == None:
    #   return "Queue underflow"
    # x = Q[Q.head]
    # if Q.head == Q.tail:
    #   Q.head = 1
    # else:
    #   Q.head = Q.head + 1
    # if Q.head == Q.tail:
    #   Q.head = None
    # return x
  
  def Size(self):
    return len(self.queue)
 

# 初始化一个队列对象
myQueue = Queue()
print(myQueue.is_empty())
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)
myQueue.enqueue(6)
print(myQueue.Size())
print(myQueue.dequeue())
myQueue.enqueue(8)
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.is_empty())
