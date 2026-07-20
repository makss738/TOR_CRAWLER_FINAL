import os

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader


KNOWLEDGE_PATH = "data/knowledge"


def load_knowledge():

    documents = SimpleDirectoryReader(
        KNOWLEDGE_PATH,
        recursive=True
    ).load_data()


    return documents


def create_index():

    documents = load_knowledge()


    index = VectorStoreIndex.from_documents(
        documents
    )


    return index


def ask_question(question):

    index = create_index()


    engine = index.as_query_engine()


    response = engine.query(
        question
    )


    return response



if __name__ == "__main__":


    print(
        "🧠 CTI RAG Assistant"
    )


    question = input(
        "Question : "
    )


    answer = ask_question(
        question
    )


    print("\nRéponse :")

    print(answer)




