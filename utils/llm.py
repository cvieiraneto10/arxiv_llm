import maritalk
#ignore warnings
import warnings
warnings.filterwarnings("ignore")


def get_response(input_text:str, userkey:str):
    model = maritalk.MariTalk(
        key=userkey,
        model="sabia-2-small"  # No momento, suportamos os modelos sabia-2-medium e sabia-2-small
    )

    response = model.generate(input_text, max_tokens=2500, temperature=0.3)
    answer = response["answer"]
    return answer

#Ler key from txt file
def read_key(path_key:str='key.txt'):
    with open(path_key, 'r') as file:
        key = file.read().replace('\n', '')
    return key

def prompt_user(file_json:dict, apikey_path:str, max_lenght: int=1000)->str:
    """Função recebe um dicionário com as páginas do pdf e retorna um texto o resumo do pdf"""
    text = ''
    for i in file_json.keys():
        text += file_json[i]

    import re

    #Remover espaços em excesso
    text = re.sub(' +', ' ', text)
    #remover quebras de linha
    text = text.replace('\n', ' ')
    #converter tudo para lower case
    text = text.lower()
    #Remover palavras com menos de 3 caracteres
    text = ' '.join([word for word in text.split() if len(word)>2])
    #remover palavras com mais de 15 caracteres
    text = ' '.join([word for word in text.split() if len(word)<=15])
    #remover caracteres especiais
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)

    #Dividir texto em partes de max_lenght caracteres
    parts = [text[i:i+max_lenght] for i in range(0, len(text), max_lenght)]

    key = read_key(apikey_path)

    #Gerar resumo
    for i in range(len(parts)):
        print(f"Parte {i+1} de {len(parts)}")
        if i == 0:
            prompt = f"Faça um resumo em bullet points do texto abaixo:\n{parts[i]} \nRESUMO:"
            resumo = get_response(prompt, key)
        else:
            prompt=f"Faça um resumo em bullet points do texto abaixo:\n{parts[i]}"
            res = get_response(prompt, key)
            prompt = f"Baseado nas informações abaixo:\n{resumo}\n Completemente o seguinte texto:\n{res}\n TEXTO ENRIQUECIDO:"

    return resumo