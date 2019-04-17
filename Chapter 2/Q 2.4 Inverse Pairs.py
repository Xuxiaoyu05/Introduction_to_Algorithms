# 逆序对

# 假设A[1...n]是一个有 n 个不同数的数组，若 i < j 且 A[i] > A[j]，则对偶(i, j)称为 A 的一个逆序对

# 给出一个确定在 n 个元素的任何排列中逆序对数量的算法，最坏情况需要 θ(nlgn)时间

# 计算逆序对：归并排序的修改版，时间复杂度 θ(nlgn)

def InversePairs(A):
  return MergeSort(A, 0, len(A)-1)

def MergeSort(A, p, r):
  count = 0
  if p < r:
    q = (p+r) // 2
    count += MergeSort(A, p, q)
    count += MergeSort(A, q+1, r)
    count += Merge(A, p, q, r)
    return count
  else:
    return 0
  
def Merge(A, p, q, r):
  res = 0
  n1 = q - p + 1
  n2 = r - q
  
  L = [0] * n1
  R = [0] * n2
  
  for i in range(0, n1):
    L[i] = A[p+i]
  for j in range(0, n2):
    R[j] = A[q+j+1]
  
  i, j, k = 0, 0, p
  
  while i < n1 and j < n2:
    if L[i] <= R[j]:
      A[k] = L[i]
      i += 1
    else:
      res += n1 - i
      A[k] = R[j]
      j += 1
    k += 1
  
  while i < n1:
    A[k] = L[i]
    i += 1
    k += 1
  
  while j < n2:
    A[k] = R[j]
    j += 1
    k += 1
  
  return res
  
  
alist = [2, 3, 8, 6, 1]
print(InversePairs(alist))
