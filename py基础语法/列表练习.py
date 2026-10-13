numbers=[i**3 for i in range(1,11)]
for i in numbers:
    print(i)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
numbers1=[j for j in range(3,31) if j%3==0]
print(numbers1)
numbers=[k**3 for k in range(1,11)]
print(numbers)

#list_slice = source_list[start:end:step]
#start：切片起始索引位置，省略则从头开始；
#end：切片结束索引位置，省略则切至列表末尾；x
#step：切片步长，可选参数，表示每N个元素取一个，默认为1。

