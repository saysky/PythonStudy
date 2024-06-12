import matplotlib.pyplot as plt

# 生成一些示例数据
time = list(range(10))  # 时间序列 [0, 1, 2, ..., 9]
x1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # 示例数据 x1
x2 = [5, 6, 4, 7, 8, 6, 9, 10, 7, 8]   # 示例数据 x2

# 绘制散点图
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(x1, x2, color='blue', marker='o')
plt.title('Scatter Plot of x1 vs x2')
plt.xlabel('x1')
plt.ylabel('x2')
plt.grid(True)

# 绘制线图
plt.subplot(1, 2, 2)
plt.plot(time, x1, label='x1', marker='o', color='green')
plt.plot(time, x2, label='x2', marker='s', color='red')
plt.title('Line Plot of x1 and x2 over Time')
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend()
plt.grid(True)

# 显示图形
plt.tight_layout()
plt.show()
