# TODO Reconhecer ICMS Redução
# Preciso ajustar esse código para buscar os dados da tabela 
# na SEFIN para poder veriricar se o NCM pode estar incluído para ser Redução
# Após isso, buscar os valores no eficiência onde tem os dados que não são redução.
# Por fim, deduzir o valor dos itens, com a sobra, será o valor que tenho que buscar da redução.
# Pegar esse valor e comparar com os itens do NCM e fazer combinação deles pra verificar se são redução mesmo.

from pathlib import Path
import random
import pandas as pd
import math
import itertools





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


def encontrar_combinação_random(lista, alvo):
    combinacao = []
    soma = 0
    tentativas = 0
    max_tentativas = math.factorial(len(lista))
    
    while (soma < (alvo - margem_erro) and soma > (alvo + margem_erro)) or tentativas < max_tentativas:
        
        combinacao = random.sample(lista, random.randint(1, len(lista)))
        soma = round(sum(combinacao),2)
        tentativas += 1
        
    localizacao = [lista.index(num) for num in combinacao]
    print(f"A quantidade de tentativas foram:: {tentativas}")
    print(f"O valor da soma é: {soma}")
    if tentativas == max_tentativas:
        print("Todas as combinações possíveis foram executadas")
        
        
    return combinacao, localizacao
    
if __name__ == "__main__":
        
    arquivo = Path().absolute() / "planilha" / "NF-Fertak.ods"
        
    dados = pd.read_excel(arquivo, header=6, dtype=str).drop(columns="Unnamed: 0").dropna(subset=['Produto'])
    
    dados['Valor produtos'] = dados['Valor produtos'].astype(float)

    lista_números = dados['Valor produtos'].dropna().tolist()


    #lista_numeros = [55.2, 965, 93.6, 235.2, 140.88, 739.2, 305, 772.8, 312.48, 92.4, 393.12, 139.44, 561.12]

    #alvo = float(20442.03)

    alvo = 10658.86
    print(f"alvo: {alvo}")

    margem_erro = float(0.01)

    print("Rodando o programa. Aguarde alguns minutos, por favor!")

    encontrar_combinação(lista_números, alvo, margem_erro)


    print("Fim!")
