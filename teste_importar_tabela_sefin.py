import requests
import pandas as pd



url_reducao = "https://legislacao.sefin.ro.gov.br/textoLegislacao.jsp?texto=183"
request = requests.get(url_reducao, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                                             "cookie":"_ga_N0KTEZ4FPC=GS1.1.1714997645.1.1.1714998021.0.0.0; _ga_JRREHRGTZL=GS1.1.1720887804.3.1.1720887820.0.0.0; _ga_9BTEGJ9GG8=GS1.1.1725893612.9.1.1725893616.0.0.0; _ga_Z06CD5Z2QX=GS1.1.1725893612.35.1.1725893619.0.0.0; _ga_SLDZF3GR58=GS1.1.1725893620.93.1.1725893670.0.0.0; _ga=GA1.4.1227731162.1565981696; JSESSIONID=91C40BFA56426B957EE06EE031269084",
                                             })
print(request.status_code)
print(request.content)
print(request.headers)
print(request.url)

#df = pd.read_xml(url_reducao)

#for tabela  in df:
#    print(tabela)