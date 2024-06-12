import matplotlib.pyplot as plt
import numpy as np

# 生成示例数据
x = np.arange(1, 1001)  # x轴范围从1到1000
y = np.random.rand(1000) * 100  # 生成1000个随机y值

# 绘制折线图
plt.plot(x, y, marker='o', linestyle='-', color='b', markersize=2)
plt.title('Line Chart with X-axis from 1 to 1000')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)

# 设置x轴范围
plt.xlim(1, 1000)

# 显示图形
plt.show()
