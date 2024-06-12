import numpy as np
import random
import matplotlib.pyplot as plt

# DE参数
F = 0.5
CR = 0.8
max_generation = 1000
bounds = [-10, 10]
dim = 2
n = 100


# 目标函数定义
def target_function_A(x):
    return pow(x[0], 2) + pow(x[1] - 2, 2)


def target_function_B(x):
    return pow(x[0] - 1, 2) + pow(x[1], 2)


# 初始化种群
populations_A = np.random.uniform(bounds[0], bounds[1], (n, dim))
populations_B = np.random.uniform(bounds[0], bounds[1], (n, dim))

fitness_A = np.array([target_function_A(ind) for ind in populations_A])
fitness_B = np.array([target_function_B(ind) for ind in populations_B])


def DE_algorithm(populations, fitness, target_function):
    for i in range(n):
        # 变异
        candidates = np.random.choice(range(n), 3, replace=False)
        a, b, c = populations[candidates[0]], populations[candidates[1]], populations[candidates[2]]
        mutation = a + F * (b - c)
        mutation = np.clip(mutation, bounds[0], bounds[1])
        # 交叉
        cross_mask = np.random.rand(dim) < CR
        if not np.any(cross_mask):
            cross_mask[np.random.randint(dim)] = True
        trial = np.copy(populations[i])
        trial[cross_mask] = mutation[cross_mask]
        # 选择
        trial_fitness = target_function(trial)
        if trial_fitness < fitness[i]:
            populations[i] = trial
            fitness[i] = trial_fitness


# 记录适应度历史
history_A = []
history_B = []

# 进化主循环
for gen in range(max_generation):
    DE_algorithm(populations_A, fitness_A, target_function_A)
    DE_algorithm(populations_B, fitness_B, target_function_B)

    # 任务间个体迁移
    migration_rate = 0.1
    num_migrate = int(n * migration_rate)
    migrate_indices = np.random.choice(range(n), num_migrate, replace=False)

    for idx in migrate_indices:
        if np.random.rand() < 0.5:  # 50%概率交换个体
            populations_A[idx], populations_B[idx] = populations_B[idx], populations_A[idx]
            fitness_A[idx], fitness_B[idx] = target_function_A(populations_A[idx]), target_function_B(
                populations_B[idx])

    best_fitness_A = np.min(fitness_A)
    best_solution_A = populations_A[np.argmin(fitness_A)]
    best_fitness_B = np.min(fitness_B)
    best_solution_B = populations_B[np.argmin(fitness_B)]

    history_A.append(best_fitness_A)
    history_B.append(best_fitness_B)

    print(f'gen:{gen + 1}, Task A - fitness:{best_fitness_A}, x:{best_solution_A}')
    print(f'gen:{gen + 1}, Task B - fitness:{best_fitness_B}, x:{best_solution_B}')

# 绘制结果
plt.plot(history_A, label='Task A')
plt.plot(history_B, label='Task B')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.xlim(0, 20)
plt.legend()
plt.show()
