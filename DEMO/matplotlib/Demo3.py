import matplotlib.pyplot as plt

# 生成一些示例数据
data = [10, 15, 7, 10, 25, 18]

# 折线图
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(data, marker='o', linestyle='-', color='b')
plt.title('Line Chart')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)

# 柱状图
plt.subplot(1, 3, 2)
plt.bar(range(len(data)), data, color='g')
plt.title('Bar Chart')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)

# 圆饼图
plt.subplot(1, 3, 3)
plt.pie(data, labels=[f'Part {i}' for i in range(len(data))], autopct='%1.1f%%')
plt.title('Pie Chart')

# 显示图形
plt.tight_layout()
plt.show()
