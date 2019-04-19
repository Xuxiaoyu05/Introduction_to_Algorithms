# 习题7.4-5：当输入数据已经“几乎有序”时，插入排序速度很快。在实际应用中，我们可以利用这一特点来提高快速排序的速度。
#            当对一个长度小于 k 的子数组调用快速排序时，让它不做任何排序就返回。当上层的快速排序调用返回后，对整个数组进行插入排序来完成排序过程。
#            这一排序算法的期望时间复杂度为O(nk+nlg(n/k))：快速排序递归停止在层lg(n/k)，每层的时间代价为O(n)，所以共计O(nlg(n/k)) +
#                                                       插入排序复杂度为 n/k * O(k^2) = O(nk) = O(nk+nlg(n/k))


import time
from random import randint

def InsertSort(A, p, r):
  for i in range(p+1, r+1):
    valToInsert = A[i]
    while i > p and A[i-1] > valToInsert:
      A[i] = A[i-1]
      i -= 1
    A[i] = valToInsert
  return A

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

# 时间复杂度 O(nk+nlg(n/k))
def Mixed_Sort(A, p, r):
  if p < r:
    if r - p < 5:   # 设置 k 值为5
      InsertSort(A, p, r)
    else:
      q = Partition(A, p, r)
      Mixed_Sort(A, p, q-1)
      Mixed_Sort(A, q+1, r)
   return A
   
# alist = [1, 2, 3, 6, 7, 4, 3, 2, 9]
# print(Mixed_Sort(alist, 0, len(alist) - 1))

def Random_Partition(A, p, r):
    i = randint(p, r)
    A[p], A[i] = A[i], A[p]
    return Partition(A, p, r)
    
# 期望运行时间 θ(nlgn)
def Random_QuickSort(A, p, r):
    if p < r:
        q = Random_Partition(A, p, r)
        Random_QuickSort(A, p, q - 1)
        Random_QuickSort(A, q + 1, r)
    return A

if __name__ == "__main__":
    alist = []
    for i in range(1, 10000):
        alist.append(randint(1, 10000))
    start1 = time.time()
    print(Mixed_Sort(alist, 0, len(alist) - 1))
    end1 = time.time()
    print (end1 - start1)

    start2 = time.time()
    print(Random_QuickSort(alist, 0, len(alist) - 1))
    end2 = time.time()
    print (end2 - start1)
