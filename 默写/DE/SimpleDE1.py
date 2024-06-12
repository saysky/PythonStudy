# 定义常量
import numpy as np

n = 100
dim = 2
bounds = [-10, 10]
CR = 0.8
F = 0.5
max_generations = 1000

def target_function(x):
    # f(x1, x2) = x1 ^ 2 + (x2 - 2) ^ 2
    return pow(x[0], 2) + pow((x[1] - 2), 2)


# 初始化
populations = np.random.uniform(-10, 10, (n, dim))
fitness = [target_function(item) for item in populations]

# 开始循环
for gen in range(max_generations):
    for i in range(n):
        # 变异
        candidates = np.random.choice(range(n), 3, replace=False) # 注意， replace=False不可重复很重要
        # a = populations[candidates[0]]
        # b = populations[candidates[1]]
        # c = populations[candidates[2]]
        a, b, c = populations[candidates]

        # mutation = a + F * (b - c)
        # mutation = np.clip(mutation, bounds[0], bounds[1])
        mutation = np.clip(a + F * (b - c), bounds[0], bounds[1])

        # 交叉
        cross_mask = np.random.rand(dim) < CR
        cross_points = np.random.randint(0, dim)
        if not np.any(cross_mask):
            cross_mask[cross_points] = True

        trail = np.copy(populations[i])  # 注意， copy()很重要，否则会污染populations
        trail[cross_mask] = mutation[cross_mask]

        # 选择
        trail_fitness = target_function(trail)
        if trail_fitness < fitness[i]:
            fitness[i] = trail_fitness
            populations[i] = trail

    # best_fitness = min(fitness)
    # best_index = fitness.index(best_fitness)
    # best_solution = populations[best_index]
    best_fitness = np.min(fitness)
    best_index = np.argmin(best_fitness)
    best_solution = populations[best_index]
    print(f"gen:{gen}, best_fitness:{best_fitness}, x1:{best_solution[0]}, x2:{best_solution[1]}")
