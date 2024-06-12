import random

# 生成0.0到1.0之间的随机浮点数
print("random.random():", random.random())

# 生成1到10之间的随机整数
print("random.randint(1, 10):", random.randint(1, 2))

# 生成1.5到10.5之间的随机浮点数
print("random.uniform(1.5, 10.5):", random.uniform(1.5, 10.5))

# 从列表中随机选择一个元素
choices = ['apple', 'banana', 'cherry']
print("random.choice(choices):", random.choice(choices))

# 从列表中随机选择3个元素
numbers = list(range(10))
print("random.sample(numbers, 3):", random.sample(numbers, 3))

# 打乱列表顺序
random.shuffle(numbers)
print("random.shuffle(numbers):", numbers)

# 生成符合高斯分布的随机数
print("random.gauss(0, 1):", random.gauss(0, 1))

print(random.randint(1, 2))
print(random.randint(1, 2))
print(random.randint(1, 2))
print(random.randint(1, 2))

print(random.choice(['aaa', 'bbb', 'ccc']))
print(random.choice(['aaa', 'bbb', 'ccc']))
print(random.choice(['aaa', 'bbb', 'ccc']))
print(random.choice(['aaa', 'bbb', 'ccc']))
print(random.sample([1, 2, 3, 4], 3))
print(random.sample(range(100), 3))

for i in range(100):
    print(random.gauss(0, 1))


