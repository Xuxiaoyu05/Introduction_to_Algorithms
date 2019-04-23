# 目的：从一个由 n 个元素构成的集合中选择第 i 个顺序统计量
# 解法1：用堆排序或归并排序对输入数据进行排序，然后在输出数组中根据下标找出第 i 个元素即可。时间复杂度 O(nlgn)

# 优化解法：期望为线性时间的选择算法（用分治算法来解决选择问题）

# 基本思想：以快速排序算法为模型，将输入数组进行递归划分；但与快速排序不同的是，快速排序会递归处理划分的两边，而 Random_Select 只处理划分的一边。
#          假设输入元素互异，快速排序的期望运行时间为θ(nlgn)，而 Random_Select 的期望运行时间为θ(n)。

# 输出：返回数组 A[p...r] 中第 i 小的元素

import random

def Partition(A, p, r):
  pivot = A[p]
  i = p
  for j in range(p+1, r+1):
    if A[j] <= pivot:
      i += 1
      A[i], A[j] = A[j], A[i]
      
  A[p] = A[i]
  A[i] = pivot
  
  return i
  
def Random_Partition(A, p, r):
  i = random.randint(p, r)
  A[p], A[i] = A[i], A[p]
  return Partition(A, p, r)
  
# 最坏情况运行时间为θ(n^2)，由于是随机化的，因此期望运行时间为θ(n)
def Random_Select(A, p, r, i):
  if p == r:   # 递归的基本情况
    return A[p]
    
  q = Random_Partition(A, p, r)
  k = q - p + 1
  
  if k == i:
    return A[q]
  elif k > i:
    return Random_Select(A, p, q-1, i)
  else:
    return Random_Select(A, q+1, r, i-k)
    
alist = []
for i in range(0, 15):
  alist.append(random.randint(1, 20))
print(alist)
print(Random_Select(alist, 0, len(alist)-1, 5))
