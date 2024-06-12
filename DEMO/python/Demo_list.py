# 1. 创建列表
empty_list = []
nums1 = [1, 2, 3, 4, 5]
nums2 = ["apple", "banana", "cherry"]
nums3 = [1, "apple", 3.14, True]

# 2. 访问列表元素
print(nums1[0])
print(nums1[1])
print(nums1[-1])
print(nums1[-2])

# 3. 列表切片
nums1 = [10, 20, 30, 40, 50]
print(nums1[1:3])  # 取第[1,3)区间元素
print(nums1[1:-1])  # 取第[1,-1)区间元素

print(nums1[:3])  # 取第[0,3)区间元素
print(nums1[2:])  # 取第[2,n)区间元素

print(nums1[::2])  # 步长为2
print(nums1[::3])  # 步长为3
print(nums1[::-1])  # 反转列表

# 4. 修改列表元素
nums1[0] = 1
nums1[1:3] = [100, 200]
print(nums1)

# 5. 添加元素
nums1.append(700)  # 末尾插入
nums1.extend([800, 900])  # 末尾插入
nums1.insert(2, 200)  # 在索引2处插入200

# 6. 删除元素
nums1.remove(200)  # 删除第一个200
print(nums1)
nums1.pop(2)  # 删除索引2处元素
print(nums1)
nums1.pop()
print(nums1)
# nums1.clear()
print(nums1)

# 7. 查找元素
x = 1000
if x in nums1:
    print(nums1.index(x))
else:
    print(f"{x}不存在")

# 8. 列表长度
print(len(nums1))

# 9. 列表排序
nums1.sort()
nums1.reverse()

# 10. 列表推导
new_nums1 = [item ** 2 for item in nums1 if item > 10]
new_nums1 = [nums1[i] ** 2 for i in range(1, 5) if i > 2]
new_nums1 = [nums1[i] ** 2 for i in range(5) if i > 2]
print(new_nums1)

# 11. 复制列表
nums1_copy1 = list(nums1)
nums1_copy2 = nums1.copy()

# 12. 合并列表
nums1_merge = nums1 + nums2
nums1.extend(nums2)

# 13. 遍历
nums1 = [10, 20, 30, 40]
for item in nums1:
    print(item)  # 换行遍历

for item in nums1:
    print(item, end=' ')  # 单行空格遍历

for index, value in enumerate(nums1):
    print(f"{index}: {value}")

# 14. 列表转字符串
# 先将int[] 转成 str[]
str1 = " ".join([str(item) for item in nums1])
print(str1)

# 15. 字符串转列表
str2 = "apple, banana, cherry"
nums2 = str2.split(", ")

nums1 = [10, 10, 20, 10]
print(nums1.count(10))
