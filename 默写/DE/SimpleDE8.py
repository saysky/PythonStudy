# 定义常量
import numpy as np

F = 0.5
CR = 0.8
max_generation = 1000
bounds = [-10, 10]
dim = 2
n = 100


def target_function(x):
    return pow(x[0], 2) + pow(x[1] - 2, 2)


# 初始化
populations = np.random.uniform(bounds[0], bounds[1], (n, dim))
fitness = np.array([target_function(item) for item in populations])

# 循环
for gen in range(max_generation):
    for i in range(n):
        # 变异
        candidates = np.random.choice(range(n), 3)
        a, b, c = populations[candidates[0]], populations[candidates[1]], populations[candidates[2]]
        mutation = a + F * (b - c)
        mutation = np.clip(mutation, bounds[0], bounds[1])
        # 交叉
        cross_mask = np.random.rand(dim) < CR
        if not any(cross_mask):
            cross_mask[np.random.randint(dim)] = True
        trail = np.copy(populations[i])
        trail[cross_mask] = mutation[cross_mask]

        # 选择
        trail_fitness = target_function(trail)
        if trail_fitness < fitness[i]:
            populations[i] = trail
            fitness[i] = trail_fitness
        pass

    best_fitness = np.min(fitness)
    best_solution = populations[np.argmin(fitness)]
    print(f'gen:{gen + 1}, fitness:{best_fitness}, x1:{best_solution[0]}, x2:{best_solution[1]}')
