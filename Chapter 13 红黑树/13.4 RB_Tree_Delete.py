# 删除红黑树中的结点

# 时间复杂度 O(lgn)

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




def Minimum(x):
  while x.left:
    x = x.left
  return x

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
      
    
