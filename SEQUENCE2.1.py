#第二章 列表和元组 list turbo
#列表可以修改，但是元组不能。
edward=['edward gumby','34']
howard=['david howard','99']
database=[edward,howard]
#容器：序列和映射。可包含其他对象的对象
#序列有列表和元组。映射有字典。

#第一个元素的索引为0
greeting='hello'
greeting[0]
#等价于
'hello'[0]

fourth=input('year:')[3]

#一个索引
days=['Mon.','Tues.','Wed.','Thu.','Fri.','Sat.','Sun.']
day=input('day=')
day_number=int(day)
day_name=days[day_number-1]
print(day_name)

#切片，头在尾巴不在 结果是[2, 4]
numbers=[2,4,6,8,10]
numbers[0:2]

numbers=[2,4,6,8,10,12,14,16,18]
numbers[:3]
#结果得到[2, 4, 6]

#最后一个是步长
numbers[0:10:1]
#[2, 4, 6, 8, 10, 12, 14, 16, 18]
numbers[0:10:2]
#[2, 6, 10, 14, 18]
numbers[::4]
#[2, 10, 18]