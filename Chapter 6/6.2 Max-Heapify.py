# Max-Heapify 目的：用于维护最大堆性质

# 输入：一个数组 A，一个下标 i，堆的大小 heapsize

# 实现过程：在调用Max-Heapify的时候，我们假定根结点为 Left(i) 和 Right(i) 的二叉树都是最大堆(先决条件)，但这时 A[i] 有可能小于其孩子，这样就违背了最大堆的性质。
#          Max-Heapify 通过让 A[i] 的值在最大堆中“逐级下降”，从而使得以下标 i 为根结点的子树重新遵循最大堆的性质。

# 时间复杂度分析：调整A[root],A[left(root)]和A[right(root)]的关系的时间代价为θ(1) + 在一棵以root的一个孩子为根结点的子树上运行Max_Heapify的时间代价（假设递归调用会发生）
#                因为每个孩子的子树大小至多为2n/3（最坏情况发生在树的最底层恰好半满的时候），递归式为T(n) <= T(2n/3) + θ(1) ==> T(n) = O(lgn)


# 即对于一棵树高为 h 的结点来说，Max-Heapify 的时间复杂度为O(h)
def Max_Heapify(A, root, heapsize):
  left = 2 * root + 1    # 因为Python中下标从0开始，所以此处应该是2i+1
  right = 2 * root + 2
  
  larger = root
  
  if left <= heapsize and A[left] > A[larger]:
    larger = left
  
  if right <= heapsize and A[right] > A[larger]:
    larger = right
  
  if larger != root:
    A[root], A[larger] = A[larger], A[root]
    Max_Heapify(A, larger, heapsize)
  
  return A

# 习题6.2-1
A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
heapsize = len(A) - 1
print(Max_Heapify(A, 2, heapsize))
