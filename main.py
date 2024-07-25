import maritalk
from utils.llm import *
from utils.utils import *
import time
import pandas as pd
import json



#https://python.langchain.com/docs/integrations/chat/maritalk/

#Para erros de conexão e https 
#https://stackoverflow.com/questions/51768496/why-do-https-requests-produce-ssl-certificate-verify-failed-error

#Editar aquivo venv\Lib\site-packages\requests\sessions.py; mudar verify = True para False


if __name__ == "__main__":
    #Ler pdf
    pdf_file = r"C:\Users\claudion\OneDrive - Cielo\02. Maritalk\docs\Why You (Currently) Do Not Need Deep Learning for Time Series Forecasting _ by Jonte Dancker _ Jun, 2024 _ Towards Data Science.pdf"
    text = lerpdf(pdf_file)
    #Salvar texto em json com utf-8
    with open('docs/Do Not Need Deep Learning for Time Series Forecasting.json', 'w', encoding='utf-8') as file:
        json.dump(text, file, ensure_ascii=False)

    resum = prompt_user(text, r'key.txt', max_lenght=3000)

    #Salvar resumo em txt utf-8
    with open('docs/Do Not Need Deep Learning for Time Series Forecasting.txt', 'w', encoding='utf-8') as file:
        file.write(resum)