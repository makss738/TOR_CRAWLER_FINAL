import os

from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    Settings
)

from llama_index.embeddings.huggingface import HuggingFaceEmbedding


KNOWLEDGE_PATH = "data/knowledge"


INDEX_PATH = "data/vector_index"



def load_documents():

    documents = SimpleDirectoryReader(
        KNOWLEDGE_PATH,
        recursive=True
    ).load_data()


    return documents



def create_index():

    print(
        "[+] Loading knowledge base..."
    )


    documents = load_documents()


    Settings.embed_model = HuggingFaceEmbedding(
        model_name=
        "sentence-transformers/all-MiniLM-L6-v2"
    )


    index = VectorStoreIndex.from_documents(
        documents
    )


    index.storage_context.persist(
        persist_dir=INDEX_PATH
    )


    print(
        "[+] Vector database created"
    )



def load_index():

    from llama_index.core import StorageContext


    storage_context = StorageContext.from_defaults(
        persist_dir=INDEX_PATH
    )


    index = VectorStoreIndex.from_documents(
        [],
        storage_context=storage_context
    )


    return index



def ask_question(question):


    index = load_index()


    engine = index.as_query_engine()


    response = engine.query(
        question
    )


    return str(response)



if __name__ == "__main__":


    if not os.path.exists(
        INDEX_PATH
    ):

        create_index()


    while True:


        question=input(
            "\nQuestion CTI : "
        )


        if question=="exit":

            break


        answer=ask_question(
            question
        )


        print(
            "\nRéponse :"
        )

        print(answer)
