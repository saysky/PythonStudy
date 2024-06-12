import numpy as np
import matplotlib.pyplot as plt

# 生成标准正态分布数据
data = np.random.normal(0, 1, 1000)

# 绘制直方图
count, bins, ignored = plt.hist(data, 30, density=True, alpha=0.6, color='g')

# 绘制标准正态分布的概率密度函数
pdf = 1/(np.sqrt(2 * np.pi)) * np.exp(- bins**2 / 2)
plt.plot(bins, pdf, linewidth=2, color='r')
plt.title('标准正态分布（均值=0，方差=1）')
plt.show()
