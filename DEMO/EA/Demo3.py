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

# 定义个体和适应度
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", np.ndarray, fitness=creator.FitnessMin)


# 定义目标函数
def target_function_A(individual):
    x = individual
    return pow(x[0], 2) + pow(x[1] - 2, 2),


def target_function_B(individual):
    x = individual
    return pow(x[0] - 1, 2) + pow(x[1], 2),


# 初始化工具箱
toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, bounds[0], bounds[1])
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=dim)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxUniform)
toolbox.register("mutate", tools.mutPolynomialBounded, low=bounds[0], up=bounds[1], eta=20.0, indpb=1.0 / dim)
toolbox.register("select", tools.selTournament, tournsize=3)

# 定义评估函数
toolbox.register("evaluate_A", target_function_A)
toolbox.register("evaluate_B", target_function_B)


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


# 进化主循环
def evolutionary_multi_task_optimization(pop_size, generations):
    pop_A = toolbox.population(n=pop_size // 2)
    pop_B = toolbox.population(n=pop_size // 2)

    history_A = []
    history_B = []

    for gen in range(generations):
        # 评估任务A的个体
        fitnesses = list(map(toolbox.evaluate_A, pop_A))
        for ind, fit in zip(pop_A, fitnesses):
            ind.fitness.values = fit

        # 评估任务B的个体
        fitnesses = list(map(toolbox.evaluate_B, pop_B))
        for ind, fit in zip(pop_B, fitnesses):
            ind.fitness.values = fit

        # 变异和交叉操作
        for pop, eval_func in [(pop_A, toolbox.evaluate_A), (pop_B, toolbox.evaluate_B)]:
            for i in range(len(pop)):
                target = pop[i]
                mutant = toolbox.mutate_de(target, pop)
                trial = toolbox.crossover_de(mutant, target)
                trial.fitness.values = eval_func(trial)

                if trial.fitness.values < target.fitness.values:
                    pop[i] = trial

        # 任务间个体迁移
        migration_rate = 0.1
        num_migrate = int(pop_size * migration_rate / 2)
        migrate_indices = random.sample(range(pop_size // 2), num_migrate)

        for idx in migrate_indices:
            if random.random() < 0.5:  # 50%概率交换个体
                pop_A[idx], pop_B[idx] = pop_B[idx], pop_A[idx]
                pop_A[idx].fitness.values = toolbox.evaluate_A(pop_A[idx])
                pop_B[idx].fitness.values = toolbox.evaluate_B(pop_B[idx])

        best_ind_A = tools.selBest(pop_A, 1)[0]
        best_ind_B = tools.selBest(pop_B, 1)[0]

        history_A.append(best_ind_A.fitness.values[0])
        history_B.append(best_ind_B.fitness.values[0])

        print(f'gen:{gen + 1}, Task A - fitness:{best_ind_A.fitness.values[0]}, x:{best_ind_A}')
        print(f'gen:{gen + 1}, Task B - fitness:{best_ind_B.fitness.values[0]}, x:{best_ind_B}')

    return history_A, history_B


# 参数设置
pop_size = 100
generations = 50

# 运行进化多任务优化算法
history_A, history_B = evolutionary_multi_task_optimization(pop_size, generations)

# 绘制结果
plt.plot(history_A, label='Task A')
plt.plot(history_B, label='Task B')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.legend()
plt.show()
