from deap import base, creator, tools
import random

IND_SIZE = 5
creator.create('FitnessMin', base.Fitness, weights=(-1.0,))  # 优化目标：单变量，求最小值
creator.create('Individual', list, fitness=creator.FitnessMin)  # 创建Individual 类，继承 list

toolbox = base.Toolbox()

# random.random 进行实数编码
toolbox.register('Attr_float', random.random)
toolbox.register('Individual', tools.initRepeat, creator.Individual, toolbox.Attr_float, n=IND_SIZE)

ind1 = toolbox.Individual()
print(ind1)

# 结果：[0.8579615693371493, 0.05774821674048369, 0.8812411734389638, 0.5854279538236896, 0.12908399219828248]
