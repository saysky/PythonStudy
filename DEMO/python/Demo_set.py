set2 = {"apple", "banana", "cherry", 'apple'}
fruits = set(["apple", "banana", "cherry"])
chars = set("abcd")
chars2 = set(['hello'])
print(set2)
print(fruits)
print(chars)
print(chars2)

set2.add('china')
set2.update(['a', 'b'])


print(set2)

fruit = fruits.pop()  # 随机删除并返回一个元素

a = {1,2,3}
b = {3, 4, 5}
c = a.union(b)
d = a | b
print(a)
print(b)
print(c)
print(d)

print(a & b)
print(a.intersection())

print(a - b )

print(a ^ b)

a = {1, 2, 3}
b = {1, 3, 2}

c = set((1, 2, 3))

c.add(1000)

print(a)
print(c)