# v1 = {"k1": 123}
# print(id(v1))  # 输出：4515998128
# del v1
# v2 = {"name": "武沛齐", "age": 18, "gender": "男"}
# print(id(v2))  # 输出：4515998128地址：4436033488
#
# v1 = [11, 22, 33]
# print(id(v1))  # 输出：4517628816
# del v1
# v2 = ["武", "沛齐"]
# print(id(v2))  # 输出：4517628816
#
# v1 = "A"
# print(id(v1))  # 输出：4517720496
# del v1
# v2 = "A"
# print(id(v2))  # 输出：4517720496
# # 除此之外，Python内部还对字符串做了驻留机制，针对那么只含有字母、数字、下划线的字符串（见源码Objects/codeobject.c），如果内存中已存在则不会重新在创建而是使用原来的地址里（不会像free_list那样一直在内存存活，只有内存中有才能被重复利用）。
# v1 = "wupeiqi@"
# v2 = "wupeiqi@"
# print(id(v1)==id(v2))  # 输出：True
#
# v1 = [11, 22, 33]
# print(id(v1))  # 输出：4517628816
# del v1
# v2 = ["武", "沛齐"]
# print(id(v2))  # 输出：4517628816
# l = [1, 2, 3]
# l_iter = l.__iter__()
# from collections.abc import Iterable
# from collections.abc import Iterator
#
# print(isinstance(l, Iterable))  # True             #查看是不是可迭代对象
# print(isinstance(l, Iterator))  # False            #查看是不是迭代器
# print(isinstance(l_iter, Iterator))  # True
# print(isinstance(l_iter, Iterable))  # True
# s = "我爱北京天安⻔"
# c = s.__iter__() # 获取迭代器
# print(c.__next__()) # 使⽤迭代器进⾏迭代. 获取⼀个元素 我
# print(c.__next__()) # 爱
# print(c.__next__()) # 北
# print(c.__next__()) # 京
# print(c.__next__()) # 天
# print(c.__next__()) # 安
# print(c.__next__()) # ⻔
# print(c.__next__()) # StopIteration
# def func():
#     print("111")
#     yield 222
#     print("333")
#     yield 444
# gener = func()
# ret = gener.__next__()
# print(ret)
# ret2 = gener.__next__()
# print(ret2)
# ret3 = gener.__next__()
# def eat():
#     for i in range(1,10000):
#         a = yield '包子'+str(i)
#         print('a is',a)
#         b = yield '窝窝头'
#         print('b is', b)
# e = eat()
# print('--------')
# print(e.__next__())
# print('--------')
# print(e.send('大葱'))
# print('--------')
# print(e.send('大蒜'))
# # print('--------')
# def func():
#     lst = ['卫龙','老冰棍','北冰洋','牛羊配']
#     yield from lst
#
# g = func()
# print(g)
# for i in g:
#     print(i)
#
# def func():
#     lst1 = ['卫龙','老冰棍','北冰洋','牛羊配']
#     lst2 = ['馒头','花卷','豆包','大饼']
#     yield from lst1
#     yield from lst2
# g = func()
# for i in g:
#     print(i)
# gen = (i for i in range(10))
# print(gen)
#
#
# def x():
#     for i in 'asdfg':
#         yield i
#
#
# #
# b = list(x())
# print('list:',b)
# print(1111)
# a = x()
# print('list:',a)
# print(list(a))


# def func():
#     print(111)
#     yield 222
#
#
# g = func()  # 生成器g
# g1 = (i for i in g)  # 生成器g1. 但是g1的数据来源于g
# g2 = (i for i in g1)  # 生成器g2. 来源g1
# # list的底层有for循环,for就是一直执行__next__() 所以可以将生成器放到list中
# print(list(g))  # 获取g中的数据. 这时func()才会被执行. 打印111.获取到222. g完毕.
# print(list(g1))  # 获取g1中的数据. g1的数据来源是g. 但是g已经取完了. g1 也就没有数据了
# print(11111)
# print(list(g2))  # 和g1同理
# print(111111)
# print(next(g))
# print(next(g1))
# print(next(g2))  # 可以用next来验证  其实list就是将内容迭代了转换成了列表
#


class Queue(object):
    def __init__(self):
        self.queue = []

    def add(self, value):
        self.queue.append(value)

    def pop(self):
        return self.queue.pop()

    def remove(self, index):
        self.queue.remove(index)
    def __iter__(self):




s = Queue()
s.add(1)
s.add(1)
s.add(1)
s.add(1)
s.add(1)
for i in s:
    print(i)