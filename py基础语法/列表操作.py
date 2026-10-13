numbers=[1,2,4,5,6,7]
print(numbers)

numbers.append(8)   #末尾添加
print(numbers)
numbers.insert(2,3)    #插入
print(numbers)
del numbers[0]   #删除第三个
print(numbers)
numbers.remove(2)  #删除2这个数字
print(numbers)
a=numbers.pop()   #弹出列表最后一个元素
print(numbers)
numbers.reverse()  #反转列表
print(numbers)
#小括号()元组，只有一个元素时要在后面加逗号，例如 a = (50,)
#中括号[]列表
#大括号{}字典(有键值对)
#大括号{}集合(无键值对)