# 若输入已被排序，则快排算法效率较低，即总是存在某些输入使得算法效率最差。
# 解决方案：在算法中引入随机性，从而使算法对于所有的输入都能获得较好的期望性能。很多人都选择随机化版本的快速排序作为大数据输入情况下的排序算法。

# 基本思想：与始终选择 A[p] 或 A[r] 作为主元的方法不同，随机抽样是从子数组 A[p...r] 中随机选择一个元素作为主元。
# 实现过程：首先将 A[p] 或 A[r] 与从 A[p...r] 中随机选出的一个元素交换。因为主元元素是随机选取的，因此在平均情况下对于输入数组的划分是比较均衡的。

from random import randint

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
  i = randint(p, r)
  A[p], A[i] = A[i], A[p]
  return Partition(A, p, r)
 
# 期望运行时间 θ(nlgn)
def Random_QuickSort(A, p, r):
  if p < r:
    q = Random_Partition(A, p, r)
    Random_QuickSort(A, p, q-1)
    Random_QuickSort(A, q+1, r)
  return A
  
alist = [1, 2, 3, 6, 7, 4, 3, 2, 9]
print(Random_QuickSort(alist, 0, len(alist) - 1))
