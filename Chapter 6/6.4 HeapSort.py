# 堆排序算法：HeapSort

# 输入：无序数组 A
# 输出：排序后的数组 A

# 基本思想：
#   （1）构建最大堆：利用Build_Max_Heap将输入数组A[1...n]建成最大堆
#   （2）元素互换：因为数组中的最大元素总在根结点A[1]中，把它同A[n]进行互换，可以让元素放到正确的位置；然后在堆中去掉结点n，通过减少A.heapsize实现
#   （3）维护最大堆性质：剩余结点中，原来根的孩子结点仍然是最大堆，而新的根结点可能会违背最大堆的性质，调用Max_Heapify(A, 1)来在A[1..n-1]上构建新的最大堆
#   （4）重复上述过程，直到堆的大小从 n-1 降到 2

# 堆排序的时间复杂度 O(nlgn)， 同时堆排序是原址排序（任何时候都只需要常数个额外的元素空间存储临时数据）
def Max_Heapify(A, root, heapsize):
  left = 2 * root  + 1
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
  for i in range(heapsize//2-1, -1, -1):
    Max_Heapify(A, i, heapsize)
  
def HeapSort(A):
    Build_Max_Heap(A)
    heapsize = len(A) - 1
    for i in range(heapsize, 0, -1):
       A[0], A[i] = A[i], A[0]
       heapsize -= 1
       Max_Heapify(A, 0, heapsize) 
    return A
        
alist = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
print(HeapSort(alist))
