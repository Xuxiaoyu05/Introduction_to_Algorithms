# 向红黑树中插入新结点

# 基本思想：(1) 利用 Tree_Insert 的略修改版本 RB_Treee_Insert 将新结点 z 插入树 T 内（将树 T 视为一棵普通的二叉搜索树），然后将 z 着为红色（不能是黑色）；
#          (2) 为了保证红黑性质，调用辅助过程 RB_Insert_Fixup 来对结点进行重新着色并旋转。

# 时间复杂度 O(lgn)


class RB_Tree_Node:
  def __init__(self, val, color = "RED"):
    self.val = val
    self.left = None
    self.right = None
    self.parent = None
    self.color = color


# RB_Insert_Fixup 过程（三步骤）：
# 分析：当新结点 z 被插入并着为红色，可能被破坏的红黑性质：性质1、性质3、性质5继续成立；性质 2 和性质 4 可能被破坏（因为 z 被设置为红色）。
#       如果有任何红黑性质被破坏，则至多有一条被破坏：）（1）z 是根结点被着为红色，破坏了性质2；（2） z 的父结点是红结点，则破坏了性质4。

# 代码中的 while 循环有 6 种情况：其中三种与另外三种是对称的，这取决于 z 的父结点 z.p 是 z.p.p 的左孩子，还是右孩子。
# 循环的每次迭代有两种可能的结果：（1）指针 z 沿着树上移；（2）执行某些旋转后循环终止。
# 可分为三种情况：区别在于 z 父亲的兄弟结点（“叔结点”）的颜色是红色还是黑色。
#（1）情况1：z 的叔结点 y 是红色的（不区分 z 是左孩子还是右孩子）
#     解决方法：此时 z.p.p 肯定是黑色，因此将 z.p 和 y 都着为黑色，将 z.p.p 着为红色以保持性质 5，然后将 z.p.p 作为新结点 z 来重复 while 循环，
#              指针 z 在树中上移两层。
#（2）情况2： z 的叔结点 y 是黑色的 且 z 是一个右孩子
#     解决方法：可以使用一个左旋将情况 2 转化为情况 3，因为 z 和 z.p 都是红色的，所以该旋转对结点的黑高和性质 5 都无影响。
#（3）情况2： z 的叔结点 y 是黑色的 且 z 是一个左孩子
#     解决方法：改变某些结点的颜色并做一次右旋，以保持性质 5。这样由于在一行中不再有两个红色结点，所有的处理到此完毕。因为此时 z.p 是黑色的，
#              所以无需再执行一次 while 循环。

def Left_Rotate(root, x):
  y = x.right
  x.right = y.left
  
  if y.left != None:
    y.left.parent = x
 
  y.parent = x.parent
  
  if x.parent == None:
    root = y
  else:
    if x == x.parent.left:
      x.parent.left = y
    else:
      x.parent.right = y
  
  y.left = x
  x.parent = y
   

def Right_Rotate(root, x):
  y = x.left
  x.left = y.right
  if y.right != None:
    y.right.parent = x
  
  y.parent = x.parent
  if x.parent == None:
    root = y
  else:
    if x == x.parent.left:
      y = x.parent.left
    else:
      y = x.parent.right
      
  y.right = x
  x.parent = y

  
def RB_Tree_Insert_Fixup(root, z):
  while z.parent.color == "RED":  # 性质 4 被破坏
    if z.parent == z.parent.parent.left:  # 判断 z 的父结点和祖父结点的关系，因为 z.p 为红色，所以 z.p.p 必然存在
      y = z.parent.parent.right    # y 为 z 的叔结点
      if y.color == "RED":  # 情况1
        z.parent.color = "BLACK"
        y.color = "BLACK"
        z.parent.parent.color = "RED"
        z = z.parent.parent  # 将 z 沿树上移两层
      else: # 叔结点为黑色
         if z == z.parent.right:  # 情况2
            z = z.parent
            Left_Rotate(root, z)  # 左旋变为情况3
         z.parent.color = "BLACK"  # 情况3
         z.parent.parent.color = "RED"
         Right_Rotate(root, z.parent.parent)
    else: # z 为 z 祖父结点的右结点（与上边对称）
      y = z.parent.parent.left
      if y.color == "RED":
        z.parent.color = "BLACK"
        y.color = "BLACK"
        z.parent.parent.color = "RED"
        z = z.parent.parent
      else:
        if z == z.parent.right:
          z = z.p
          Left_Rotate(root, z)
        z.parent.color = "BLACK"
        z.parent.parent.color = "RED"
        Right_Rotate(root, z.parent.parent)
   
  root.color = "BLACK"   # 修正性质 2 

def RB_Tree_Insert_Val(root, val):
  y = None
  x = root
  
  while x != None:
    y = x
    if val < x.val:
      x = x.left
    else:
      x = x.right
  
  z = RB_Tree_Node(val)
  z.parent = y
  z.color = "RED" 
  
  if y == None:
    root = z
  else:
    if val < y.val:
      y.left = z
    else:
      y.right = z
      
  return root

def RB_Tree_Insert(root, z):
  y = None
  x = root
  
  while x != None:
    y = x
    if z.val < x.val:
      x = x.left
    else:
      x = x.right
  
  z.parent = y
  if y == None:
    root = z
  else:
    if z.val < y.val:
      y.left = z
    else:
      y.right = z
  
  # z.left = None
  # z.right = None
  
  z.color = "RED"   # 将 z 设置为红色
  
  RB_Tree_Insert_Fixup(root, z)   # 维持红黑性质
  
 
# 用插入的方式创建一棵红黑树
Arr = [11, 2, 1, 7, 5, 8, 14, 15]
root = None
for i in Arr:
  root = RB_Tree_Insert_Val(root, i)  # 此处必须要加 root =...，否则传入函数的 root 一直是 None
print(root.val)  
  

 
