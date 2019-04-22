# 思考题6.3：在一个 m*n 的 Young 氏矩阵中，每一行的数据都是从左到右排序的，每一列的数据都是从上到下排序的。Young 式矩阵中也会存在一些值为+inf的数据项，
#           表示那些不存在的元素。因此，Young 氏矩阵可以用来存储 r <= mn个有限的数。

# 6.3(a)：画出一个包含元素为 <9, 16, 3, 2, 4, 8, 5, 14, 12>的 4*4 Young 氏矩阵
#         答：[[2, 3, 12, 14], [4, 8, 16, +inf], [5, 9, +inf, +inf], [+inf, +inf, +inf, +inf]]

# 6.3(b)：对于一个 m*n Young 氏矩阵 Y 来说，请证明：如果 Y[1, 1] = inf，则 Y 为空；如果 Y[m, n] < inf，则 Y 为满（即包含 mn 个元素）
#         答：Young 氏矩阵 Y 中 Y[1, 1] 是其中最小的元素，Y[m, n] 是其中最大的元素

# 6.3(c)：请给出一个在 m*n Young 氏矩阵上时间复杂度为 O(m+n) 的 Extract-Min 的算法实现。你的算法可以考虑使用一个递归过程。它可能把一个规模为 m*n 的 Young 氏矩阵
#         分解为 (m-1)*n 或者 m*(n-1) 的子问题（考虑使用Max-Heapify）。这里，定义 T(p) 用来表示 Extract-Min 在任一 m*n 的 Young 氏矩阵上的时间复杂度，
#         其中 p = m + n。给出并求解 T(p) 的递归表达式，其结果为 O(m+n)

# 6.3(d)：试说明如果在 O(m+n) 时间内，将一个新元素插入到一个未满的 m*n 的 Young 式矩阵中。

# 6.3(e)：在不用其它排序算法的情况下，试说明如何利用一个 n*n 的 Young 式矩阵 在 O(n^3) 时间内将 n^2 个数进行排序。

# 6.3(f)：设计一个时间复杂度 O(m+n) 的算法，它可以用来判断一个给定的数是否存储在 m*n 的 Young 式矩阵中。

def MainTain_Young(Y, i, j):
  smaller_i, smaller_j = i, j
  while i < m and Y[i+1][j] < Y[i][j]:
    Y[i][j], Y[i+1][j] = Y[i+1][j], Y[i][j]
    
  while j < n and Y[i][j+1] < 
  
  
  
  
def Extract-Min(Y):
  min = Y[0][0]
  Y[0][0] = float("+inf")
  Maintain_Young(Y, 0, 0)
  return min
