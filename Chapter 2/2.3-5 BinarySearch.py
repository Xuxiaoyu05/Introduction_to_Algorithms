# 在线性查找问题中，如果序列 A 已经排好序，就可以用二分查找算法来查找对应的元素，可以将序列剩余部分的规模减半。

# 时间复杂度：最坏情况: θ(lgn)

def BinarySearch(A, v):
  left = 0
  right = len(A) - 1
  
  while left <= right:
    mid = (left + right)//2
    if v == A[mid]:
      return mid
    elif v > A[mid]:
      left = mid + 1
    else:
      right = mid - 1
  return -1
  
  
alist = [1,2,3,5,7,8,9]
v = 5
print(BinarySearch(alist, v))
