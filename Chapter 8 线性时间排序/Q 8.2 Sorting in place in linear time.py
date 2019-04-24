# 思考题8.2：（线性时间原址排序）假设有一个包含 n 个待排序数据记录的数组，且每条记录的关键字的值为 0 或 1。对这样一组记录进行排序的算法可能具备如下三种
#            特性中的一部分。
#           （1）算法的时间代价是 O(n)
#           （2）算法是稳定的
#           （3）算法是原址排序，除了输入数组之外，算法只需要固定的额外存储空间

#8.2(a)：给出一个满足上述条件 1 和条件 2 的算法。
#8.2(b)：给出一个满足上述条件 1 和条件 3 的算法。
#8.2(c)：给出一个满足上述条件 2 和条件 3 的算法。

#8.2(d)：你设计的算法 (a) ~ (c) 中的任一个是否可以用于 RadixSort 的第 2 行作为基础排序方法，从而使 RadixSort 在排序有 b 位关键字的 n 条记录时的代价
#        是 O(bn)？如果可以，请解释应如何处理；如果不行，请说明原因。
#        答：只有 (a) 可以用于 RadixSort；因为 (b) 不是稳定排序，(c) 若用于 RadixSort，则总的时间复杂度为 O(bn^2)

#8.2(e)：假设有 n 条记录，其中所有关键字的值都在 1 到 k 的区间内。你应该如何修改计数排序，使得它可以在 O(n+k) 时间内完成对 n 条记录的原址排序。除输入
#        数组外，你可以使用 O(k) 大小的额外存储空间。你给出的算法是稳定的吗？（提示：当 k = 3 时，你应该如何做？）
#        答：多用一个 k + 1 大小的数组来存储未变化的 C 中的值

import random

#(a) 满足条件 1 和条件 2：算法的时间代价是 O(n) 且是稳定的
def Stable_Linear_Sort(A): # 计数排序的修改版
  zeros, ones = 0, 0
  copy = [0] * len(A)
  
  for i in range(0, len(A)):
    if A[i] == 0:
      ones += 1
  
  for j in range(0, len(A)):
    if A[j] == 0:
      copy[zeros] = A[j]
      zeros += 1
    else:
      copy[ones] = A[j]
      ones += 1
    
  return copy

#(b) 满足条件 1 和 3：算法的时间代价是 O(n) 且是原址排序
def Linear_InPlace_Sort(A): # Hoare划分的修改版
  i = 0
  j = len(A) - 1
  
  while i != j:
    while A[j] == 1 and i < j:
      j -= 1
    while A[i] == 0 and i < j:
      i += 1
    
    if i < j:
      A[i], A[j] = A[j], A[i]
  
  return A
      
#(c) 满足条件 2 和 3：算法是稳定的原址排序
def Stable_InPlace_Sort(A):  # 插入排序的修改版
  for i in range(1, len(A)):
    valToInsert = A[i]
    while i > 0 and A[i-1] > valToInsert:
      A[i] = A[i-1]
      i -= 1
    A[i] = valToInsert
    
  return A

# alist = []
# for i in range(0, 15):
#   alist.append(random.randint(0,1))
# print(alist)
# print(Stable_Linear_Sort(alist))
# print(Linear_InPlace_Sort(alist))
# print(Stable_InPlace_Sort(alist))

#(e) 时间复杂度 O(n+k)，空间复杂度 O(k)，算法是原址排序
def InPlace_CountingSort(A, k):
  C = [0] * (k+1)
  pos = [0] * (k+1)
  
  for i in range(0, len(A)):
    C[A[i]] += 1
  
  for j in range(2, k+1):
    C[j] += C[j-1]
  
  for i in range(0, k+1):
    pos[i] = C[i]
    
  i = 0
  while i < len(A):
    key = A[i]  # 此处必须用 key 来存储 A[i] 的值，因为当 A[i], A[C[key]-1] = A[C[key]-1], A[i] 交换时，若后面是 C[A[i]]-1，其中A[i]的值就已经变化了
    placed = (pos[key-1] <= i) and (i < pos[key])
    
    if placed: # 如果 A[i] 被放置在正确位置上，则 i += 1
      i += 1 
    else: # 将 A[i] 放到其正确位置上
      A[i], A[C[key]-1] = A[C[key]-1], A[i]
      C[key] -= 1
      
  return A
         
alist = []
for i in range(0, 10):
  alist.append(random.randint(1, 10))  # 值为 1-k
print(alist)
print(InPlace_CountingSort(alist, 10))
