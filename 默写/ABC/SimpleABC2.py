import numpy as np

# 定义常量
max_generations = 1000
limit = 1000
num_employed_bee = 20
num_onlooker_bee = 20
dim = 2
bounds = [-10, 10]


def target_function(x):
    return pow(x[0], 2) + pow(x[1] - 2, 2)


# 初始化
populations = np.random.unifrom(bounds[0], bounds[1], (num_employed_bee, dim))
fitness = np.array([target_function(populations[item]) for item in populations])
trail_count = np.zeros(num_employed_bee)


def employed_bee_phase(i):
    # 产生新解
    other_index = np.random.randint(num_employed_bee)
    while other_index == i:
        other_index = np.random.randint(num_employed_bee)
    dimension = np.random.randint(dim)
    new_solution = np.copy(populations[i])
    new_solution[dimension] = populations[i][dimension] + (
            populations[i][dimension] - populations[other_index][dimension]) * np.random.uniform(-1, 1)
    new_solution = np.clip(new_solution, bounds[0], bounds[1])

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
    for i in range(num_employed_bee):
        employed_bee_phase(i)

    # 观察蜂阶段
    for i in range(num_onlooker_bee):
        roulette_wheel = np.cumsum((1 / fitness) / sum(1 / fitness))
        select_index = np.where(roulette_wheel >= np.random.rand())[0][0]
        employed_bee_phase(select_index)
        pass

    # 雇佣蜂阶段
    for i in range(num_employed_bee):
        if trail_count(i) >= limit:
            populations[i] = np.random.uniform(bounds[0], bounds[1], (dim,))
            fitness[i] = target_function(populations[i])
            trail_count[i] = 0

    best_fitness = np.min(fitness)
    best_index = np.argmin(fitness)
    best_solution = populations[best_index]
    print(f'gen:{gen}, fitness:{best_fitness}, x1:{best_solution[0]}, x2:{best_solution[1]} ')
