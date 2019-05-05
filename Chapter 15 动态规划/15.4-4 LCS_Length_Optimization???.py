# 习题 15.4-4：说明如何只使用表 c 中 2 * min(m, n) 个表项 及 O(1) 的额外空间来计算 LCS 的长度，然后说明如何只用 min(m, n) 个表项及 O(1) 的额外空间
#              完成相同的工作。

# 分析：此题目的是 LCS 在时空开销上的改进，因为在任何时候 LCS 只需要表 c 中的两行，当前正在计算的一行和前一行。如果只需计算 LCS 的长度，这一改进是有效的。
#       但是无法在 O(m+n) 时间内重构 LCS。

def LCS_Length_Optimization(X, Y):
  m = len(X)
  n = len(Y)
  
  c = [0] * (n+1)
  
  for i in range(1, m+1):
    for j in range(1, n+1):
      if X[i-1] == Y[j-1]:
        c[j] = c[j-1] + 1
      else:
        c[j] = c[j-1]
   
