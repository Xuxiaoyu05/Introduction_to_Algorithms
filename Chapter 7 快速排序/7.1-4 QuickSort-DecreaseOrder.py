# 习题7.1-4：如何修改 QuickSort，使得它能够以非递增序进行排序

def Partition(A, p, r):
  pivot = A[p]
  i = p
  for j in range(p+1, r+1):
    if A[j] >= pivot:
      i += 1
      A[i], A[j] = A[j], A[i]
      
  A[p] = A[i]
  A[i] = pivot
  
  return i

def QuickSort(A, p, r):
  if p < r:
    q = Partition(A, p, r)
    QuickSort(A, p, q-1)
    QuickSort(A, q+1, r)
  return A
  
alist = [1, 2, 3, 6, 7, 4, 3, 2, 9]
print(QuickSort(alist, 0, len(alist)-1))
