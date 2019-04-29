# 旋转

# 为什么要进行旋转？
#（1）Tree_Insert 和 Tree_Delete 在含 n 个关键字的红黑树上，运行时间为 O(lgn)。但这两个操作对树做了修改，导致树可能违反红黑性质；                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
#（2）为了维护红黑性质，必须要改变树中某些结点的颜色以及指针结构；
#（3）指针结构的修改是通过旋转来完成的。（旋转操作保持了二叉搜索树的性质（值之间的大小关系））

# 旋转分类：
#（1）左旋：当在某个结点 x 上做左旋时，假设它的右孩子为 y 而不是 None，x 可以为其右孩子不是 None 的树内任意结点。左旋以 x 到 y 的链为“支轴”进行，它使
#          y 成为该子树新的根结点，x 成为 y 的左孩子，y 的左孩子成为 x 的右孩子。
#（2）右旋：当在某个结点 y 上做右旋时，假设它的左孩子为 x 而不是 None，y 可以为其左孩子不是 None 的树内任意结点。右旋以 y 到 x 的链为“支轴”进行，它使
#          x 成为该子树新的根结点，y 成为 x 的右孩子，x 的右孩子成为 y 的左孩子。

# 时间复杂度分析：
# 左旋和右旋均通过改变常数数目的指针来实现，因此都在 O(1) 时间内运行完成。
# 在旋转操作中只有指针改变，其它所有属性都保持不变。

# 左旋
def Left_Rotate(root, x):
  y = x.right     # 设置 y
  
  x.right = y.left   # y 的左孩子成为 x 的右孩子
  if y.left != None:
    y.left.parent = x
    
  y.parent = x.parent   # 将 y 的父结点设置为 x 的父结点
  if x.parent == None:
    root = y
  else:
    if x == x.parent.left:
      x.parent.left = y
    else:
       x.parent.right = y
  
  y.left = x             # 将 x 设置为 y 的左孩子
  x.parent = y
  
# 右旋
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
