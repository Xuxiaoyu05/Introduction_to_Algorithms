# 思考题7.6：(对区间的模糊排序) 考虑这样的一种排序问题：我们无法准确知道待排序的数字是什么。但对于每一个数，我们知道它属于实数轴上的某个区间。也就是说，
#            我们得到了 n 个形如 [ai, bi] 的闭区间，其中 ai <= bi。我们的目标是实现这些区间的模糊排序，即对 j = 1, 2, ..., n 生成一个区间的排列
#            <i1, i2, ..., in>, 且存在 cj ∈ [aij, bij]，满足 c1 <= c2 <= ... <= cn。

#7.6(a)：为 n 个区间的模糊排序设计一个随机算法。你的算法应该具有算法的一般结构，它可以对左边端点（即 ai 的值）进行快速排序，同时它也能利用区间的重叠性质
#        来改善时间性能。（当区间重叠越来越多的时候，区间的模糊排序问题会变得越来越容易。你的算法应当充分利用这一重叠性质。）

#7.6(b)：证明：在一般情况下，你的算法的期望运行时间为 θ(nlgn)。但是，当所有的区间都有重叠的时候，算法的期望运行时间为 θ(n)（也就是说，存在一个值 x，对
#             所有的 i，都有 x ∈ [ai, bi]。）你的算法不必显示地检查这种情况，而是随着重叠情况的增加，算法的性能自然地提高。


def
