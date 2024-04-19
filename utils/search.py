from langchain_community.retrievers import ArxivRetriever

def get_arxiv_docs(query, num_docs=10):
    retriever = ArxivRetriever(load_max_docs=num_docs)
    docs = retriever.get_relevant_documents(query=query)
    return docs