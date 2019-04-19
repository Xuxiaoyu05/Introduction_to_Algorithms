# 思考题6.2：d 叉堆与二叉堆很类似，但（一个可能的例外）是其中的每个非叶结点有 d 个孩子，而不是仅仅两个。
# 6.2(a)：如何在一个数组中表示一个 d 叉堆。 答：在Python中，Parent 下标为(i-1)//2，Children下标为 3*i + c（其中 1 <= c <= d） 
# 6.2(b)：包含 n 个元素的 d 叉堆的高度是多少？请用 n 和 d 表示。  答：以 d 为底 n 的对数 logd(n) 
# 6.2(c)：请给出 Extract-Max 在 d 叉最大堆上的一个有效实现，并用 d 和 n 表示出它的时间复杂度。
# 6.2(d)：给出 Insert 在 d 叉最大堆上的一个有效实现，并用 d 和 n 表示出它的时间复杂度。
# 6.2(e)：给出 Increase-Key(A, i, k) 的一个有效实现，当 k < A[i] 时，它会触发一个错误，否则执行 A[i] = k，并更新相应的 d 叉最大堆，
#         请用 d 和 n 表示出它的时间复杂度。


d = 3   # d 值可以自己定义

def Parent(i, d):
  return (i-1)//d

def Children(i, c, d):
  return d * i + c + 1  # 0 <= c < d

# 维护 d 叉堆性质，时间复杂度O(dlogd(n))
def D_Heap_Max_Heapify(A, root, heapsize):
  larger = root
  for c in range(0, d):
    if Children(root, c, d) <= heapsize and A[Children(root, c, d)] > A[larger]:
      larger = Children(root, c, d)
  
  if larger != root:
    A[root], A[larger] = A[larger], A[root]
    D_Heap_Max_Heapify(A, larger, heapsize)

# 将传入数组构建为最大 d 叉堆, 时间复杂度O(n)
def Build_D_Heap(A):
  heapsize = len(A) - 1
  for i in range((heapsize-1)//d, -1, -1):
    D_Heap_Max_Heapify(A, i, heapsize)
  return A

# 去掉并返回 S 中的具有最大关键字的元素，时间复杂度O(dlogd(n))
def D_Heap_Extract_Max(A):
  if len(A) < 1:
    return
  max = A[0]
  heapsize = len(A) - 1
  A[0] = A[heapsize]
  heapsize -= 1
  D_Heap_Max_Heapify(A, 0, heapsize)
  return max

# 将元素 x 的关键字增加到 k（假设 k 的值不小于 x 的原关键字），时间复杂度O(logd(n))
def D_Heap_Increase_Key(A, i, key):
  if key < A[i]:
    return
  A[i] = key
  
  while i > 0 and A[Parent(i, d)] < A[i]:
    A[i], A[Parent(i, d)] = A[Parent(i, d)], A[i]
    i = Parent(i, d)
  return A

# 时间复杂度 O(logd(n))
def D_Heap_Insert(A, x):
  A.append(float("-inf"))
  heapsize = len(A) - 1
  D_Heap_Increase_Key(A, heapsize, x)
  return A
  
alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
D_Heap = Build_D_Heap(alist)  # 构建得到的最大 3 叉堆：[12, 7, 10, 11, 5, 6, 2, 8, 9, 3, 1, 4]
print(D_Heap)
# print(D_Heap_Extract_Max(D_Heap))
# print(D_Heap_Increase_Key(D_Heap, 6, 20))  # [20, 12, 10, 11, 5, 6, 7, 8, 9, 3, 1, 4]
print(D_Heap_Insert(D_Heap, 15))  # [15, 7, 10, 12, 5, 6, 2, 8, 9, 3, 1, 4, 11]
