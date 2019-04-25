# 习题 12.1-3：设计一个执行中序遍历的非递归算法。（提示：一种容易的方法是使用栈作为辅助数据结构；另一种较复杂但比较简洁的做法是不使用栈，但要假设能
#              测试两个指针是否相等。）


class Tree:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

# 中序遍历的递归解法
def InOrder_Tree(root):
  
