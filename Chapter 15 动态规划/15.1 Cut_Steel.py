# 钢条切割

# 问题：给定一段长度为 n 英寸的钢条和一个价格表 pi(i = 1, 2, ..., n)，求切割钢条方案，使得销售收益 rn 最大。注意：如果长度为 n 英寸的钢条的价格 pn 足够
#       大，最优解可能就是完全不需要切割。长度为 n 英寸的钢条共有 2^(n-1) 种不同的切割方案。

# 分析：对于 rn(n >= 1)，我们可以用更短的钢条的最优切割收益来描述它：rn = max(pn, r1+rn-1, r2+rn-2, ..., rn-1+r1)
#      为了求解规模为 n 的原问题，我们先求解形式完全一样，但规模更小的子问题。我们通过组合两个相关子问题的最优解，并在所有可能的两段切割方案中选取组合收益
#      最大者，构成原问题的最优解。我们称钢条切割问题满足“最优子结构”性质：问题的最优解由相关子问题的最优解组合而成，而这些子问题可以独立求解。


# 自顶向下递归求解，时间复杂度 O(2^n)，由于反复求解相同的子问题，所以效率很低。
def Cut_Steel_Recursive(p, n):
  if n == 0:
    return 0
    
  q = float("-inf")
  
  for i in range(1, n+1):
    q = max(q, p[i] + Cut_Steel_Recursive(p, n-i))
  
  return q


# 使用动态规划方法求解最优钢条切割问题
# 基本思想：动态规划方法仔细安排求解顺序，对每个子问题只求解一次，并将结果保存下来。如果随后再次需要此子问题的解，只需查找保存的结果，而无需重新计算。
#          因此，动态规划方法是付出额外的内存空间来节省计算时间，是典型的时空权衡例子。
# 动态规划有两种等价的实现方法：
#（1）带备忘的自顶向下法：仍按自然的递归形式来编写过程，但过程会保存每个子问题的解（通常保存在一个数组或散列表中）。当需要一个子问题的解时，过程首先检查
#                       是否已保存过此解，如果是，则直接返回保存的值，否则，按通常方式计算这个子问题。
#（2）自底向上法：将子问题按规模排序，按从小至大的顺序进行求解。当求解某个子问题时，它所依赖的那些更小的子问题都已求解完毕，结果已经保存。每个子问题只需
#               求解一次，当我们求解它（也是第一次遇到它）时，它的所有前提子问题都已经求解完成。
# 两种方法的区别：两种方法得到的算法具有相同的渐进运行时间，仅有的差异是在某些特殊情况下，自顶向下方法并未真正递归的考察所有可能的子问题。由于没有频繁的
#               递归函数调用的开销，自底向上方法的时间复杂性函数通常具有更小的系数。

# 动态规划 之 带备忘的自顶向下法，时间复杂度 θ(n^2)
def DP_Cut_Steel_Memo(p, n):
  r = [float("-inf")] * (n+1)   # 定义新数组 r, 并将其初始化为 -inf
  return DP_Cut_Steel_Memo_AUX(p, n, r)  

def DP_Cut_Steel_Memo_AUX(p, n, r):
  if r[n] >= 0:
    return r[n]
  
  if n == 0:
    q = 0
  else:
    q = float("-inf")
    for i in range(1, n+1):
      q = max(q, p[i] + DP_Cut_Steel_Memo_AUX(p, n-i, r))
  
  r[n] = q
  
  return q


# 动态规划 之 自底向上法，时间复杂度 θ(n^2)
def DP_Cut_Steel_Bottom_UP(p, n):
  r = [float("-inf")] * (n+1)   # 定义新数组 r, 并将其初始化为 -inf
  r[0] = 0
  
  for j in range(1, n+1):
    q = float("-inf")
    for i in range(1, j+1):
      q = max(q, p[i] + r[j-i])
    r[j] = q
  
  return r[n]

# 动态规划 之 自底向上法的扩展版本，返回最大收益值 和 最优解对应的第一段钢条的切割长度 sj
def DP_Cut_Steel_Bottom_UP_Extended(p, n):
  r = [float("-inf")] * (n+1) 
  s = [0] * (n+1)
  r[0] = 0
  
  for j in range(1, n+1):
    q = float("-inf")
    for i in range(1, j+1):
      if q < p[i] + r[j-i]:
        q = p[i] + r[j-i]
        s[j] = i
    r[j] = q
  
  return r, s

def Print_Cut_Steel_Solution(p, n):
  (r, s) = DP_Cut_Steel_Bottom_UP_Extended(p, n)
  while n > 0:
    print(s[n])
    n = n - s[n]


p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 9
print(Cut_Steel_Recursive(p, n))  # 结果应为 25
print(DP_Cut_Steel_Memo(p, n))
print(DP_Cut_Steel_Bottom_UP(p, n))
Print_Cut_Steel_Solution(p, n)
