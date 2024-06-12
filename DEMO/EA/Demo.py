import numpy as np
import random
import matplotlib.pyplot as plt


# 定义个体和种群的基本结构
class Individual:
    def __init__(self, x):
        self.x = x
        self.fitness_A = None
        self.fitness_B = None

    def evaluate_A(self):
        self.fitness_A = self.x ** 2

    def evaluate_B(self):
        self.fitness_B = (self.x - 2) ** 2


# 生成初始种群
def generate_population(size, lower_bound, upper_bound):
    population = []
    for _ in range(size):
        x = np.random.uniform(lower_bound, upper_bound)
        individual = Individual(x)
        population.append(individual)
    return population


# 评估种群中的个体
def evaluate_population(population):
    for individual in population:
        individual.evaluate_A()
        individual.evaluate_B()


# 选择操作
def select(population, task):
    population.sort(key=lambda ind: ind.fitness_A if task == 'A' else ind.fitness_B)
    return population[:len(population) // 2]


# 交叉操作
def crossover(parent1, parent2):
    alpha = np.random.rand()
    child1 = Individual(alpha * parent1.x + (1 - alpha) * parent2.x)
    child2 = Individual(alpha * parent2.x + (1 - alpha) * parent1.x)
    return child1, child2


# 变异操作
def mutate(individual, lower_bound, upper_bound):
    if np.random.rand() < 0.1:
        individual.x = np.random.uniform(lower_bound, upper_bound)


# 任务间的个体迁移
def migrate(population_A, population_B, rate=0.1):
    num_migrate = int(len(population_A) * rate)
    migrants_A = random.sample(population_A, num_migrate)
    migrants_B = random.sample(population_B, num_migrate)
    for i in range(num_migrate):
        population_A[-(i + 1)] = migrants_B[i]
        population_B[-(i + 1)] = migrants_A[i]


# 进化算法主循环
def evolutionary_multi_task_optimization(pop_size, generations, lower_bound, upper_bound):
    population_A = generate_population(pop_size // 2, lower_bound, upper_bound)
    population_B = generate_population(pop_size // 2, lower_bound, upper_bound)
    history_A = []
    history_B = []

    for gen in range(generations):
        evaluate_population(population_A)
        evaluate_population(population_B)

        # 确保种群不为空
        if len(population_A) == 0 or len(population_B) == 0:
            break

        # 记录每代的最佳适应度
        best_individual_A = min(population_A, key=lambda ind: ind.fitness_A)
        best_individual_B = min(population_B, key=lambda ind: ind.fitness_B)
        history_A.append(best_individual_A.fitness_A)
        history_B.append(best_individual_B.fitness_B)

        # 选择阶段
        selected_A = select(population_A, 'A')
        selected_B = select(population_B, 'B')

        # 交叉和变异阶段
        new_population_A = []
        new_population_B = []

        for i in range(len(selected_A) // 2):
            parent1, parent2 = selected_A[i], selected_A[-i - 1]
            child1, child2 = crossover(parent1, parent2)
            mutate(child1, lower_bound, upper_bound)
            mutate(child2, lower_bound, upper_bound)
            new_population_A.extend([child1, child2])

        for i in range(len(selected_B) // 2):
            parent1, parent2 = selected_B[i], selected_B[-i - 1]
            child1, child2 = crossover(parent1, parent2)
            mutate(child1, lower_bound, upper_bound)
            mutate(child2, lower_bound, upper_bound)
            new_population_B.extend([child1, child2])

        # 任务间个体迁移
        migrate(new_population_A, new_population_B)

        population_A = new_population_A
        population_B = new_population_B

    return history_A, history_B


# 参数设置
pop_size = 100
generations = 50
lower_bound = -10
upper_bound = 10

# 运行进化多任务优化算法
history_A, history_B = evolutionary_multi_task_optimization(pop_size, generations, lower_bound, upper_bound)

# 绘制结果
plt.plot(history_A, label='Task A')
plt.plot(history_B, label='Task B')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.legend()
plt.show()
