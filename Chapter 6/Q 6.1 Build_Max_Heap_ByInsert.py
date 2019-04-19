# 思考题6.1：用插入的方式建堆：我们可以通过反复调用 Max-Heap-Insert实现向一个堆中插入元素来构建最大堆

def Parent(i):
  return (i-1)//2
  
def Heap_Increase_Key(A, i, key):
  if key < A[i]:
    return
  A[i] = key
  while i > 0 and A[Parent(i)] < A[i]:
    A[i], A[Parent(i)] = A[Parent(i)], A[i]
    i = Parent(i)

# 时间复杂度O(n)
def Max_Heap_Insert(A, x, heapsize):
  A[heapsize] = float("-inf")
  Heap_Increase_Key(A, heapsize, x)

# 最坏情况下，时间复杂度θ(nlgn)
def Build_Max_Heap_ByInsert(A):
  heapsize = 1
  for i in range(1, len(A)):
    Max_Heap_Insert(A, A[i], heapsize)
    heapsize += 1
  return A

def Max_Heapify(A, root, heapsize):
  left = 2 * root + 1
  right = 2 * root + 2
  
  larger = root
  if left <= heapsize and A[left] > A[larger]:
    larger = left
  if right <= heapsize and A[right] > A[larger]:
    larger = right
  
  if larger != root:
    A[root], A[larger] = A[larger], A[root]
    Max_Heapify(A, larger, heapsize)
    
def Build_Max_Heap(A):
  heapsize = len(A) - 1
  for i in range((heapsize-1)//2, -1, -1):
    Max_Heapify(A, i, heapsize)
  return A
  
alist = [1,2,3,4,5,6,7,8]
print(Build_Max_Heap_ByInsert(alist))  # 最大堆结果为[8, 7, 6, 4, 3, 2, 5, 1]
print(Build_Max_Heap(alist))  # 最大堆结果为[8, 5, 7, 4, 1, 6, 3, 2]

# 6.1(a)：当输入数据相同的时候，Build-Max-Heap和Build_Max_Heap_ByInsert生成的堆不总是一样，如上所示。
# 6.1(b)：在最坏情况下，Build_Max_Heap_ByInsert建立一个包含 n 个元素的堆的时间复杂度是θ(nlgn)。lg2+lg3+...+lgn = lg(n!) = θ(nlgn)
