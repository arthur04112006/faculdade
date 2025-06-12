import matplotlib.pyplot as plt 

x/y = [403, 363, 381, 367, 341, 317, 401, 384, 342, 377, 329, 377, 349]

plt.boxplot(x/y)
plt.title("Boxplot - Detecçao de Outliers")
plt.ylabel("x/y")
plt.grid(True)
plt.show()