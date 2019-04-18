# 习题6.2-5：Max_Heapify 中的递归调用可能导致代码效率较低，请用循环控制结构取代递归，重写Max_Heapify代码

# 时间复杂度O(lgn)
def Max_Heapify(A, root, heapsize):
  while True:
    left = 2 * root + 1
    right = 2 * root + 2

    larger = root

    if left <= heapsize and A[left] > A[larger]:
      larger = left

    if right <= heapsize and A[right] > A[larger]:
      larger = right

    if larger != root:
      A[root], A[larger] = A[larger], A[root]
      root = larger
    else:
      break
   
   return A

A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
heapsize = len(A) - 1
print(Max_Heapify(A, 2, heapsize))
