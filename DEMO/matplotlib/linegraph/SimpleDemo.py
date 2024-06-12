import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [pow(x, 2) for x in x]
plt.plot(x, y)
plt.show()
