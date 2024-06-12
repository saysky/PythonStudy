import matplotlib.pyplot as plt

# 假设 x1 和 x2 是随时间变化的两个参数
time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x1 = [10, 11, 13, 12, 14, 15, 16, 18, 17, 19, 20]
x2 = [5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10]

# 绘制 x1 和 x2 随时间变化的图形
plt.plot(time, x1, label='x1', marker='o')
plt.plot(time, x2, label='x2', marker='s')

# 添加图形标题和轴标签
plt.title('Parameters x1 and x2 over Time')
plt.xlabel('Time')
plt.ylabel('Values')

# 显示图例
plt.legend()

# 显示网格
plt.grid(True)

# 显示图形
plt.show()
