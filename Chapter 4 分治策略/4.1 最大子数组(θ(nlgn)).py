# 分治法：（1）分解（2）递归（3）合并
           # 递归情况：当子问题足够大，需要递归求解时，称为递归情况
           # 基本情况：当子问题变得足够小，不再需要递归时，则说明递归已经“触底”，称为基本情况
           
           
# 问题：给定一个数组 A，寻找具有最大和的非空连续子数组，这样的连续子数组为最大子数组。

# 前提条件：（1）可能有多个子数组达到最大和；（2）只有当数组中包含负数时，最大子数组问题才有意义。如果所有数组元素都是非负的，整个数组的和肯定是最大的。

# 方法1：分治策略
# 问题分析：采用分治方法寻找子数组A[low...high]中的最大子数组，意味着我们要将子数组划分成两个规模尽量相等的子数组。然后求解两个子数组A[low...mid]和A[mid+1...hign]
#          A[low...high]的任何连续子数组所处的位置A[i...j]所处的位置必然是以下三种情况之一，因此A的一个最大子数组也必然是这三种情况之一：
#         （1）完全位于子数组A[low...mid]中，因此low <= i <= j <= mid
#         （2）完全位于子数组A[mid+1...high]中，因此mid < i <= j <= high
#         （3）跨越了中点，因此low <= i <= mid <j <= high
#          如果最大子数组属于情况(1)或(2)，可以递归的求解A[low...mid]，A[mid+1...high]的最大子数组，这两个是原问题的规模更小的子问题；
#          若是情况(3)，则需要寻找跨越中点的最大子数组，然后在三种情况中选择和最大者。


# 求跨越中点的最大子数组可以在线性时间内求解，此问题并非原问题规模更小的实例，因为它加入了限制-求出的子数组必须跨过中点。
# 因此，任何跨越中点的子数组都由两个子数组A[i...mid]和A[mid+1...j]组成，其中low <= i <= mid <j <= high，因此只需找出形如A[i...mid]和A[mid+1...j]的最大子数组合并即可
# 子过程 Find_Max_Crossing_Subarray：输入：数组A，下标low, mid, high；输出：一个下标元组划定跨越中点的最大子数组的边界，并返回最大子数组的和

# 时间复杂度 θ(n), n = high - low + 1
def Find_Max_Crossing_Subarray(A, low, mid, high):
    left_sum = float("-inf")
    sum = 0
    for i in range(mid, low-1, -1):
      sum += A[i]        # 保存A[i...mid]中所有值的和
      if sum > left_sum:
        left_sum = sum   # 保存目前为止找到的最大和
        max_left = i     

    right_sum = float("-inf")
    sum = 0
    for j in range(mid+1, high+1):
      sum += A[j]
      if sum > right_sum:
        right_sum = sum
        max_right = j

    return max_left, max_right, left_sum + right_sum
  
 
 # 求解最大子数组问题的分治算法
 # 输出：数组A，下标low和high；输出：i, j, 最大子数组A[i...j]的和
 # 时间复杂度：θ(nlgn)
 
 def Find_Max_Subarray(A, low, high):
    if high == low:   # 基本情况，数组中只有一个元素
      return low, high, A[low]
    else:
      mid = (low + high)//2
      left_low, left_high, left_sum = Find_Max_Subarray(A, low, mid)  # 左子数组
      right_low, right_high, right_sum = Find_Max_Subarray(A, mid+1, high)  # 右子数组
      cross_low, cross_high, cross_sum = Find_Max_Crossing_Subarray(A, low, mid, high)  # 求跨越中点的最大子数组
      
      # 合并
      if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
      elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
      else:
        return cross_low, cross_high, cross_sum

alist = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(Find_Max_Subarray(alist, 0, len(alist)-1))
