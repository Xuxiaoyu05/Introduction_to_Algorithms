# 在归并排序中对小数组采用插入排序

# 基本思想：
#     虽然归并排序最坏情况下运行时间为θ(nlgn)，插入排序的最坏情况运行时间为θ(n^2)；
#     但是插入排序中的常量因子可能使得它在 n 较小时，在许多机器上实际运行的更快；
#     因此，当归并排序中子问题变得足够小时，采用插入排序来使递归的叶变粗是有意义的

# 对归并排序的一种修改：使用插入排序来排序长度为 k 的 n/k 个子表，然后使用标准的合并机制来合并这些子表，其中 k 是一个特定的值。

# 时间复杂度：（1）插入排序最坏情况下可以在 θ(nk) 时间内排序每个长度为k的n/k个子表；（2）最坏情况在合并这些子表时间为θ(nlg(n/k))
# 修改后的算法的最坏运行时间为 θ(nk + nlg(n/k)) 


def MixedSort(A, p, r):
  if p >= r:
    return
  elif r - p < 5:  # k 值
    InsertSort(A, p, r)
  else:
    q = (p + r)//2
    MixedSort(A, p, q)
    MixedSort(A, q+1, r)
    Merge(A, p, q, r)
  return A

def InsertSort(A, p, r):
  for i in range(p+1, r+1):
    valToInsert = A[i]
    while i >= p+1 and A[i-1] > valToInsert:
      A[i] = A[i-1]
      i -= 1
    A[i] = valToInsert
    
  return A


# 合并
def Merge(A, p, q, r):
  n1 = q - p + 1
  n2 = r - q
  
  L = [0] * (n1+1)
  R = [0] * (n2+1)
  
  for i in range(0, n1):
    L[i] = A[p+i]
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
      
      
alist = [6, 5, 3, 1, 8, 7, 2, 4,11,13,45,26,18,26,35,50,15,29,62,88,24,9]
print(MixedSort(alist,0,len(alist)-1))
