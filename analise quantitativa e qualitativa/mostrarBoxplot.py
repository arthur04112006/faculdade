import matplotlib.pyplot as plt 

valores = [403, 363, 381, 367, 341, 317, 401, 384, 342, 377, 329, 377, 349]

plt.boxplot(valores)
plt.title("Boxplot - Detecçao de Outliers")
plt.ylabel("Valores")
plt.grid(True)
plt.show()