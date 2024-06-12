import numpy as np
import matplotlib.pyplot as plt

# 定义常量
n = 100
dim = 2
max_generations = 1000
bounds = [-10, 10]
CR = 0.8
F = 0.5
best_fitness_list = [0] * max_generations


# 目标函数
def target_function(x):
    return pow(x[0], 2) + pow(x[1] - 2, 2)


# 初始化
populations = np.random.uniform(bounds[0], bounds[1], (n, dim))
fitness = np.array([target_function(item) for item in populations])

# 循环
for gen in range(max_generations):
    for i in range(n):
        # 变异 vi = xr1 + F * (xr2 - xr3)
        candidates = np.random.choice(range(n), 3)
        a, b, c = populations[candidates[0]], populations[candidates[1]], populations[candidates[2]]
        mutation = a + F * (b - c)

        # 交叉
        cross_mask = np.random.rand(dim) < CR
        if not any(cross_mask):
            cross_points = np.random.randint(dim)
            cross_mask[cross_points] = True
        trail = np.copy(populations[i])
        trail[cross_mask] = mutation[cross_mask]

        # 选择
        trail_fitness = target_function(trail)
        if trail_fitness < fitness[i]:
            populations[i] = trail
            fitness[i] = trail_fitness

    # 求最优解
    best_fitness = np.min(fitness)
    best_index = np.argmin(fitness)
    best_solution = populations[best_index]
    print(f'gen{gen}, fitness:{best_fitness}, x1:{best_solution[0]}, x2:{best_solution[1]}')
    best_fitness_list[gen] = best_fitness


# 绘制折线图
x = range(max_generations)
y = best_fitness_list
plt.plot(x, y, marker='o', linestyle='-', color='b', markersize=2)
plt.title('Line Chart with X-axis from 1 to 1000')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)

# 设置x轴范围
plt.xlim(1, 50)

# 显示图形
plt.show()