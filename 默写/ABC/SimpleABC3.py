import numpy as np
import matplotlib.pyplot as plt

# 定义常量
max_generations = 1000
num_employed_bees = 20
num_onlooker_bees = 20
limit = 1000
dim = 2

bounds = [-10, 10]

best_fitness_list = [0] * max_generations


def target_function(x):
    return pow(x[0], 2) + pow(x[1] - 2, 2)


# 初始化
populations = np.random.uniform(bounds[0], bounds[1], (num_employed_bees, dim))
fitness = np.array([target_function(item) for item in populations])
trail_count = np.zeros(num_employed_bees)


def employed_bee_phase(i):
    # 产生新解 Vi = Xi + (Xi - Xr1) * rand
    other_index = np.random.randint(num_employed_bees)
    while other_index == i:
        other_index = np.random.randint(num_employed_bees)
    dimension = np.random.randint(dim)
    new_solution = np.copy(populations[i])
    new_solution[dimension] = populations[i][dimension] + (
            populations[i][dimension] - populations[other_index][dimension]) * np.random.uniform(-1, 1)

    # 求适应度
    new_fitness = target_function(new_solution)

    # 选择更新
    if new_fitness < fitness[i]:
        populations[i] = new_solution
        fitness[i] = new_fitness
        trail_count[i] = 0
    else:
        trail_count[i] += 1


# 循环
for gen in range(max_generations):
    # 雇佣蜂阶段
    for i in range(num_employed_bees):
        employed_bee_phase(i)

    # 观察蜂阶段
    for i in range(num_employed_bees):
        roulette_wheel = np.cumsum((1 / fitness) / sum(1 / fitness))
        r = np.random.rand()
        select_index = np.where(roulette_wheel >= r)[0][0]
        employed_bee_phase(select_index)

    # 侦查蜂阶段
    for i in range(num_employed_bees):
        if trail_count[i] >= limit:
            populations[i] = np.random.uniform(bounds[0], bounds[1], (dim,))
            fitness[i] = target_function(populations[i])
            trail_count[i] = 0
        pass
    pass

    best_fitness = np.min(fitness)
    best_index = np.argmin(fitness)
    best_solution = populations[best_index]
    print(f'gen:{gen}, fitness:{best_fitness}, x1:{best_solution[0]}, x2:{best_solution[1]}')
    best_fitness_list[gen] = best_fitness

x = range(max_generations)
y = best_fitness_list
plt.plot(x, y)
plt.xlim(1, 100)
plt.grid(True)
plt.show()
