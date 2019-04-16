# 给定 n 个整数的集合 S 和另一个整数 x ，该算法能确定 S 中是否存在两个其和刚好为 x 的元素

# 方法3：使用散列表，时间复杂度 θ(n)，空间复杂度 θ(n)

def twoSum_III(S, x):
  hash_table = {}
  
  for i, num in enumerate(S):
    if (x-num) in hash_table:
      return [hash_table[x-num], i]   # 返回这两个元素在数组中的位置
    else:
      hash_table[num] = i
  return False
  

alist = [6, 5, 3, 1, 8, 7, 2, 4]
x = 8
print(twoSum_III(alist, x))
