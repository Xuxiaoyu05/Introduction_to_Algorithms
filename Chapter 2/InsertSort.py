# 插入排序

# 特点：（1）适用于少量元素的排序（2）原址排序（即最多只有常数个数字存储在数组外面）（3）联想：从桌面上拿扑克牌并放在手中牌正确的位置

# 非降序排列
def InsertSort(A):
  for i in range(1, len(A)):
    valToInsert = A[i]
    while i >= 1 and A[i-1] > valToInsert:
      A[i] = A[i-1]
      i -= 1
    A[i] = valToInsert
    
  return A


# 非升序排列(习题2.1-2)
def InsertSort_II(A):
  for i in range(1, len(A)):
    valToInsert = A[i]
    while i >= 1 and A[i-1] < valToInsert:
      A[i] = A[i-1]
      i -= 1
    A[i] = valToInsert
    
  return A


nums = [4, 5, 3, 8, 2, 9, 6, 7, 1]
print(InsertSort(nums))
print(InsertSort_II(nums))
