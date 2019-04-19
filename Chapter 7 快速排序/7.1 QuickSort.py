# 快速排序通常是实际排序应用中最好的选择。
# （1）它的平均性能非常好，它的期望时间复杂度为θ(nlgn)，且θ(nlgn)中隐含的常数因子非常小
# （2）快速排序是原址排序，甚至在虚存环境中也能很好的工作
# （3）最坏情况下， 即当输入数组已经完全有序时，快速排序的时间复杂度为θ(n^2)。而在同样情况下，插入排序的复杂度为θ(n)
# （4）事实上，任何一种常数比例的划分，即使是99:1都会产生深度为θ(lgn)的递归树，其中每一层的时间代价都是O(n)。
#      因此，只要划分是常数比例的，算法的运行时间总是O(nlgn)
# （5）在平均情况下，Partition 假设好的划分（最好情况）和差的划分（最差情况）交替出现在树的各层上，快速排序的时间复杂度依然为O(nlgn)

# 基本思想：采用“分治”思想。
#         （1）分解：数组 A[p...r] 被划分为两个（可能为空）的子数组 A[p...q-1]，A[q+1...r]，使得 A[p...q-1] 中的每一个元素都小于等于 A[q]，
#                   而 A[q] 也小于等于 A[q+1...r] 中的每个元素。
#         （2）解决：通过递归调用快速排序，对子数组 A[p...q-1] 和 A[q+1...r] 进行排序
#         （3）合并：因为子数组都是原址排序的，所以不需要合并操作，数组 A[p...r] 已经有序

# 性质：（1）若 p <= k <= i，则 A[k] <= x；（2）若 i+1 <= k <= j-1，则 A[k] > x

# Partition 时间复杂度为θ(n)，n = r - p + 1
def Partition(A, p, r):
  pivot = A[p]   # 以最左边元素为基准
  i = p
  for j in range(p+1, r+1):
    if A[j] <= pivot:
      i += 1
      A[i], A[j] = A[j], A[i]
      
  A[p] = A[i]
  A[i] = pivot
  
  return i

def Partition_II(A, p, r):
  pivot = A[r]
  i = p - 1
  for j in range(p, r):
    if A[j] <= pivot:
      i += 1
      A[i], A[j] = A[j], A[i]
      
  A[r] = A[i+1]
  A[i+1] = pivot
  
  return i+1
  
def QuickSort(A, p, r):
  if p < r:   # 数组中不止一个元素
    q = Partition(A, p, r)
    QuickSort(A, p, q-1)
    QuickSort(A, q+1, r)
  return A

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(QuickSort(alist, 0, len(alist)-1))
