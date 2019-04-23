# 在一个由 n 个元素组成的集合中，第 i 个顺序统计量是该集合中第 i 小的元素。如：
# (1) 最小值是第 1 个顺序统计量；
# (2) 最大值是第 n 个顺序统计量；
# (3) 中位数：当 n 为奇数时，中位数是唯一的，位于 i = (n+1)/2 处，当 n 为偶数时，存在两个中位数，分别位于 i = n/2 和 i = n/2 + 1 处。
#             因此，中位数总是出现在 i = floor((n+1)/2) [下中位数]处 和 i = ceil((n+1)/2) [上中位数]处。

# 目的：从一个由 n 个元素构成的集合中选择第 i 个顺序统计量

# 对于确定最小值/最大值问题，其下界就是 n - 1 次比较，即为了确定最小值/最大值，必须要做 n - 1 次比较。

# 寻找最小值
# 需要进行 n - 1次比较，时间复杂度为 θ(n) 
def FindMinimum(A):
  min = A[0]
  for i in range(1, len(A)):
    if min > A[i]:
      min = A[i]
  return min

# 寻找最大值
# 需要进行 n - 1次比较，时间复杂度为 θ(n) 
def FindMaximum(A):
  max = A[0]
  for i in range(1, len(A)):
    if max < A[i]:
      max = A[i]
  return max
  
 # 同时找到最小值和最大值
 # 普通解法：分别独立的找出最小值和最大值，共需 2(n-1) = 2n - 2 次比较
 # 优化解法：对输入元素成对处理：首先把一对输入元素相互进行比较，然后把较小的与当前最小值比较，把较大的与当前最大值比较。这样，对每两个元素共需3次比较。
 #          最大值/最小值初始值取决于 n 的奇偶性：若 n 为奇数，最小值/最大值的初始值都设为第一个元素的值，然后成对的处理余下的元素；
 #                                             如果 n 为偶数，就对前两个元素做一次比较，以决定最小值和最大值的初值，然后成对的处理余下元素。
 #          总的比较次数：若 n 为奇数，总共需要进行 3 * floor(n/2) 次比较；若 n 为偶数，总共需要进行 3(n-2)/2 + 1 = 3n/2 - 1。
 #                       因此，无论哪一种情况，总的比较次数至多是 3 * floor(n/2) 次。
 
 def FindMaxAndMin(A):
  if len(A) % 2 != 0: # 元素个数为奇数
    min, max = A[0], A[0]
    for j in range(1, len(A)-1, 2):
      if A[j] > A[j+1]:
        if A[j] > max:
          max = A[j]
        if A[j+1] < min:
          min = A[j+1]
      else:
        if A[j+1] > max:
          max = A[j+1]
        if A[j] < min:
          min = A[j]
  else:  # 元素个数为偶数
    if A[1] > A[0]:
      min, max = A[0], A[1]
    else:
      min, max = A[1], A[0]
    
    for j in range(2, len(A)-1, 2):
      if A[j] > A[j+1]:
        if A[j] > max:
          max = A[j]
        if A[j+1] < min:
          min = A[j+1]
      else:
        if A[j+1] > max:
          max = A[j+1]
        if A[j] < min:
          min = A[j]
          
  return min, max

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(FindMinimum(alist))
print(FindMaximum(alist))
print(FindMaxAndMin(alist))
