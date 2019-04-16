# 数组A中有n个数，首先找出A的最小元素并将其与A[1]中的元素进行交换。接着，找出A中的次最小元素并将其与A[2]中的元素进行交换
# 对A中的前 n-1 个元素按该方式继续，该算法被称为选择算法

# 时间复杂度：（1）最好情况：θ(n^2);（2）最坏情况：θ(n^2)； （3）平均情况：θ(n^2)

def SelectionSort(A):
  n = len(A) 
  for i in range(0, n-1):
    min = i
    for j in range(i+1, n):
      if A[j] < A[min]:
        min = j
    A[i], A[min] = A[min], A[i]
  return A
  
alist = [6, 5, 3, 1, 8, 7, 2, 4]
print(SelectionSort(alist))
