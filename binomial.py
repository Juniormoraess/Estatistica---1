from scipy.stats import binom
## Probabilidade não acumulativa
probMoeda = (binom.pmf(3, 5, 0.5)) * 100
probProva = (binom.pmf(7, 10, 0.20)) * 100
probSinal = (binom.pmf(4, 4, 0.25)) * 100
probEnem = (binom.pmf(30, 45, 0.20)) * 100

print()
print(probMoeda)
print(probProva)
print(probSinal)
print(probEnem)
print()

## Probabilidade acumulativa
probSinalCumulativo = (binom.cdf(3, 4, 0.25)) * 100
print(probSinalCumulativo)
print()