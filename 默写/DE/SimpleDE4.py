import numpy as np

# 定义常量
CR = 0.8
F = 0.5
max_generations = 1000
n = 100
dim = 2
bounds = [-10, 10]


def target_function(x):
    return pow(x[0], 2) + pow(x[1] - 2, 2)


# 初始化
populations = np.random.uniform(bounds[0], bounds[1], (n, dim))
fitness = np.array([target_function(item) for item in populations])

# 循环
for gen in range(max_generations):
    for i in range(n):
        # 交叉
        candidates = np.random.choice(range(n), 3)
        a, b, c = populations[candidates[0]], populations[candidates[1]], populations[candidates[2]]
        mutation = a + F * (b - c)

        # 变异
        cross_points = np.random.randint(0, dim)
        cross_mask = np.random.rand(dim) < CR
        if not any(cross_mask):
            cross_mask[cross_points] = True
        trail = np.copy(populations[i])
        trail[cross_mask] = mutation[cross_mask]

        # 选择
        trail_fitness = target_function(trail)
        if trail_fitness < fitness[i]:
            populations[i] = trail
            fitness[i] = trail_fitness

    best_fitness = np.min(fitness)
    best_index = np.argmin(fitness)
    best_solution = populations[best_index]
    print(f'gen:{gen}, fitness:{best_fitness}, x1:{best_solution[0]}, x2:{best_solution[1]}')

