from langchain_community.document_loaders import PyPDFLoader
import os

UPLOAD_FOLDER = "uploads"

def load_documents():

    docs = []

    for file in os.listdir(UPLOAD_FOLDER):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(
                UPLOAD_FOLDER,
                file
            )

            loader = PyPDFLoader(pdf_path)

            file_docs = loader.load()

            for doc in file_docs:
                doc.metadata["source"] = file

            docs.extend(file_docs)

    print("Total Pages Loaded:", len(docs))

    return docs