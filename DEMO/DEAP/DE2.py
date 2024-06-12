#    This file is part of EAP.
#
#    EAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    EAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with EAP. If not, see <http://www.gnu.org/licenses/>.

import random
import array

import numpy

from deap import base
from deap import benchmarks
from deap import creator
from deap import tools

# Problem dimension
NDIM = 10

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -3, 3)  # 随机生成
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, NDIM)  # 初始化个体
toolbox.register("population", tools.initRepeat, list, toolbox.individual)  # 初始化种群
toolbox.register("select", tools.selRandom, k=3)  # 选择3个个体参与交叉
toolbox.register("evaluate", benchmarks.sphere)  # 目标函数，求解最小值


def main():
    # Differential evolution parameters
    CR = 0.25
    F = 1
    POPULATION_SIZE = 300  # Number of individuals to select for the next generation
    MAX_GENERATIONS = 200  # Number of generations

    pop = toolbox.population(n=POPULATION_SIZE);
    hof = tools.HallOfFame(1)  # 仅仅记录最优个体
    stats = tools.Statistics(lambda ind: ind.fitness.values)  # 统计种群的统计信息
    stats.register("avg", numpy.mean)  # 计算平均值
    stats.register("std", numpy.std)  # 计算标准差
    stats.register("min", numpy.min)  # 计算最小值
    stats.register("max", numpy.max)  # 计算最大值

    logbook = tools.Logbook()  # 记录日志
    logbook.header = "gen", "evals", "std", "min", "avg", "max"  # 日志头部

    # Evaluate the individuals
    fitnesses = toolbox.map(toolbox.evaluate, pop) # 计算个体的适应度
    for ind, fit in zip(pop, fitnesses): # 将适应度赋值给个体
        ind.fitness.values = fit

    record = stats.compile(pop) # 记录统计信息
    logbook.record(gen=0, evals=len(pop), **record) # 记录日志
    print(logbook.stream) # 打印日志

    for g in range(1, MAX_GENERATIONS):
        for k, agent in enumerate(pop):
            a, b, c = toolbox.select(pop)
            y = toolbox.clone(agent)
            index = random.randrange(NDIM)
            for i, value in enumerate(agent):
                if i == index or random.random() < CR:
                    y[i] = a[i] + F * (b[i] - c[i])
            y.fitness.values = toolbox.evaluate(y)
            if y.fitness > agent.fitness:
                pop[k] = y
        hof.update(pop)
        record = stats.compile(pop)
        logbook.record(gen=g, evals=len(pop), **record)
        print(logbook.stream)

    print("Best individual is ", hof[0], hof[0].fitness.values[0])


if __name__ == "__main__":
    main()
