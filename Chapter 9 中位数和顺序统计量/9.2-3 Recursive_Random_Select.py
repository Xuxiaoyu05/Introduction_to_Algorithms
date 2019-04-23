# 习题 9.2-3：给出 Random_Select 的一个基于循环的版本


import random

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
  
def Random_Partition(A, p, r):
  i = random.randint(p, r)
  A[p], A[i] = A[i], A[p]
  return Partition(A, p, r)
  
def Recursive_Random_Select(A, p, r, i):  
  while p < r:  # 循环条件，最初我以为是 k != i，这种想法是错的
    q = Random_Partition(A, p, r)
    k = q - p + 1
    if k == i:
      return A[q]
    elif k > i:
      r = q - 1
    else:
      p = q + 1
      i -= k
   
   return A[p]

alist = []
for i in range(0, 15):
  alist.append(random.randint(1, 20))
  
print(alist)
print(Recursive_Random_Select(alist, 0, len(alist)-1, 5))
