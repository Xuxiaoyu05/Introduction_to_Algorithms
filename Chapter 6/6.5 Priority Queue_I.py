# 优先队列

# 定义：（1）是一种用来维护由一组元素构成的集合S的数据结构。其中的每一个元素都有一个相关的值，称为关键字。《算法导论》
#       （2）通俗定义：普通的队列是一种先进先出的数据结构，元素在队尾追加，在队头删除。在优先队列中，元素被赋予优先级。
#                     当访问元素时，具有最高优先级的元素最先删除。优先队列具有最高级先出 （first in, largest out）的行为特征。
#                     通常采用堆数据结构来实现。

# 分类：（1）最大优先队列（基于最大堆实现） （2）最小优先队列（基于最小堆实现）

# 应用：（1）最大优先队列的一个常见应用是共享计算机系统的作业调度。当一个作业完成或被中断后，调度器从所有的等待作业中，选出具有最高优先级的作业来执行。
#       （2）最小优先队列的一个常见应用是基于事件驱动的模拟器。队列中保存要模拟的事件，每个事件都有一个发生时间作为其关键字。
#            事件必须按照发生的时间顺序进行模拟。

# 一个最大优先序列支持：
#   （1）Insert(S, x)：将元素 x 插入集合 S 中
#   （2）Maximum(S)：返回 S 中具有最大关键字的元素
#   （3）Extract-Max(S)：去掉并返回 S 中的具有最大关键字的元素
#   （4）Increase-Key(S, x, k)：将元素 x 的关键字增加到 k（假设 k 的值不小于 x 的原关键字）

def Max_Heapify(A, root, heapsize):
  left = 2 * i + 1
  right = 2 * i + 2
  
  larger = root
  if left <= heapsize and A[left] > A[larger]:
    larger = left
  if right <= heapsize and A[right] > A[larger]:
    larger = right
  
  if larger != root:
    A[root], A[larger] = A[larger], A[root]
    Max_Heapify(A, larger, heapsize)
    
 
# 返回 S 中具有最大关键字的元素，时间复杂度θ(1)
def Heap_Maximum(A):
  return A[0]

# 去掉并返回 S 中的具有最大关键字的元素，时间复杂度θ(lgn)
def Heap_Extract_Max(A):
  if len(A) < 1:
    return "heap underflow"
  max = A[0]
  heapsize = len(A) - 1
  A[0] = A[heapsize]
  heapsize -= 1
  Max_Heapify(A, 0, heapsize)
  return max


def Parent(i):
  return (i-1)//2         # Python 中 i 结点的父结点

# 将元素 x 的关键字增加到 k（假设 k 的值不小于 x 的原关键字），时间复杂度θ(lgn)
def Heap_Increase_Key(A, i, k):
  if key < A[i]:
    return "New key is smaller than current key."
  A[i] = key
  while i > 0 and A[Parent(i)] < A[i]:
    A[i], A[Parent(i)] = A[Parent(i)], A[i]
    i = Parent(i)
    
# 将元素 x 插入集合 S 中，时间复杂度
# 实现过程：
    
  




