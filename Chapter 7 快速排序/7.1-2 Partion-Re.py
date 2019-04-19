# 习题7.1-2：当数组 A[p...r] 元素都相同时，Partition 返回的 q 值是什么？ 答：r
#            修改 Partition，使得当数组 A[p...r] 中所有元素的值都相同时，q = ⌊(p+r)/2⌋


def Partition(A, p, r):
  pivot = A[p]
  i = p
  count = 0
  
  for j in range(p+1, r+1):
    if A[j] == pivot:
      count += 1
    if A[j] <= pivot:      
      i += 1
      A[i], A[j] = A[j], A[i]
          
  A[p] = A[i]
  A[i] = pivot
  
  return i - count//2
  
  
def QuickSort(A, p, r):
  if p < r:
    q = Partition(A, p, r)
    QuickSort(A, p, q-1)
    QuickSort(A, q+1, r)
  return A
  
 alist = [1, 1, 1, 1, 1, 1, 1, 1, 1]
 print(QuickSort(alist, 0, len(alist)-1))
