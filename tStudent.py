from scipy.stats import t

## u = 75, X = 80, dp = 10

## Qual a prob de selecionar um cientista com salario menor que 80/h?
prob = t.cdf(1.5, 8)

## Qual a prob de selecionar um cientista com salario maior que 80/h?
prob2 = t.sf(1.5, 8)

print(prob)
print(prob2)