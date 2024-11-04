from pathlib import Path
import random
import pandas as pd
import math
import itertools

arquivo = Path().absolute() / "planilha" / "NF-Positec.ods"

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
print(dados)
total = dados['Valor produtos'] = dados['Valor produtos'].astype(float)
# total_com_frete = dados['Total + Frete'] = dados['Total + Frete'].astype(float)
lista_números = total.dropna().tolist()

print(lista_números)

# alvo = float(10662.8)
# alvo = float(1286.39)
# alvo = float(593.83)
alvo = float(4135.29)

margem_erro = float(0.01)

print("Rodando o programa. Aguarde alguns minutos, por favor!\n ....")
encontrar_combinação(lista_números, alvo, margem_erro)

print("Fim!")




