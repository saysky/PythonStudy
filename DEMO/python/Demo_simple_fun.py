# 数据类型转换
a = int("123")  # 转换为整数
b = float("123.45")  # 转换为浮点数
c = str(123)  # 转换为字符串

# 数学函数
print(abs(-5))  # 输出: 5
print(max([1, 2, 3]))  # 输出: 3
print(min([1, 2, 3]))  # 输出: 1
print(sum([1, 2, 3]))  # 输出: 6
print(round(3.14159, 2))  # 输出: 3.14

# 字符串处理
s = "Hello, Python!"
print(s.lower())  # 输出: hello, python!
print(s.upper())  # 输出: HELLO, PYTHON!
print(s.split())  # 输出: ['Hello,', 'Python!']
print("-".join(["Hello", "Python"]))  # 输出: Hello-Python

# 输入输出
# name = input("Enter your name: ")
# print("Hello, " + name)

# 文件操作
# with open("example.txt", "w") as file:
#     file.write("Hello, World!")

# 高阶函数
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))  # 输出: [1, 4, 9, 16, 25]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # 输出: [2, 4]

# 其他常用函数
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)  # 输出: (0, 'a'), (1, 'b'), (2, 'c')

zipped = list(zip([1, 2, 3], ['a', 'b', 'c']))  # 输出: [(1, 'a'), (2, 'b'), (3, 'c')]

print(any([False, True, False]))  # 输出: True
print(all([True, True, True]))  # 输出: True

sorted_list = sorted([3, 1, 2])  # 输出: [1, 2, 3]
reversed_list = list(reversed([1, 2, 3]))  # 输出: [3, 2, 1]
