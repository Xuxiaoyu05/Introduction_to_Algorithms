# 红黑树的插入与删除

# 定义红黑树结点
class RB_Node:
  def __init__(self, val, color = "RED"):
    self.val = val
    self.left = None
    self.right = None
    self.parent = None
    self.color = color

# 定义红黑树
class RB_Tree:
  def __init__(self):
    self.root = None


  # 左旋O(1)
  def Left_Rotate(self, x):
    y = x.right
    x.right = y.left
    
    if y.left != None:
      y.left.parent = x
        
    y.parent = x.parent
    
    if x.parent == None:
      self.root = y
    else:
      if x == x.parent.left:
        x.parent.left = y
      else:
        x.parent.right = y
     
    y.left = x
    x.parent = y
    
  
  # 右旋O(1)
  def Right_Rotate(self, x):
    y = x.left
    x.left = y.right
    
    if y.right != None:
      y.right.parent = x
    
    y.parent = x.parent
    
    if x.parent == None:
      self.root = y
    else:
      if x == x.parent.left:
        x.parent.left = y
      else:
        x.parent.right = y
    
    y.right = x
    x.parent = y
    
   
  # 向红黑树中插入结点O(lgn)
  def RB_Tree_Insert(self, z):
    y = None
    x = self.root

    # 寻找 z 待替换的 None 结点
    while x != None:
      y = x      # 用 y 来存储父结点
      if z.val < x.val:
        x = x.left
      else:
        x = x.right

    z.parent = y   # 设置 z 的父结点

    if y == None:
      self.root = z
    else:
      if z.val < y.val:
        y.left = z
      else:
        y.right = z
   
    z.color = "RED"  # 新插入的结点颜色设置为红色
    
    self.RB_Tree_Insert_Fixup(z)  # 调整整棵树以保持红黑性质
  
  
  # 插入后调整树以维持红黑性质O(lgn)
  def RB_Tree_Insert_Fixup(self，z):   # 只有性质 2 和 4 可能被破坏
    while z.parent and z.parent.color == "RED":  # 性质 4 被破坏，但需要先判断 z 的父结点是否存在
      # 根据 z.parent 和 z.parent.parent 的关系分为两种情形：
      if z.parent == z.parent.parent.left:  # 若第一行条件满足，则 z.parent.parent 必然存在，因为 z.parent 为红色
        y = z.parent.parent.right    # z 的叔结点
        
        if y and y.color == "RED":      # 情况 1：叔结点为红色（此时 z.parent 和 y 都为红色），需先判断 y 是否存在
          z.parent.color = "BLACK"      # 解决方案：将 z.parent 和 y 的颜色置为黑色，z.parent.parent 置为红色，z 结点沿树上升两层。
          y.color = "BLACK"
          z.parent.parent.color = "RED"
          z = z.parent.parent
          
        else:  # 叔结点为黑色
          if z == z.parent.right       # 情况 2：叔结点为黑色 且 z 为 z.parent 的右孩子
            z = z.p                    # 解决方案：z 先上移到 z.parent, 然后通过左旋使 z 下移，
            self.Left_Rotate(z)
          
          z.parent.color = "BLACK"
          z.parent.parent.color = "RED"
          self.Right_Rotate(z.parent.parent)
          
      else:   # z.parent 为 z.parent.parent 的右结点（与上面对称的）
        y = z.parent.parent.left
        
        if y and y.color == "RED":
          z.parent.color = "BLACK"
          y.color = "BLACK"
          z.parent.parent == "RED"
          z = z.parent.parent
          
        else:
          if z == z.parent.right:
            z = z.parent
            self.Left_Rotate(z)
          
          z.parent.color = "BLACK"
          z.parent.parent.color = "RED"
          self.Left_Rotate(z.parent.parent)
      
    self.root.color = "BLACK"   # 恢复性质 2
  
  # 前序遍历
  def PreOrder_RB_Tree(self):
    res = []
    colors = []
    stack = []
    stack.append(self.root)
    
    while stack:
      cur = stack.pop()
      res.append(cur.val)
      colors.append(cur.color)
      
      if cur.right:
        stack.append(cur.right)
      if cur.left:
        stack.append(cur.left)
      
    return res, colors
  
  
  # 创建一棵红黑树
  def Create_RB_Tree(self, arr):
    for i in arr:
      self.root = RB_Tree_Insert(RB_Node(i))
    
    # 前序遍历输出构建的树
    print(PreOrder_RB_Tree())
    
  def RB_Tree_Node_Transplant(self, u, v):
    if u.parent == None:
      self.root = v
    else:
      if u == u.parent.left:
        u.parent.left = v
      else:
        u.parent.right = v
    
    if v != None:
      v.parent = u.parent
  
  # 寻找树中最小的结点
  def Find_Minimum(self, x):
    while x.left:
      x = x.left
    return x
  
  
  # 删除红黑树中的结点O(lgn)
  def RB_Tree_Delete(self, z):
    y = z    # y 始终指向树中待删除或待移动的结点，x 结点为将移到树中 y 位置的结点
    y_original_color = z.color
    
    if z.left == None:                         # 情况1：z 的左孩子为空，右孩子可为空或不为空
      x = z.right                              # 解决方法：用 z.right 来替代 z
      RB_Tree_Node_Transplant(z, z.right)      
    elif z.right == None:                      # 情况2：z 的左孩子不为空，右孩子为空
      RB_Tree_Node_Transplant(z, z.left)       # 解决方法：用 z.left 来替代 z
    else: # 情况3：当 z 的左右孩子都存在，在右子树中寻找其后继结点
      y = Find_Minimum(z.right)
      y_original_color = y.color
      
      x = y.right
      
      if y.parent != z: # 如果 y 不是 z 的右孩子
        RB_Tree_Node_Transplant(y, y.right)
        y.right = z.right
        y.right.parent = y
      
      RB_Tree_Node_Transplant(z, y)
      y.left = z.left
      y.left.parent = y
      
      y.color = z.color       # 不要忘了将 y 的颜色更改为 z 的颜色
    
    
    if y_original_color == "BLACK":     # 如果 y 的原始颜色为红色，那么将不会破坏红黑性质；
      RB_Tree_Delete_Fixup(x)           # 如果 y 的原始颜色为黑色，则需要调用 RB_Tree_Delete_Fixup(x) 来维持整棵树的红黑性质
   
  # 删除后调整树以维持红黑性质O(lgn)
  def RB_Tree_Delete_Fixup(self, x):
    # 可能会被破坏的性质为：
    #（1）性质2（y 是根结点，它的红色孩子成为新的根结点）；
    #（2）性质4（x 和 x.p 都为红色）；
    #（3）性质5（黑色结点的删除或移动导致y的祖先的黑高改变）; 解决方法：将占有 y 位置的结点 x 视为还有额外的黑色，x 为双重黑色或红黑色
    
    while x and x.color == "BLACK":  # 当 x 的颜色为红色时退出循环
      # 根据 x 和其父结点 x.parent 之间的关系分为两大类情况
      if x == x.parent.left:
        w = x.parent.right     # w 是 x 的兄弟结点
        if w.color == "RED":   # 情况1：w 的颜色是红色
          w.color = "BLACK"    # 解决方法：将其转换为情况 2,3,4 处理，w 改为黑色，x.parent 改为红色并左旋，更改 w 为 x 的新的兄弟结点
          x.parent.color = "RED"
          Left_Rotate(x.parent)
          w = x.parent.right    # 此时 w 的颜色一定是黑颜色
        
        if w.left.color == "BLACK" and w.right.color == "BLACK":   # 情况2：w 为黑色且其左右孩子均为黑色
          w.color = "RED"                                          # 解决方法：将 w 的颜色改为红色，x 上移
          x = x.parent
        else:
          if w.right.color == "BLACK":   # 情况3：w 为黑色且其右孩子为黑色，左孩子为红色
            w.left.color = "BLACK"       # 解决方法：转为情况4，将 w.left 改为黑色，w 改为红色，并将 w 右旋，更改 w 为 x 的新的兄弟结点
            w.color = "RED"
            Right_Rotate(w)
            w = x.parent.right
          
          w.color = x.parent.color       # 情况4：w 为黑色且其右孩子为红色
          x.parent.color = "BLACK"
          w.right.color = "BLACK"
          Left_Rotate(x.parent)
          x = self.root
     else:   # x == x.parent.right （对称的）
      w = x.parent.left
      if w.color == "RED":  # 情况1：w 结点是红色的
        w.color = "BLACK"
        x.parent.color = "RED"
        Right_Rotate(x.parent)
        w = x.parent.left
     
      if w.left.color == "BLACK" and w.right.color == "BLACK"   # 情况2：w 及其左右孩子都为黑色
        w.color = "RED"
        x = x.parent
      else:
        if w.right.color == "BLACK":   # 情况3：w 为黑色，其左孩子为红色，右孩子为黑色
          w.color = "RED"
          w.left.color = "BLACK"
          Right_Rotate(w)
          w = x.parent.left
        
        w.color = x.parent.color
        x.parent.color = "BLACK"
        w.right.color = "BLACK"
        Right_Rotate(x.parent)
        x = self.root

    x.color = "BLACK"     # 若 x 为红色，将其颜色置为黑色
      
    
    
