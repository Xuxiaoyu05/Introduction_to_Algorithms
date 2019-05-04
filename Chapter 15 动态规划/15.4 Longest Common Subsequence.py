# 最长公共子序列（LCS）

# 最长公共子序列问题：给定两个序列 X = <x1, x2, ..., xm> 和 Y = <y1, y2, ..., yn>，求 X 和 Y 长度最长的公共子序列。(子序列无需连续)

# 分析：如果用暴力搜索法求解 LCS 问题，需要穷举 X 的所有子序列，对每个子序列检查它是否也是 Y 的子序列，记录找到的最长子序列。X 的每个子序列对应 X 的下标
#       集合{1, 2, ..., m} 的一个子集，所以 X 有 2^m 个子序列，因此暴力方法的运行时间为指数阶。
#       因为 LCS 问题具有最优子结构性质，所以考虑用动态规划方法求解。

# 步骤1：刻画最长公共子序列的特征
# 定理 15.1：(LCS 的最优子结构) 令 X = <x1, x2, ..., xm> 和 Y = <y1, y2, ..., yn> 为两个序列，Z = <z1, z2, ..., zk> 为 X 和 Y 的任意 LCS。
#           （1）如果 xm = yn，则 Zk = xm = yn 且 Z(k-1) 是 X(m-1) 和 Y(n-1) 的一个 LCS；
#           （2）如果 xm != yn，那么 Zk != xm 意味着 Z 是 X(m-1) 和 Y 的一个 LCS；
#           （3）如果 xm != yn，那么 Zk != yn 意味着 Z 是 X 和 Y(n-1) 的一个 LCS。
# 由上述定理可以看出，两个序列的 LCS 包含两个序列的前缀的 LCS。因此，LCS 问题具有最优子结构性质。

# 步骤2：一个递归解
# 由定理 15 可得，在求 X = <x1, x2, ..., xm> 和 Y = <y1, y2, ..., yn> 的一个 LCS 时，需要求解一个或两个子问题。如果 xm = yn，我们应该求解 X(m-1) 和
# Y(n-1) 的一个 LCS，将 xm = yn 追加到这个 LCS 的末尾，就得到 X 和 Y 的一个 LCS。如果 xm != yn，必须求解两个子问题：求 X(m-1) 和 Y 的一个 LCS 与 X
# 和 Y(n-1) 的一个 LCS。两个 LCS 中较长者即为 X 和 Y 的一个 LCS。可以看出 LCS 问题的重叠子问题性质。
# 所以，最长公共子序列的状态转移方程为，其中 c[i, j] 表示 Xi 和 Yj 的 LCS 的长度。
# c[i, j] = (1) 若 i = 0 或 j = 0， c[i, j] = 0 
#           (2) 若 i, j > 0 且 xi = yj，c[i, j] = c[i-1, j-1] + 1
#           (3) 若 i, j > 0 且 xi != yj，c[i, j] = max(c[i, j-1], c[i-1, j])

# 步骤3：计算 LCS 的长度
# 由于 LCS 只有 θ(mn) 个不同的子问题，所以可以用动态规划方法自底向上地计算。
# 输入：两个序列  X = <x1, x2, ..., xm> 和 Y = <y1, y2, ..., yn> 
# 它将 c[i, j] 的值保存在 c[0...m, 0...n] 中，并按 “行主次序” 计算表项（从左至右计算 c 的第一行，然后计算第二行，以此类推）。
# 过程还维护一个表 b[1...m, 1...n] 帮助构造最优解。b[i, j] 指向的表项对应计算 c[i, j] 时 所选择的的子问题最优解。过程返回表 b 和 表 c。
# c[m, n] 保存了 X 和 Y 的 LCS 的长度。

# 计算 LCS 的长度，时间复杂度 θ(mn)
def LCS_Length(X, Y):
  m = len(X)
  n = len(Y)
  
  c = [[0] * (n+1) for i in range(m+1)]   # 定义矩阵 C 为 (m+1) * (n+1) 的二维矩阵，并全部初始化为 0
  b = [[0] * (n+1) for i in range(m+1)]        # 定义矩阵 B 为 m * n 的二维矩阵来存储子问题的最优解
  
  # 当 i = 0 或 j = 0 时，c[i, j] = 0，由于初始化 c 矩阵时已经将所有值设置为 0，所以这一部分省略
  # for i in range(0, n+1):
  #   C[0][i] = 0
  # for j in range(0, m+1):
  #   C[m][0] = 0
  
  
  # 重点：行主次序
  for i in range(1, m+1):
    for j in range(1, n+1):
      if X[i-1] == Y[j-1]:  # 注意此处是 X[i-1] == Y[j-1]，因为 Python 下标是从 0 开始
        c[i][j] = c[i-1][j-1] + 1
        b[i][j] = "ok"
      else:
        # c[i][j] = max(c[i-1][j], c[i][j-1])
        if c[i-1][j] >= c[i][j-1]:
          c[i][j] = c[i-1][j]
          b[i][j] = "up"
        else:
          c[i][j] = c[i][j-1]
          b[i][j] = "left"
          
  Print_LCS(b, X, m, n)  # 输出 LCS
  return c[m][n]

# 步骤4：构造 LCS
# 时间复杂度 O(m+n)
def Print_LCS(b, X, i, j):
  if i == 0 or j == 0:
    return
  if b[i][j] == "ok":
    Print_LCS(b, X, i-1, j-1)
    print(X[i-1])
  elif b[i][j] == "up":
    Print_LCS(b, X, i-1, j)
  else:
    Print_LCS(b, X, i, j-1)
  
 X = ["A", "B", "C", "B", "D", "A", "B"]
 Y = ["B", "D", "C", "A", "B", "A"]
 print(LCS_Length(X, Y))   # 答案：BCBA，4
