# 习题 15.4-3：设计 LCS_Length 的带备忘的版本，运行时间为 O(mn)

def LCS_Length_Memo(X, Y):
  m = len(X)
  n = len(Y)
  c = [[float("-inf")] * (n+1) for i in range(m+1)]
  
  for i in range(0, m+1):
    c[i][0] = 0
  for j in range(0, n+1):
    c[0][j] = 0
    
  return LCS_Length_Memo_Aux(X, Y, c, m, n)

def LCS_Length_Memo_Aux(X, Y, c, i, j):
  if c[i][j] >= 0:
    return c[i][j]
  
  for l in range(1, i+1):
    for k in range(1, j+1):
      if X[l-1] == Y[k-1]:
        c[l][k] = LCS_Length_Memo_Aux(X, Y, c, l-1, k-1) + 1
      else:
        c[l][k] = max(LCS_Length_Memo_Aux(X, Y, c, l, k-1), LCS_Length_Memo_Aux(X, Y, c, l-1, k))
  
  return c[i][j]


 X = ["A", "B", "C", "B", "D", "A", "B"]
 Y = ["B", "D", "C", "A", "B", "A"]
 print(LCS_Length_Memo(X, Y))   # 答案：BCBA/BCBA，4
