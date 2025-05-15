import matplotlib.pyplot as plt 

x = [60, 75, 62, 68, 84, 97, 66, 65, 86, 78, 93, 75, 88]
y = [403, 363, 381, 367, 341, 317, 401, 384, 342, 377, 329, 377, 349]

plt.scatter(x, y, color='blue')
plt.title("grafico de dispersao - possivel outlier")
plt.xlabel("x")
plt.xlabel("y")
plt.grid(True)
plt.show()