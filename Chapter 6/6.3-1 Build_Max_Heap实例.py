# 习题6.3-1：说明Build_Max_Heap在数组A = <5, 3, 17, 10, 84, 19, 6, 22, 9>上的执行结果

# 时间复杂度 O(lgn)
def Max_Heapify(A, root, heapsize):
  left = 2 * root + 1    # 因为Python中下标从0开始，所以此处应该是2i+1
  right = 2 * root + 2

  larger = root
  
  if left <= heapsize and A[left] > A[larger]:
    larger = left 

  if right <= heapsize and A[right] > A[larger]:
    larger = right

 
  if larger != root:
    A[root], A[larger] = A[larger], A[root]
    Max_Heapify(A, larger, heapsize)
   

# 时间复杂度 O(n)
def Build_Max_Heap(A):

  heapsize = len(A) - 1

  for i in range((heapsize-1)//2, -1, -1):    # 在Python中，由于下标是从0开始，所以(heapsize-1)//2是最后一个非叶子结点

    Max_Heapify(A, i, heapsize)
    
  return A
    
    
A = [5, 3, 17, 10, 84, 19, 6, 22, 9]
print(Build_Max_Heap(A))
