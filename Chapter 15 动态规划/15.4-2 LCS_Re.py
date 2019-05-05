# 习题 15.4-1：设计伪代码，利用完整的表 c 及原始序列 X = <x1, x2, ..., xm> 和 Y = <y1, y2, ..., yn> 来重构 LCS，要求运行时间为 O(m+n)，不能
#              使用表 b。

# 时间复杂度 θ(mn)
def LCS_Length(X, Y):
  m = len(X)
  n = len(Y)
  
  c = [[0] * (n+1) for i in range(m+1)]
  
  for i in range(1, m+1):
    for j in range(1, n+1):
      if X[i-1] == Y[j-1]:
        c[i][j] = c[i-1][j-1] + 1
      else:
        c[i][j] = max(c[i-1][j], c[i][j-1])
  
  Print_LCS_Re(c, X, m, n)
  
  return c[m][n]

# 时间复杂度 O(m+n)
def Print_LCS_Re(c, X, i, j):
  if i == 0 or j == 0:
    return
  
  if c[i][j] == c[i-1][j-1] + 1:
    Print_LCS_Re(c, X, i-1, j-1)
    print(X[i-1])
  else:
    if c[i-1][j] >= c[i][j-1]:
      Print_LCS_Re(c, X, i-1, j)
    else:
      Print_LCS_Re(c, X, i, j-1)
    

 X = ["A", "B", "C", "B", "D", "A", "B"]
 Y = ["B", "D", "C", "A", "B", "A"]
 print(LCS_Length(X, Y))   # 答案：BCAB，4
