# 习题6.5-8：Heap-Delete(A, i)操作能够将结点 i 从堆 A 中删除，对于一个包含 n 个元素的堆，请设计一个能够在 O(lgn) 时间内完成的 Heap-Delete 操作

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
    
def Heap_Delete(A, i):    
  heapsize = len(A) - 1
  A[i] = A[heapsize]
  heapsize -= 1
  Max_Heapify(A, i, heapsize)
  return A[:-1]
  
alist = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
print(Heap_Delete(alist, 2))
