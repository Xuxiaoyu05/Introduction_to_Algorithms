# 链表

# 基本定义：链表中的各对象按线性顺序排列。数组的线性顺序是由数组下标决定的，与数组不同的是，链表的顺序是由各个对象里的指针决定的。

# 双向链表：双线链表中的每个元素都是一个对象，每个对象有一个关键字 key 和两个指针：next 和 prev。对象中还可以包含其它的辅助数据（即卫星数据）。
#          设 x 为链表的一个元素，x.next 指向它在链表中的后继元素，x.prev 指向它的前驱元素。
#          如果 x.prev = None, 即元素 x 没有前驱，因此 x 是链表的第一个元素，即链表的头(head)；
#          如果 x.next = None，则元素 x 没有后继，因此 x 是链表的最后一个元素，即链表的尾(tail)。
#          属性 L.head 指向链表的第一个元素，如果 L.head = None，则链表为空。

# 链表分类：链表可以有多种形式，可以是单链接的或双链接的，可以是已排序的或未排序的，可以是循环的或非循环的。
#          如果一个链表是单链接的，则省略每个元素的 prev 指针。在循环链表中，表头元素的 prev 指针指向表尾元素，表尾元素的 next 指针则指向表头元素。


# 双向链表
class ListNode:
  def __init__(self, x):
    self.val = x
    self.prev = None
    self.next = None

class LinkedList:
  # 链表的搜索，最坏情况下可能要搜索整个链表，运行时间为θ(n) 
  def List_Search(self, head, k):
    x = head
    while x != None and x.val != k:
      x = x.next
    return x

  # 链表的插入（在头部插入）
  # 在一个含 n 个元素的链表上执行 List-Insert 的运行时间是 O(1)
  def List_Insert(self, head, x):
    x.next = head
    if head != None:
      head.prev = x
    head = x
    x.prev = None
    return head

  # 链表的删除（在尾部删除）
  # 过程 List-Delete 将一个元素 x 从链表 L 移除。该过程要求给定一个指向 x 的指针，然后通过修改一些指针，将 x "删除出" 该链表。
  # 如果要删除具有给定关键字值的元素，则必须先用 List-Search 找到该元素。
  # List-Insert 的运行时间是 O(1)，若要删除具有给定关键字的元素，则最坏情况下需要的时间为θ(n)[List-Search的时间]
  def List_Delete(self, head, x):
    if x.prev != None:
      x.prev.next = x.next
    else:
      head = x.next

    if x.next != None:
      x.next.prev = x.prev
    return head
  
 
l1 = ListNode(1)
l2 = ListNode(3)
l3 = ListNode(5)
l4 = ListNode(7)

l1.next = l2
l2.next = l3
l3.next = l4

l2.prev = l1
l3.prev = l2
l4.prev = l3

l5 = ListNode(9)

linked = LinkedList()

print(linked.List_Search(l1, 5).next.val)
print(linked.List_Insert(l1, l5).val)
print(linked.List_Delete(l1, l2).next.val)



# 习题 10.2-1：单链表上的动态集合操作 Insert 能否在 O(1) 时间内实现？ Delete操作呢？
# 答：单链表上的 Insert 操作可以在 O(1) 内实现。但是 Delete 不行，因为必须要顺着链表检索到其前一个结点，然后将前一个结点的 next 属性置为 x.next。
