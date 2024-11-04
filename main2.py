from pathlib import Path
import random
import pandas as pd
import math
import itertools

arquivo = Path().absolute() / "planilha" / "NF-Fame.ods"

def encontrar_combinação(lista, alvo, margem_erro):
    combinacao = []
    quant_verificado = 0
    for r in range(1, len(lista) + 1):
        for subset in itertools.combinations(lista, r):
            quant_verificado += 1
            valor = sum(subset)
            if  valor > (alvo - margem_erro) and valor < (alvo + margem_erro):
                combinacao = list(subset)
                print(combinacao)
                print(valor)

dados = pd.read_excel(arquivo, header=6, dtype=str).drop(columns="Unnamed: 0")
#mascara = dados2["NCM"].str.contains("32082019")
#dados = dados2[~mascara]
total = dados['Valor produtos'] = dados['Valor produtos'].astype(float)
#print(total)
#total_com_frete = dados['Total + Frete'] = dados['Total + Frete'].astype(float).round(2)
lista_numeros = total.dropna().tolist()


print(lista_numeros)

#print(lista)
alvo = float(529.47)
#alvo = float(4688.52)
#alvo = float(593.83)
#alvo = float(717.28)

margem_erro = float(0.01)

print("Rodando o programa. Aguarde alguns minutos, por favor!\n ....")
encontrar_combinação(lista_numeros, alvo, margem_erro)

print("Fim!")




