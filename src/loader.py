from langchain_community.document_loaders import PyPDFLoader

pdf_path = "uploads/cyber.pdf"

print("Loading PDF...")

loader = PyPDFLoader(pdf_path)

docs = loader.load()

print("Pages loaded:", len(docs))

print("\nFirst page:\n")

print(docs[0].page_content[:500])