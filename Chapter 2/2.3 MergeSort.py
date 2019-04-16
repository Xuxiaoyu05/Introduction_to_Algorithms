#  分治法三步骤：
# （1）分解：将原问题分解为若干子问题，这些子问题是原问题的规模较小的实例；
# （2）解决：递归的求解各子问题，若子问题规模足够小，则直接求解；
# （3）合并：将这些子问题的解合并成原问题的解

# 归并排序完全遵循分治模式：
# （1）分解：将待排序的n个元素的序列分成各具n/2个元素的两个子序列
# （2）解决：使用归并排序递归地排列两个子序列
# （3）合并：合并两个已排序的子序列以产生已排序的答案

# 当待排序的长度为1时，递归“开始回升”，因为长度为1的每个序列都已排好序

# 归并排序算法时间复杂度：θ(nlgn)

def MergeSort(A, p, r):
  if p < r:  # 待排序的子问题中至少包括两个元素
    q = (p+r) // 2
    MergeSort(A, p, q)
    MergeSort(A, q+1, r)
    Merge(A, p, q, r)
  return A  # 要有返回值

# Merge操作时间复杂度为θ(n)
def Merge(A, p, q, r):
  n1 = q - p + 1
  n2 = r - q
  
  left = [0] * (n1 + 1)
  right = [0] * (n2 + 1)
  
  for i in range(0, n1):
    left[i] = A[p + i]
  for j in range(0, n2):
    right[j] = A[q + j + 1]
  
  # 哨兵
  left[n1] = float("+inf")
  right[n2] = float("+inf")
  
  i, j = 0, 0
  for k in range(p, r+1):
    if left[i] <= right[j]:
      A[k] = left[i]
      i += 1
    else:
      A[k] = right[j]
      j += 1

alist = [6, 5, 3, 1, 8, 7, 2, 4]
print(MergeSort(alist, 0, len(alist)-1))
