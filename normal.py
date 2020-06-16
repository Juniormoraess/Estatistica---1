from scipy.stats import norm

## Média = 8, dp = 2
## Qual a probabilidade do peso do objeto ser menor que 6kg?
probMenor = norm.cdf(1500, 1250, 480)

## Qual a probabilidade do peso do objeto ser maior que 6kg?
probMaior = norm.sf(6, 8, 2)

## Qual a probabilidade do peso do objeto ser menor que 6kg ou maior que 10kg?
probMM = norm.cdf(6, 8, 2) + norm.sf(10, 8, 2)

## Qual a probabilidade do peso do objeto ser menor que 10kg e maior que 8kg?
probMeM = norm.cdf(10, 8, 2) - norm.cdf(8, 8, 2)

print()
print(probMenor)
##print(probMaior)
##print(probMM)
##print(probMeM)
##print()