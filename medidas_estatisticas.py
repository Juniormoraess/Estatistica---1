import numpy as np
from scipy import stats

players = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]

media = np.mean(players)
mediana = np.median(players)
quartis = np.quantile(players, [0, 0.25, 0.5, 0.75, 1])
desvioPadrao1 = np.std(players) ## Desvio padrão para população
desvioPadrao2 = np.std(players, ddof = 1) ## Desvio padrão para amostra

print()
print(media)
print(mediana)
print(quartis)
print(desvioPadrao1)
print(desvioPadrao2)
print()

estatisticas = stats.describe(players)
print(estatisticas)