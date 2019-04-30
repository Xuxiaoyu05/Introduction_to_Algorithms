# 向红黑树中插入新结点

# 基本思想：(1) 利用 Tree_Insert 的略修改版本 RB_Treee_Insert 将新结点 z 插入树 T 内（将树 T 视为一棵普通的二叉搜索树），然后将 z 着为红色（不能是黑色）；
#          (2) 为了保证红黑性质，调用辅助过程 RB_Insert_Fixup 来对结点进行重新着色并旋转。

# RB_Tree_Insert 时间复杂度 O(lgn):
# 分析：由于一棵有 n 个结点的红黑树的高度为 O(lgn)，因此 RB_Insert 根据值寻找插入位置需要花费 O(lgn) 时间；
#       在 RB_Insert_Fixup 中，仅当情况 1 发生，指针 z 沿着树上升两层，while 循环才会重复执行，所以 while 循环可能被执行的总次数为 O(lgn)；
#       因此 RB_Tree_Insert 总共花费 O(lgn) 时间。
#       此外，该程序所做的旋转从不超过 2 次，因为只要执行了情况 2 或情况 3，while 循环就结束了。


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
  
  return root
   

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
      x.parent.left = y
    else:
      x.parent.right = y
      
  y.right = x
  x.parent = y
  
  return root
  
def RB_Tree_Insert_Fixup(root, z):
  while z.parent and z.parent.color == "RED":  # 性质 4 被破坏，需要判断 z 是否存在父结点
    if z.parent == z.parent.parent.left:  # 判断 z 的父结点和祖父结点的关系，因为 z.p 为红色，所以 z.p.p 必然存在
      y = z.parent.parent.right    # y 为 z 的叔结点
      if y and y.color == "RED":  # 情况1，需要判断叔结点是否存在
        z.parent.color = "BLACK"
        y.color = "BLACK"
        z.parent.parent.color = "RED"
        z = z.parent.parent  # 将 z 沿树上移两层
      else: # 叔结点为黑色
         if z == z.parent.right:  # 情况2
            z = z.parent
            root = Left_Rotate(root, z)  # 左旋变为情况3
         z.parent.color = "BLACK"  # 情况3
         z.parent.parent.color = "RED"
         root = Right_Rotate(root, z.parent.parent)
    else: # z 为 z 祖父结点的右结点（与上边对称）
      y = z.parent.parent.left
      if y and y.color == "RED":
        z.parent.color = "BLACK"
        y.color = "BLACK"
        z.parent.parent.color = "RED"
        z = z.parent.parent
      else:
        if z == z.parent.right:
          z = z.parent
          root = Left_Rotate(root, z)
        z.parent.color = "BLACK"
        z.parent.parent.color = "RED"
        root = Right_Rotate(root, z.parent.parent)
   
  root.color = "BLACK"   # 修正性质 2
  
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
  
  z.color = "RED"   # 将 z 设置为红色(此步可以不需要，因为初始化的时候已经将 z 设置为红色了)
  
  root = RB_Tree_Insert_Fixup(root, z)   # 维持红黑性质，需要用 root 来平衡后的结果
  
  return root
  
def PreOrder_RB_Tree(root):
  res = []
  colors = []
  stack = []
  stack.append(root)
  
  while stack:
    cur = stack.pop()
    res.append(cur.val)
    colors.append(cur.color)
    
    if cur.right:
      stack.append(cur.right)
    if cur.left:
      stack.append(cur.left)
  
  return res, colors

# 用插入的方式创建一棵红黑树
Arr = [11, 2, 14, 1, 7, 15, 5, 8]
root = None
for i in Arr:
  root = RB_Tree_Insert(root, RB_Tree_Node(i))  # 此处必须要加 root =...，否则传入函数的 root 一直是 None
print(PreOrder_RB_Tree(root))  # 结果：([11, 2, 1, 7, 5, 8, 14, 15], ['BLACK', 'RED', 'BLACK', 'BLACK', 'RED', 'RED', 'BLACK', 'RED'])
# 插入值为 4 的结点
root = RB_Tree_Insert(root, RB_Tree_Node(4))
print(PreOrder_RB_Tree(root))  # 结果：([7, 2, 1, 5, 4, 11, 8, 14, 15], ['BLACK', 'RED', 'BLACK', 'BLACK', 'RED', 'RED', 'BLACK', 'BLACK', 'RED'])
