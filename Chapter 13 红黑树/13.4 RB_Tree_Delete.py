# 删除红黑树中的结点

# 总时间复杂度 O(lgn)：
# 因为含有 n 个结点的红黑树的高度为 O(lgn)，RB_Delete 不调用 RB_Delete_Fixup 时该过程的总时间代价为 O(lgn)。
# 在 RB_Delete_Fixup 中，情况 1、3 和 4 在各执行常数次数的颜色改变和至多 3 次旋转后便终止。情况 2 是 while 循环可以重复执行的唯一情况，然后指针 x
# 沿树上升至多 O(lgn) 次，且不执行任何旋转。所以，过程 RB_Delete_Fixup 要花费 O(lgn) 时间，做至多 3 次旋转，所以 RB_Delete 运行的总时间为 O(lgn)。


# 基本思想：从一棵红黑树中删除结点的过程是基于 Tree_Delete 过程而来的。首先需要设计一个供 Tree_Delete 调用的子过程 RB_Transplant，并应用到红黑树上。

def RB_Transplant(root, u, v):
  if u.p == None:
    root = v
  else:
    if u == u.parent.left:
      u.parent.left = v
    else:
      u.parent.right = v
      
  if v != None:
    v.parent = u.parent

# RB_Delete：类似于 Tree_Delete，多出的代码记录结点 y 的踪迹（y 有可能导致红黑性质的破坏）
#（1）始终维持结点 y 为从树中删除的结点或者移至树内的结点。
#     当 z 的子结点少于两个时，第 1 行将 y 指向 z（待移除）。当 z 有两个子结点时，第 9 行将 y 指向 z 的后继，y 将移至树中 z 的位置。
#（2）由于结点 y 的颜色可能发生改变(y.color = z.color)，变量 y_original_color 存储了发生改变前的结点 y 的颜色。（在给 y 赋值后立刻设置该变量）
# 记录结点 x 的踪迹，将 x 移至树中 y 的原来位置。

# 在结点被移除或在树中移动之前，必须记住 y 的颜色，并且记录结点 x 的踪迹，将 x 移至树中 y 的原来位置，因为结点 x 也可能引起红黑性质的破坏。
# 删除结点 z 后，如果结点 y 的原始颜色为黑色，则调用辅助过程 RB_Delete_Fixup，通过改变颜色和执行旋转来恢复红黑性质。
# 如果 y 的原始颜色为红色，当 y 被删除或移动时，红黑性质仍然保持。原因如下:
#（1）树中的黑高没有发生变化；
#（2）不存在两个相邻的红结点。因为 y 占据了 z 的位置，再考虑到 z 的颜色，树中的新位置不可能有两个相邻的红结点。另外，如果 y 不是 z 的右孩子，则 y 的原
#     右孩子 x 代替 y。如果 y 是红色，则 x 一定是黑色，因此用 x 代替 y 不可能使两个红结点相等。
#（3）如果 y 是红色，就不可能是根结点，所以根结点仍旧是黑色。

# 如果结点 y 的原始颜色为黑色，则会出现 3 个问题，需要用 RB_Delete_Fixup 进行调整。
#（1）如果 y 是原来的根结点，而 y 的一个红色的孩子成为新的根结点，这就违反了性质 2；
#（2）如果 x 和 x.p 是红色的，则违反了性质 4；
#（3）在树中移动 y 将导致先前包含 y 的任何简单路径上黑结点个数少 1，因此 y 的任何祖先都不满足性质 5。

# 问题（3）解决方法：将现在占有 y 原来位置的结点 x 视为还有一种额外的黑色。也就是说，如果将任意包含结点 x 的简单路径上黑结点个数加 1，则性质 5 成立。
# 在这种假设下，当将黑结点 y 删除或移动时，将其黑色 “下推” 给结点 x。现在问题变为结点 x 既不能红色，又不是黑色，从而违反了性质 1。现在的结点 x 是双重
# 黑色或者红黑色，这就分别给包含 x 的简单路径上黑结点数贡献了 2 或 1。x 的 color 属性仍为 RED（如果 x 是红黑色的）或 BLACK（如果 x 是双重黑色的）。
# 即结点额外的黑色是针对 x 结点的，而不是反映在它的 color 属性上的。

def RB_Tree_Delete(root, z):
  y = z
  y_original_color = y.color
  
  if z.left == None:
    x = z.right   # x 记录取代 y 的结点
    RB_Transplant(root, z, z.right)
  elif z.right == None:
    x = z.left
    RB_Transplant(root, z, z.left)
  else:
    y = Minimum(z.right)
    y_original_color = y.color
    x = y.right    # y.right 取代 y 原来在树中的位置
    
    if y.parent == z:
      x.parent = y   # 当 y 为 z 的右孩子时，我们并不想让 x.p 指向 y 的原始父结点，因为要在树中删除该结点，由于结点 y 将在树中向上移动占据 z 的位置，
                     # 所以将 x.p 设置为 y，使得 x.p 指向 y 父结点的原始位置。
    else:
      RB_Transplant(root, y, y.right)
      y.right = z.right
      y.right.parent = y
    
    RB_Transplant(root, z, y)
    y.left = z.left
    y.left.parent = z
    
    y.color = z.color   # 将 y 的颜色设置为 z 的原本颜色
    
    if y_original_color == "BLACK":  # 如果结点 y 为黑色，就有可能引入了一个或多个红黑性质被破坏的情况，需要调用 RB_Delete_Fixup 来恢复红黑性质
      RB_Delete_Fixup(T, x) 
      
# while 循环的目标是将额外的黑色沿树上移，直到：
#（1）x 指向红黑结点，此时在最后一行中，将 x 着为（单个）黑色；
#（2）x 指向根结点，此时可以简单的“移除”额外的黑色；
#（3）执行适当的旋转和重新着色，退出循环。

# 在 while 循环中，x 总是指向一个具有双重黑色的非根结点。第 2 行中要判断 x 是其父结点 x.p 的左孩子还是右孩子（代码对称）。
# 保证指针 w 指向 x 的兄弟，由于结点 x 是双重黑色的，故 w 不可能是 None（因为否则，从 x.p 至（单黑色）叶子 w 的简单路径上的黑结点个数就会小于从x.p到
#  x 的简单路径上的黑结点数）。
# 4 种情况：
#（1）x 的兄弟结点 w 是红色的：
#    因为 w 必须有黑色子结点，所以可以改变 w 和 x.p 的颜色，然后对 x.p 做一次左旋而不违反红黑树的任何性质。现在，x 的新兄弟结点是旋转之前 w 的某个子
#    结点，其颜色为黑色，这样，就将情况 1 转换为情况 2，3 或 4 处理。
# 当结点 w 为黑色时，属于情况 2、3 和 4；这些情况是由 w 的子结点的颜色来区分的。
#（2）x 的兄弟结点 w 是黑色的，而且 w 的两个子结点都是黑色的：
#    当 w 的两个子结点都是黑色的，因为 w 也是黑色的，所以从 x 和 w 上去掉一重黑色，使得 x 只有一重黑色而 w 为红色。为了补偿从 x 和 w 中去掉的一重黑色，
#    在原来是红色或黑色的 x.p 上新增一重额外的黑色。通过将 x.p 作为新结点 x 来重复 while 循环。注意到，如果通过情况 1 进入到情况 2，则新结点 x 是红黑色的，
#    因为原来的 x.p 是红色的。因此，新结点 x 的 color 属性值 c 是 RED，并在测试循环条件后循环终止。然后在最后一行将新结点 x 着为（单一）黑色。
#（3）x 的兄弟结点 w 是黑色的，w 的左孩子是红色的，w 的右孩子是黑色的：
#    交换 w 和其左孩子 w.left 的颜色，然后对 w 进行右旋而不违反红黑树的任何性质。现在 x 的新结点 w 是一个有红色右孩子的黑色结点，这样我们就将情况 3
#    转换成了情况 4。
#（4）x 的兄弟结点 w 是黑色的，且 w 的右孩子时红色的。
#    通过进行某些颜色修改并对 x.p 做一次左旋，可以去掉 x 的额外黑色，从而使它变为单重黑色，而且不破坏红黑树的任何性质。将 x 设置为根后，当 while 循环
#    测试其循环条件时，循环终止。 

def RB_Tree_Delete_Fixup(root, x):
  while x and x.color == "BLACK":
    if x == x.parent.left:
      w = x.parent.right:
      if w.color == "RED":  # 情况 1
        w.color == "BLACK"
        x.parent.color == "RED"
        Left_Rotate(root, x.parent)
        w = x.parent.right  # 此时的 w 结点已经是黑色的
      
      if w.left.color == "BLACK" and w.right.color == "BLACK": # 情况 2：w 及其左右子结点都是黑色的
        w.color = "RED"
        x = x.parent
      
      else: 
        if w.right.color == "BLACK": # 情况3：w 及其右结点为黑色，左结点为红色
          w.left.color = "BLACK"
          w.color = "RED"
          Right_Roatete(root, w)
          w = x.parent.right
        
        w.color = x.parent.color 
        x.parent.color = "BLACK"
        w.right.color = "BLACK"
        Left_Rotate(root, x.parent)
        x = root
        
    else: # x == x.parent.right
      w = x.parent.left
      if w.color == "RED": # 情况1
        w.color = "BLACK"
        x.parent.color = "RED"
        Right_Rotate(root, x.parent)
        w = x.parent.left  # 此时 w 的结点是黑色的
      
      if w.left.color == "BLACK" and w.right.color == "BLACK": # 情况2
        w.color = "RED"
        x = x.parent
      else:
        if w.right.color == "BLACK"  # 情况3
          w.left.color = "BLACK"
          w.color = "RED"
          Right_Rotate(root, w)
          w = x.parent.left
        
        w.color = x.parent.color  # 情况4
        x.parent.color = "BLACK"
        Left_Rotate(root, x.parent)
        x = root
          
  x.color = "BLACK"   # 将 x 的颜色设置为黑色      
