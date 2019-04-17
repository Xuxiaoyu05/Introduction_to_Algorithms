# 最大子数组的暴力求解法，时间复杂度为θ(n^2)

def Max_Subarray(A):
  left = 0
  right = 0
  max_sum = float("-inf")
  
  for i in range(0, len(A)):
    sum = 0
    for j in range(i, len(A)):
      sum += A[j]
      if sum > max_sum:
        max_sum = sum
        left = i
        right = j
        
  return left, right, max_sum
  
alist = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(Max_Subarray(alist))
