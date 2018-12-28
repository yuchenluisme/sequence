#修改列表中的值
x=[1,1,1]
x[1]=2
x
del x[2]

#给切片赋值
name=list('richard')
name[2:]=list('ta')
#name
#['r', 'i', 't', 'a']

#numbers
#[1, 2, 3, 9, 5]
numbers=[1,5]
numbers[1:1]=[2,3,9]

lst=[1,2,3,4]
lst.append(4)
#lst
#[1, 2, 3, 4, 4]

a=[13,3]
b=[3]
a.extend(b)
a
#[13, 3, 3]

a=[4,0,6]
b=a.copy()
b[0]=8
#b
#[8, 0, 6]
#a
#[4, 0, 6]
a.count(0)
#1

c=[3,4,2,3]
c.index(3)
#用Index索引找到第一个0的位置

numbers
[1, 2, 3, 9, 5]
numbers.insert(0,29)
numbers
#[29, 1, 2, 3, 9, 5]


#pop删除第几个元素
numbers
[29, 1, 2, 3, 9, 5]
numbers.pop(2)
#2
numbers.pop(2)
#3

#remove移除元素
numbers
[29, 1, 9, 5]
numbers.remove(5)
numbers
[29, 1, 9]

#.sort(numbers)排序

#创建一个元素的tuple
67,

#必须有逗号(67,)
