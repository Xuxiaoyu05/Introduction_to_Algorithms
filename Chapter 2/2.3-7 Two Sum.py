# 描述一个运行时间为 θ(nlgn) 的算法。给定 n 个整数的集合 S 和另一个整数 x ，该算法能确定 S 中是否存在两个其和刚好为 x 的元素


# 方法1：先排序-后用二分查找，时间复杂度 θ(nlgn)

def twoSum(S, x):
  S = MergeSort(S, 0, len(S)-1)
  
  for num in S:
    if BinarySearch(S, x-num) != -1:
      return True
      
  return False
 
# 归并排序
def MergeSort(A, p, r):
  if p < r:
    q = (p+r) // 2
    MergeSort(A, p, q)
    MergeSort(A, q+1, r)
    Merge(A, p, q, r)
  return A
  
def Merge(A, p, q, r):
  n1 = q - p + 1
  n2 = r - q
  
  L = [0] * (n1+1)
  R = [0] * (n2+1)
  
  for i in range(0, n1):
    L[i] = A[p + i]
  
  for j in range(0, n2):
    R[j] = A[q+j+1]
  
  L[n1] = float("+inf")
  R[n2] = float("+inf")
  
  i, j = 0, 0
  
  for k in range(p, r+1):
    if L[i] <= R[j]:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1
 
def BinarySearch(A, p):
  left = 0
  right = len(A) - 1
  
  while left <= right:
    mid = (left + right)//2
    if p == A[mid]:
      return mid
    elif p > A[mid]:
      left = mid + 1
    else:
      right = mid - 1
      
   return -1

alist = [6, 5, 3, 1, 8, 7, 2, 4]
x = 8
print(twoSum(alist, x))
