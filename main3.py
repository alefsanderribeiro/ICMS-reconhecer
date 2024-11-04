# TODO Reconhecer ICMS Substituição
# Pegar os dados no eficiência do valor total da NF que estão cobrando Subistituição, com o cód. receita 1231. 
# Após pegar o valor cobrado da Substituição, pegar o frete e verificar se é FOB. 
# Se for FOB, será somado junto e distribuido proporcionalmente em cada item.
# Após, isso, fazer a combinação de cada item


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
    valor_total_frete = 23.41
    
    arquivo = Path().absolute() / "planilha" / "NF-Bramais.ods"

    dados = pd.read_excel(arquivo, header=6, dtype=str).drop(columns="Unnamed: 0").dropna(subset=['Produto'])

    # Convertendo a coluna 'Valor produtos' para float
    dados['Valor produtos'] = dados['Valor produtos'].astype(float)
    
    # Calculando o valor total dos produtos
    valor_total_produtos = dados['Valor produtos'].sum()
    
    # Calculando o frete proporcional para cada item
    dados['Frete proporcional'] = dados['Valor produtos'] / valor_total_produtos * valor_total_frete
    
    # Calculando o total com frete para cada item
    dados['Total + Frete'] = dados['Valor produtos'] + dados['Frete proporcional']
    
    # Atualizando a lista de números para usar os valores com frete
    lista_números = dados['Total + Frete'].dropna().tolist()
    
    #print(dados[['Produto','Valor produtos', 'Frete proporcional', 'Total + Frete']])

    #alvo = float(20442.03)

    alvo = float(686.50)
    #alvo = float(2667.16)

    margem_erro = float(0.01)

    print("Rodando o programa. Aguarde alguns minutos, por favor!")

    encontrar_combinação(lista_números, alvo, margem_erro)


    print("Fim!")
