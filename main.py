import maritalk
from utils.search import *
import time
import pandas as pd


#https://python.langchain.com/docs/integrations/chat/maritalk/

#Para erros de conexão e https 
#https://stackoverflow.com/questions/51768496/why-do-https-requests-produce-ssl-certificate-verify-failed-error

#Editar aquivo venv\Lib\site-packages\requests\sessions.py; mudar verify = True para False


def get_response(input_text:str, userkey:str):
    model = maritalk.MariTalk(
        key=userkey,
        model="sabia-2-small"  # No momento, suportamos os modelos sabia-2-medium e sabia-2-small
    )

    response = model.generate(input_text)
    answer = response["answer"]
    return answer

#Ler key from txt file
def read_key():
    with open('key.txt', 'r') as file:
        key = file.read().replace('\n', '')
    return key

key = read_key()

tema = str(input("Qual o tema da sua pesquisa?:\n"))
# print(get_response("Qual é o seu nome?", key))
inicio = time.time()
docs=get_arxiv_docs(tema, 10)

#Para cada artigo, criar um dataframe com os metadados e o resumo
colunas = list(docs[0].metadata.keys()) + ['Summary']
#Criar dicionário onde cada chave é uma coluna e o valor é uma lista vazia
data = {coluna: [] for coluna in colunas}
#Remover "Summary" da lista de colunas
colunas.remove('Summary')

for doc in docs:
    data['Summary'].append(get_response(f"Resuma esse artigo em bullet points em português:\n {doc.page_content}", key))
    for coluna in colunas:
        data[coluna].append(doc.metadata[coluna])
data = pd.DataFrame(data)
data.to_excel('artigos.xlsx', index=False)
# print(docs[0].metadata)
# print(get_response(f"Resuma esse artigo em bullet points em português:\n {docs[0].page_content}", key))

print("Tempo de execução: ", time.time()-inicio)