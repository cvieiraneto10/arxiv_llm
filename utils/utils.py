from langchain_community.retrievers import ArxivRetriever
import PyPDF2

def get_arxiv_docs(query, num_docs=10):
    retriever = ArxivRetriever(load_max_docs=num_docs)
    docs = retriever.get_relevant_documents(query=query)
    return docs


def lerpdf(pdf_file:str)-> dict:
    """ Função recebe um arquivo pdf e retorna um dicionário onde cada página é uma chave e o valor é o texto da página"""
    pdf = PyPDF2.PdfReader(pdf_file)
    text = {}
    for i in range(len(pdf.pages)):
        print(f'Lendo página {i}')
        page = pdf.pages[i]
        text[i] = page.extract_text()
    return text