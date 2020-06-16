from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt

## Gera dados de distribuição normal
data = norm.rvs(size = 100)

## Gera o grafico de verificação da distribuição normal
graph = stats.probplot(data, plot = plt)

## Faz o teste de shapiro para a verificação da distribuição normal
stats.shapiro(data)

plt.show()
