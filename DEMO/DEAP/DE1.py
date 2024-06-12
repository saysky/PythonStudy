import numpy as np
import random
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms

# DE参数
F = 0.5
CR = 0.8
max_generation = 1000
bounds = [-10, 10]
dim = 2
n = 100

# 定义适应度和个体类型
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", np.ndarray, fitness=creator.FitnessMin)


# 定义目标函数
def target_function(individual):
    x = individual
    return pow(x[0], 2) + pow(x[1] - 2, 2),


# 初始化工具箱
toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, bounds[0], bounds[1])
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=dim)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", target_function)
toolbox.register("select", tools.selBest)


# DE变异操作
def de_mutation(individual, population, F):
    a, b, c = random.sample(population, 3)
    mutant = creator.Individual(a + F * (b - c))
    for i in range(len(mutant)):
        if mutant[i] < bounds[0]:
            mutant[i] = bounds[0]
        elif mutant[i] > bounds[1]:
            mutant[i] = bounds[1]
    return mutant


# DE交叉操作
def de_crossover(mutant, target, CR):
    trial = creator.Individual(target)
    for i in range(len(mutant)):
        if random.random() < CR:
            trial[i] = mutant[i]
    return trial


toolbox.register("mutate_de", de_mutation, F=F)
toolbox.register("crossover_de", de_crossover, CR=CR)

# 初始化种群
pop = toolbox.population(n=n)

# 评估初始种群
fitnesses = list(map(toolbox.evaluate, pop))
for ind, fit in zip(pop, fitnesses):
    ind.fitness.values = fit

# 进化主循环
for gen in range(max_generation):
    for i in range(len(pop)):
        target = pop[i]
        mutant = toolbox.mutate_de(target, pop)
        trial = toolbox.crossover_de(mutant, target)
        trial.fitness.values = toolbox.evaluate(trial)

        if trial.fitness.values < target.fitness.values:
            pop[i] = trial

    best_ind = tools.selBest(pop, 1)[0]
    print(f'gen:{gen + 1}, fitness:{best_ind.fitness.values[0]}, x1:{best_ind[0]}, x2:{best_ind[1]}')

# 绘制结果（可选）
best_fitness = best_ind.fitness.values[0]
best_solution = best_ind

print(f'Final best fitness: {best_fitness}')
print(f'Final best solution: x1={best_solution[0]}, x2={best_solution[1]}')
