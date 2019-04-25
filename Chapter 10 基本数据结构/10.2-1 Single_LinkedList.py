# 习题 10.2-1：单链表上的动态集合操作 Insert 能否在 O(1) 时间内实现？ Delete操作呢？
# 答：单链表上的 Insert 操作可以在 O(1) 内实现。但是 Delete 不行，因为必须要顺着链表检索到其前一个结点，然后将前一个结点的 next 属性置为 x.next。

class ListNode:
  def __init(self, x):
    self.val = x
    self.next = None

class SingleLinkedList:
  def SList_Search(self, head, k):
    x = head
    while x != None and x.val != k:
      x = x.next
    return x
  
  def SList_Insert(self, head, x):
    x.next = head
    head = x
  
  def SList_Delete(self, head, x):
    
