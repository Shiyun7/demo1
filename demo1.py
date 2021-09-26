"""
print("hello world")
print("xixi"+"hh")
#print("hhh"*100)  #打印100个hhh
print(8>9)

"""
# a = int(input("请输入："));#input输入的都是字符串

# b = int(input("请输入："))
# print("获取的内容：",a+b)

# c = "sdfjsdjfsf"
# print(len(c))
#数据格式的转换
# print(type(()))

#练习通过代码获取两段内容，并且计算他们的长度之和
# a = input("请输入：")
# b = input("请输入：")
# print("两个字符串的综合为：",len(a+b))

#一维元组
#a = ()  #空的元组
# a = (1,2,3,"jj","jj","True")
# print(a)
#元组的下标
#print(a[2])
# print(a.index("jj"))   #打印出第一个jj的下标
# print(a.count("jj"))  #打印出有多少个jj
# print(a[-1])   #打印出右边最后一个字符
#批量取值（切片）
#print(a[0:4])   #左闭右开
#print(a[3:5])  #打印出第三个到第五个（不包括第五个）字符
# print(a[5:])  #第5个到最后
# print(a[:4])   #从第一个开始到第4个


#二维元组，元组里面套几个元组就是几维元组
# b = (a,"jj","jj")  #b里面有3个值
# print(b[0][3])


######数组和元组的区别：
#元组一定写好过后不可以修改，而数组是可以修改的
###数组####
# a = [1,2,4,3,"dfs","sdf","sdf"]
# a.append("追加数据")  #append是在数组末尾追加数据

# a.insert(0,"insert")  #insert(下标,要插入的字符)，表示在哪个下标前插入字符
# print(a)
# #print(a.pop(4))   #类似剪切的作用，就是将某个值拿出来放到其他地方去用
# #print(a)
# #pop(下标)  这个方法是将下标为4的值剪切出来
# b = a.pop(4)
# print(b)

# a = ["sdf"]
# xx = ["hello","not fine",False]
# a.extend(xx)  #将xx里面的内容放到a数组里
# print(a)
# print(a+xx)  #这种方法也能实现extend的作用

 #print(a)
# a.remove("sdf")
# print(a)
# b = xx.remove(0)  #将False识别成0
# print(b)
# print(xx)

""""
所有的方法都是用小括号结尾；元组、数组、字典的取值都是用中括号
元组、数组、字典的定义，分别是(),[],{}
"""

#字典.字典的特点：
#1、字典中的值没有顺序   2、字典的结构必须是键值对的结构  key:value
# a = {
# "name":"李四",
# 0:"很好",
# "age":25
# }
# # print(a)
# #取值
# print(a["name"])
# #新增
# a["weight"] = "45kg"
# print(a)
# #修改
# a["name"] = "zhangsan"
# print(a)
# #字典常用方法

# print(a.get("name"))
# print(a.pop("name"))
# print(a)
# a.update(age="234")   #这是没有返回值的，只是一个动作
# print(a)

#数组和字典的删除
# del a["name"]
# print(a)
# del a[0]

""""
练习：获取用户输入的个人信息，并且存储到字典中，个人信息包括姓名name、年龄age、性别sex
"""
# name = input("请输入姓名：")
# age = input("请输入年龄：")
# sex = input("请输入性别：")
# a = {"name":name,"age":age,"sex":sex}
# print(a)