# 思考题7.1：(Hoare划分的正确性) 本章中的 Partition 算法并不是其最初的版本。下面给出的是最早由 C.R.Hoare 所设计的划分算法：

def Hoare_Partition(A, p, r):
  pivot = A[p]
  i, j = p, r
  
  while True:
    while A[j] >= pivot and j >= 0:
      j -= 1
    while A[i] <= pivot and i <= r:
      i += 1
    
    if i < j:
      A[i], A[j] = A[j], A[i]
  
  A[p] = A[i]
  A[i] = pivot
  
  return i
  
def QuickSort(A, p, r):
  if p < r:
    q = Hoare_Partition(A, p, r)
    QuickSort(A, p, q-1)
    QuickSort(A, q+1, r)
  return A
  
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(QuickSort(alist, 0, len(alist)-1)) 
