import pandas as pd
import numpy as np
from math import ceil

populacao = 150
amostra = 15
k = ceil(populacao/amostra)

r = np.random.randint(low = 1, high = k+1, size = 1)

acumulador = r[0]
sorteados = []
print(k)
for i in range (amostra):
    sorteados.append(acumulador)
    acumulador = acumulador + k
    # print(sorteados)
base = pd.read_csv('iris.csv')
base_final = base.loc[sorteados]
print(base_final)