# 习题9.3-5：假设你已经有了一个最坏情况下是线性时间的用于求解中位数的“黑箱”子程序。设计一个能在线性时间内解决任意顺序统计量的选择问题算法。

def Select(array, n):
  mid = median(array)
  smaller = [num for num in array if item < mid]
  larger = [num for num in array if item > mid]
  if len(smaller) == n:
    return mid
  elif len(smaller) > n:
    return Select(smaller, n)
  else:
    return Select(larger, n - len(smaller) - 1)
    
    
def Median(array):
  def median_index(n):
    if n%2 != 0:
      return n//2
    else:
      return n//2 - 1
  
  def partition(array, element):
    i = 0
    for j in range(len(array)-1):
      if array[j] == element:
        array[j], array[-1] = array[-1], arraty[j]
      
      if array[j] < element:
        array[i], array[j] = array[j], array[i]
        i += 1
      
      array[i], array[-1] = array[-1], array[i]
      
      return i
   
   def select(array, n):
    if len(array) <= 1:
      return array[0]
    
    medians = []
    
    for i in range(0, len(array), 5):
      group = sorted(array[i:i+5])
      array[i:i+5] = group
      median = group[median_index(len(group)]
      medians.append(median)
    
    pivot = select(medians, median_index(len(medians)))
    index = partition(array, pivot)
    
    if n == index:
      return array[index]
    elif n < index:
      return select(array[:index], n)
    else:
      return select(array[index+1:], n - index - 1)
    
    return select(array[:], median_index(len(array)))
        
  
