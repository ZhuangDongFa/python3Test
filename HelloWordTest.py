#coding=utf-8
#x = "xxxxxxx"
"""
多行注释
"""
paragraph="""
这是一个段落,
我换行了
"""
print ("Hello World")
print ("输出多行字符"+\
    "a"+\
    "a")
print ("不换行输出2",)
print ("a")
print("不换行输出新方法3,", end="")
print ("a")
print(paragraph)

print("请输入您的名字")
my_name = input()
print("您的名字是："+my_name)

input("\n\n按下 enter 键后退出。")
