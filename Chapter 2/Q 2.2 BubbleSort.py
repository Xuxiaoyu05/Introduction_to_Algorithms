# 冒泡排序：反复交换相邻的未按次序排列的元素

# 时间复杂度：最好，最坏情况下都是θ(n^2)
def BubbleSort(A):
  for i in range(0, len(A) - 1):
    for j in range(len(A) - 1, i, -1):
      if A[j] < A[j-1]:
        A[j], A[j-1] = A[j-1], A[j]
  return A
 
alist = [6, 5, 3, 1, 8, 7, 2, 4]
print(BubbleSort(alist))


# 改进后的冒泡排序

# 时间复杂度：最好情况下θ(n), 最坏情况下θ(n^2)
def BubbleSort_Optimize(A):
  exchange = True
  i = 0
  
  while i < len(A) and exchange:
    exchange = False   # 若某一趟没有发生交换，则跳出循环
    for j in range(len(A)-1, i, -1):
      if A[j] < A[j-1]:
        A[j], A[j-1] = A[j-1], A[j]
        exchange = True
    i += 1
  return A
  
alist = [6, 5, 3, 1, 8, 7, 2, 4]
print(BubbleSort_Optimize(alist))
