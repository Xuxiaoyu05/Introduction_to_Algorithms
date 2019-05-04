# 习题 15.1-3：我们对钢条切割问题进行一点修改，除了切割下的钢条段具有不同价格 pi 外，每次切割还要付出固定的成本 c。这样，切割方案的收益就等于钢条段的
#              价格之和减去切割的成本。设计一个动态规划算法解决修改后的钢条切割问题。


def Cut_Steel_DP_Bottom_Up(p, n)
  r = [float("-inf")] * (n+1)
  return Cut_Steel_DP_Bottom_Up_Aux(p, n, r)

def Cut_Steel_DP_Bottom_Up_Aux(p, n, r):
  if r[n] >= 0:
    return r[n]
  
  if n == 0:
    q = 0
  else:
    for j in range(1, n+1):
      q = float("-inf")
      for i in range(1, j+1):
        q = max(q, p[i] + r[j-i])
        c = 
    
    r[j] = q
  
  return q



p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 9
c = 1.5
