# 思考题 12.1：（带有相同关键字的二叉搜索树）相同关键字给二叉搜索树的实现带来了问题。

#              a. 当用 Tree_Insert 将 n 个相同关键字的数据插入到一棵初始为空的二叉搜索树中，其渐进性能是多少？ 答： θ(n^2)

#                 建议通过在第5行 (if z.key < x.key) 之前测试 z.key = x.key 和在第 11 行（if z.key < y.key）之前测试 z.key = y.key 的方法，来对
#                 Tree_Insert 进行改进。如果相等，根据下面的策略之一来实现。对于每个策略，得到将 n 个其中带有相同关键字的数据插入到一棵初始为空的二叉
#                 搜索树中的渐进性能。

#              b. 在结点 x 设置一个布尔标志 x.b，并根据 x.b 的值，置 x 为 x.left 或 x.right。当插入一个与 x 关键字相同的结点时，每次访问 x 时交替的置
#                 x.b 为 False 或 True。
             
#              c. 在 x 处设置一个与 x 关键字相同的结点列表，并将 x 插入到该列表中。

#              d. 随机地置 x 为 x.left 或 x.right。（给出最坏情况性能，并非形式地导出期望运行时间）


# b. 遇到关键字相同的结点时，交替设置布尔标志 x.b 为 False 或 True
def Tree_Insert_Bool(root, z):
  y = None
  x = root
  
  x_flag = True
  
  while x != None:
    y = x
    if z.key == x.key:
      if x_flag:
        x = x.left
      else:
        x = x.right
        
      x_flag = !x_flag
      
    elif z.key < x.key:
      x = x.left
    else:
      x = x.right
 
 y_flag = True
 z.parent = y
 if y == None:
    root = z
 else:
  if z.val == y.val:
    if y_flag:
      y.left = z
    else:
      y.right = z    
    y_flag = !flag
    
 elif z.key < y.key:
  y.left = z
else:
  y.right = z
    
  
   
