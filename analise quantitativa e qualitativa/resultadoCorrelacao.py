from scipy.stats import pearsonr

x = [60, 75, 62, 68, 84, 97, 66, 65, 86, 78, 93, 75, 88]
y = [403, 363, 381, 367, 341, 317, 401, 384, 342, 377, 329, 377, 349]

# pearsonr retorna (correlação, p-valor)
correlacao, p_valor = pearsonr(x, y)  

print(f"Correlação de Pearson: {correlacao:.3f}")