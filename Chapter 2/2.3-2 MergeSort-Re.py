# 改写过程 Merge，使之不使用哨兵，而是一旦数组 L 和 R 的所有元素均被复制回 A 就立刻停止，然后把另一个数组的剩余部分复制回 A

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
  
  L = [0] * n1
  R = [0] * n2
  
  for i in range(0, n1):
    L[i] = A[p+i]
  
  for j in range(0, n2):
    R[j] = A[q+j+1]
    
  i, j, k = 0, 0, p    # 此处，k不为0，k为左边界p
  
  while i < n1 and j < n2:
    if L[i] <= R[j]:
      A[k] = L[i]
      i += 1
    else:
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

alist = [6, 5, 3, 1, 8, 7, 2, 4]
print(MergeSort(alist, 0, len(alist)-1))
