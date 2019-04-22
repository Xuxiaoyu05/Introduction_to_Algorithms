# 思考题7.2：(针对相同元素值的快速排序) 在随机化快速排序的分析中，我们假设所有元素是互异的。在本题中，我们将探究当假设不成立时会出现什么情况。

# 7.2(a)：如果所有输入元素的值都相同，那么随机化快速排序的运行时间会是多少？
#         答：θ(n^2)，因为每次都会产生 n-1 和 0 的划分

# 7.2(b)：Partition 过程返回一个数组下标 q, 使得 A[p...q-1] 中的每个元素都小于 A[q]，而 A[q+1...r] 中的每个元素都大于 A[q]。修改 Partition 代码来
          构造一个新的 Partition'(A, p, r)，它排列 A[p...r] 的元素，返回值是两个数组下标 q 和 t，其中 p <= q <= t <= r，且有
          (1) A[q...t] 中的所有元素都相等
          (2) A[p...q-1] 中的每个元素都小于 A[q]
          (3) A[t+1...r] 中的每个元素都大于 A[q]
          与 Partition 类似，新构造的 Partition' 的时间复杂度是 θ(r - p)
          
# 7.2(c)：将 Randomized_QuickSort 过程改为调用 Partition'，并重新命名为 Randomized_QuickSort'。修改 QuickSort 的代码构造一个新的 QuickSort'(A, p, r)，
          它调用 Randomized_QuickSort'，并且只有分区内的元素互不相同的时候才做递归调用。
          
# 7.2(d)：在 QuickSort' 中，应该如何改变 7.4节 中的分析方法，从而避免所有元素都是互异的这一假设。


def Partition_New(A, p, r):
  pivot = A[p]
  i = p
  q = p
  t = p
  
  for j in range(p+1, r+1):
    if A[j] = pivot:
      t += 1
    elif A[j] < pivor:
      q += 1
      
