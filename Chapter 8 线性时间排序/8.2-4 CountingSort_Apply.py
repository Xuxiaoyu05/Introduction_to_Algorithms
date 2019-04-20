# 习题8.2-4：设计一个算法，它能够对任何给定的介于 0 到 k 之间的 n 个整数先进行预处理，然后在 O(1) 时间内回答输入的 n 个整数中有多少个落在区间[a...b]内，
#            你设计的算法的预处理时间应为 θ(n+k)


def CountingSort_Apply(A, k, a, b):
  B = [0] * len(A)
  C = [0] * (k+1)
  
  # 初始化
  for i in range(0, k+1):
    C[i] = 0
  
  # 统计 A 中每个元素的个数
  for j in range(0, len(A)):
    C[A[j]] = C[A[j]] + 1
  
  # C[i] 中存储小于等于 i 的元素的个数
  for i in range(1, k+1):
    C[i] = C[i] + C[i-1]
  
  if a == 0:
    return C[b]
  
  return C[b] - C[a-1]
  
if __name__ == "__main__":
  alist = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
  print(CountingSort_Apply(alist, 6, 1, 5))
