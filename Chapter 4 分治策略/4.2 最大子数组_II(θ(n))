# 求解最大子数组问题存在一个线性时间的算法(采用贪心策略)，时间复杂度为θ(n)

def Max_SubArray(A):
  temp = 0
  max_val = 0
  
  for i in range(0, len(A)):
    temp += A[i]
    max_val = max(max_val, temp)
    temp = max(temp, 0)
  return max_val
  
alist = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(Max_SubArray(alist))
