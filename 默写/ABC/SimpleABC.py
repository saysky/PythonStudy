import numpy as np

# 定义常量
max_generations = 1000
limit = 1000
dim = 2
num_employed_bees = 20
num_onlooker_bees = 20
bounds = [-10, 10]


def target_function(x):
    return pow(x[0], 2) + pow(x[1] - 2, 2)


def employed_bee_phase(select_index):
    # 产生新解
    other_index = np.random.randint(0, num_employed_bees)
    while other_index == select_index:
        other_index = np.random.randint(0, num_employed_bees)
    dimension = np.random.randint(0, dim)
    new_solution = np.copy(populations[i])
    new_solution[dimension] = populations[i][dimension] + (
            populations[i][dimension] - populations[other_index][dimension]) * (np.random.uniform(-1, 1))

    # 检查边界
    new_solution = np.clip(new_solution, bounds[0], bounds[1])

    # 求适应度
    new_fitness = target_function(new_solution)

    # 选择更新
    if new_fitness < fitness[i]:
        fitness[i] = new_fitness
        populations[i] = new_solution
        trail_count[i] = 0
    else:
        trail_count[i] += 1


# 初始化
populations = np.random.uniform(bounds[0], bounds[1], (num_employed_bees, dim))
fitness = np.array([target_function(item) for item in populations])
trail_count = np.zeros(num_employed_bees)

# 循环
for gen in range(max_generations):
    # 雇佣蜂阶段
    for i in range(num_employed_bees):
        # 开采
        employed_bee_phase(i)

    # 观察蜂阶段
    for i in range(num_onlooker_bees):
        roulette_wheel = np.cumsum((1 / fitness) / sum(1 / fitness))
        r = np.random.rand()
        indices = np.where(roulette_wheel >= r)
        select_index = indices[0][0]
        # 开采
        employed_bee_phase(select_index)

    # 侦查蜂阶段
    for i in range(num_employed_bees):
        if trail_count[i] >= limit:
            trail_count[i] = 0
            populations[i] = np.random.uniform(bounds[0], bounds[1], (1, dim))
            fitness[i] = target_function(populations[i])

    best_fitness = np.min(fitness)
    best_index = np.argmin(fitness)
    best_solution = populations[best_index]
    print(f'gen:{gen}, best_fitness:{best_fitness}, x1:{best_solution[0]}, x2:{best_solution[1]}')
