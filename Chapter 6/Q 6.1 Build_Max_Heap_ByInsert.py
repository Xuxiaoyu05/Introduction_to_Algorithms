# 思考题6.1：用插入的方式建堆：我们可以通过反复调用 Max-Heap-Insert实现向一个堆中插入元素来构建最大堆

def Parent(i):
  return (i-1)//2
  
def Heap_Increase_Key(B, i, key):
  if key < B[i]:
    return
  B[i] = key
  while i > 0 and B[Parent(i)] < B[i]:
    B[i], B[Parent(i)] = B[Parent(i)], B[i]
    i = Parent(i)

def Max_Heap_Insert(B, x):
  B.append(float("-inf"))
  heapsize = len(B) - 1
  Heap_Increase_Key(B, heapsize, x)
  
def Build_Max_Heap_ByInsert(A):
  B = []
  B.append(A[0])
  for i in range(1, len(A)):
    Max_Heap_Insert(B, A[i])
  return B

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
print(Build_Max_Heap_ByInsert(alist))
print(Build_Max_Heap(alist))
