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


# 保持 Young 式矩阵的性质：将 A[i, j] 与其邻居（右边 A[i][j+1]，下边 A[i+1][j]）比较，并且将其与最小值交换。
# 当 A[i, j] 小于其周围邻居时，程序终止。
def MainTain_Young(Y, i, j, m, n):
  smaller_i, smaller_j = i, j
  
  if i < m and Y[i+1][j] < Y[i][j]:  # 下边
    smaller_i, smaller_j = i+1, j
    
  if j < n and Y[i][j+1] < Y[smaller_i][smaller_j]:  # 右边
    smaller_i, smaller_j = i, j+1
  
  if smaller_i != i or smaller_j != j:
    Y[i][j], Y[smaller_i][smaller_j] = Y[smaller_i][smaller_j], Y[i][j]
    MainTain_Young(Y, smaller_i, smaller_j, m, n)
  

# 去掉并返回 Young 式矩阵中的最小值，时间复杂度 O(m + n)
def Young_Extract_Min(Y, m, n):
  min = Y[0][0]
  Y[0][0] = float("+inf")
  MainTain_Young(Y, 0, 0, m, n)
  #   print(Y)    # 结果应为[[3, 8, 12, 14], [4, 9, 16, inf], [5, inf, inf, inf], [inf, inf, inf, inf]]
  return min


def Maintain_Young_II(Y, i, j, m, n):
  position_i, position_j = i, j
  
  if i > 0 and Y[i-1][j] > Y[i][j]:  # 上边
    position_i, position_j = i-1, j
  if j > 0 and Y[i][j-1] > Y[position_i][position_j]:  # 左边
    position_i, position_j = i, j-1
  
  if position_i != i or position_j != j:
    Y[i][j], Y[position_i][position_j] = Y[position_i][position_j], Y[i][j]
    Maintain_Young_II(Y, position_i, position_j, m, n)
    
    
def Young_Insert(Y, key, m, n):
  if Y[m][n] != float("+inf"):
    return "Young Matrix is full."
  
  Y[m][n] = key
  Maintain_Young_II(Y, m, n, m, n)
  return Y
  
matrix = [[2, 3, 12, 14], [4, 8, 16, float("+inf")], [5, 9, float("+inf"), float("+inf")],
          [float("+inf"), float("+inf"), float("+inf"), float("+inf")]]

m = len(matrix)-1
n = len(matrix[0])-1
# print(Young_Extract_Min(matrix, m, n))
print(Young_Insert(matrix, 6, m, n))










