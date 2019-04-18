# 用最小堆实现最小优先队列


# 一个最小优先序列支持：
#   （1）Insert(S, x)：将元素 x 插入集合 S 中
#   （2）Minimum(S)：返回 S 中具有最小关键字的元素
#   （3）Extract-Min(S)：去掉并返回 S 中的具有最小关键字的元素
#   （4）Decrease-Key(S, x, k)：将元素 x 的关键字减少到 k（假设 k 的值不大于 x 的原关键字）


# 时间复杂度：θ(1)
def Heap_Minimum(A):
  return A[0]

def Min_Heapify(A, root, heapsize):
  left = 2 * root + 1
  right = 2 * root + 2
  
  smaller = root
  if left <= heapsize and A[left] < A[smaller]:
    smaller = left
  if right <= heapsize and A[right] < A[smaller]:
    smaller = right
  
  if smaller != root:
    A[root], A[smaller] = A[smaller], A[root]
    Min_Heapify(A, smaller, heapsize)

# 时间复杂度：O(lgn)
def Heap_Extract_Min(A):
  if len(A) < 1:
    return "heap underflow"
  min = A[0]
  heapsize = len(A) - 1
  A[0] = A[heapsize]
  heapsize -= 1
  Min_Heapify(A, 0, heapsize)
  return min

def Parent(i):
  return (i-1)//2

# 时间复杂度：O(lgn)
def Heap_Decrease_Key(A, i, key):
  if key > A[i]:
    return "New key is larger than current key."  # 如果考虑增大某一位置的优先级，直接调用Min_Heapify将其下移即可
  A[i] = key
  while i > 0 and A[Parent(i)] > A[i]:
    A[i], A[Parent(i)] = A[Parent(i)], A[i]
    i = Parent(i)
  return A

# 时间复杂度：O(lgn)
def Min_Heap_Insert(A, x):
  A.append(float("+inf"))
  heapsize = len(A) - 1
  Heap_Decrease_Key(A, heapsize, x)
  return A

alist = []
print(Heap_Minimum(A))
print(Heap_Extract_Min(A))
print()
