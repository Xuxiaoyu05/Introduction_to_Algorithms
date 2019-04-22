# 思考题 7.4：(快速排序的栈深度) 7.1节中的 QuickSort 算法包含了两个对其自身的递归调用。在调用 Partition 后，QuickSort 分别递归调用了左边的子数组
#            和右边的子数组。事实上，QuickSort 中的第二个递归调用并不是必须的，我们可以用一个循环控制结构来代替它。这一技术称为尾递归。

#7.4(a)：证明：Tail_Recursive_QuickSort(A, 1, A.length) 能正确地对数组 A 进行排序。编译器通常使用栈来存储递归执行过程中的相关信息，包括每一次递归调用的参数等、
               最新调用的信息存在栈的顶部，而第一次调用的信息存在栈的底部。当一个过程被调用时，其相关信息被压入栈中；当它结束时，其信息则被弹出。因为我们
               假设数组参数使用指针来指示的，所以每次过程调用只需要 O(1) 的栈空间。栈深度是在一次计算中会用到的栈空间的最大值。
               
#7.4(b)：请描述一种场景，使得针对一个包含 n 个元素数组的 Tail_Recursive_QuickSort 的栈深度是 θ(n)

#7.4(c)：修改 Tail_Recursive_QuickSort 的代码，使其最坏情况下栈深度是 θ(lgn)，并且能够保持 O(nlgn) 的期望时间复杂度。

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

def Tail_Recursive_QuickSort(A, p, r):
  while p < r:
    q = Partition(A, p, r)
    Tail_Recursive_QuickSort(A, p, q-1)
    p = q + 1
