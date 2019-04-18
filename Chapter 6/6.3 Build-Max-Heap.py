# 构建最大堆

# 输入：数组 A

# 实现过程：采用“自底向上”的方法将数组A[1...n]构建为最大堆，通过6.1-7可知，子数组A(⌊n/2⌋+1...n)中的元素都是叶结点，每个叶结点都可看成只包含一个元素的堆
#          过程Build-Max-Heap对树中的非叶子结点都调用一次Max-Heapify
#          采用“自底向上”的方法是因为在调用Max-Heapify过程时需要确保其左子树和右子树都是最大堆


def Max_Heapify(A, root, heapsize):
  left = 2 * root + 1    # 因为Python中下标从0开始，所以此处应该是2i+1
  right = 2 * root + 2

  larger = root

  if left < heapsize and A[left] > A[larger]:  # 此处相较之前的Max_Heapify有所改动，因为在构建最大堆时，最后非叶子结点为heapsize//2-1，heapsize为len(A)所以不能等于
    larger = left

  if right < heapsize and A[right] > A[larger]:
    larger = right

  

  if larger != root:
    A[root], A[larger] = A[larger], A[root]
    Max_Heapify(A, larger, heapsize)
    
  return A

# 时间复杂度：O(n), 可在线性时间内，将一个无序数组构造成为一个最大堆
def Build_Max_Heap(A):
  heapsize = len(A)
  for i in range(heapsize//2-1, -1, -1):    # 在Python中，由于下标是从0开始，所以heapsize//2-1是最后一个非叶子结点
    Max_Heapify(A, i, heapsize)
    
# 构建最小堆：时间复杂度 O(n)
def Build_Min_Heap(A):
  heapsize = len(A) - 1
  for i in range(heapsize//2-1, -1, -1):
    Min_Heapify(A, i, heapsize)
