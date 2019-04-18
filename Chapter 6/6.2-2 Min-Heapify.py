# 习题6.2-2：Min_Heapify 维护最小堆性质

# 时间复杂度O(lgn)
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
  
  return A
