# 习题2.1-4

# Consider the problem of adding two n-bit binary integers, stored in two n-element arrays A and B. 
# The sum of the two integers should be stored in binary form in an (n+1)-element array C. 

# 两个 n 位二进制整数相加，这两个整数分别存储在两个 n 元数组 A 和 B 中，这两个整数的和应按二进制形式存储在一个(n+1)元数组C中

# 分析：A和B中每个位置的元素都为0或1，影响最小的元素排在最前或最后

# 影响最小的元素排在前
def AddTwoBinaryIntergers(A, B):
  n = len(A)
  C = [-1] * (n + 1)
  carry = 0
  for i in range(0, n):
    C[i] = (A[i] + B[i] + carry) % 2
    carry = (A[i] + B[i] + carry) // 2
  if carry == 1:
    C[n] = 1
  else:
    C[n] = 0
    
  return C
  

# 影响最小的元素排在后
def AddTwoBinaryIntergers_II(A, B):
  n = len(A)
  C = [-1] * (n + 1)
  carry = 0
  for i in range(n, 0, -1):
    C[i] = (A[i-1] + B[i-1] + carry) % 2
    carry = (A[i-1] + B[i-1] + carry) // 2
  if carry == 1:
    C[0] = 1
  else:
    C[0] = 0
  
  return C
 
A = [0,1,0,1,1,1,0,1]
B = [0,1,1,0,1,1,0,1]
print(AddTwoBinaryIntergers(A, B))
print(AddTwoBinaryIntergers_II(A, B))
