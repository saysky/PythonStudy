import random
import numpy as np
from deap import base, creator, tools

# 定义适应度和个体类型
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", np.ndarray, fitness=creator.FitnessMin)

# 初始化工具箱
toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -10, 10)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=2)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# 定义目标函数
def target_function(individual):
    x = individual[0]
    y = individual[1]
    return (x**2 + (y - 2)**2,)

toolbox.register("evaluate", target_function)

# 初始化种群
pop_size = 100
population = toolbox.population(n=pop_size)

# 评估初始种群
fitnesses = list(map(toolbox.evaluate, population))
for ind, fit in zip(population, fitnesses):
    ind.fitness.values = fit

# ABC参数
max_generation = 1000
limit = 100  # 忘记参数，用于控制弃用食物源
trials = np.zeros(pop_size)

def update_individual(ind, phi, partner):
    new_ind = creator.Individual(ind + phi * (ind - partner))
    return new_ind

# 进化主循环
for gen in range(max_generation):
    # 雇佣蜂阶段
    for i in range(pop_size):
        partner_idx = random.randint(0, pop_size - 1)
        while partner_idx == i:
            partner_idx = random.randint(0, pop_size - 1)
        phi = random.uniform(-1, 1)
        new_ind = update_individual(population[i], phi, population[partner_idx])
        new_ind.fitness.values = toolbox.evaluate(new_ind)
        if new_ind.fitness.values < population[i].fitness.values:
            population[i] = new_ind
            trials[i] = 0
        else:
            trials[i] += 1

    # 观察蜂阶段
    fitnesses = np.array([ind.fitness.values[0] for ind in population])
    probs = fitnesses / fitnesses.sum()
    for i in range(pop_size):
        if random.random() < probs[i]:
            partner_idx = random.randint(0, pop_size - 1)
            while partner_idx == i:
                partner_idx = random.randint(0, pop_size - 1)
            phi = random.uniform(-1, 1)
            new_ind = update_individual(population[i], phi, population[partner_idx])
            new_ind.fitness.values = toolbox.evaluate(new_ind)
            if new_ind.fitness.values < population[i].fitness.values:
                population[i] = new_ind
                trials[i] = 0
            else:
                trials[i] += 1

    # 侦查蜂阶段
    for i in range(pop_size):
        if trials[i] > limit:
            population[i] = toolbox.individual()
            population[i].fitness.values = toolbox.evaluate(population[i])
            trials[i] = 0

    best_ind = tools.selBest(population, 1)[0]
    print(f'gen:{gen + 1}, fitness:{best_ind.fitness.values[0]}, x:{best_ind}')

# 输出最终结果
print(f'Final best fitness: {best_ind.fitness.values[0]}')
print(f'Final best solution: {best_ind}')
