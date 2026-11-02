from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import numpy as np


load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")


docs = [
    "a deadlock happens when processes wait forever for resources held by each other",
    "normalization in dbms organizes tables to reduce duplicate data",
    "tcp is a reliable protocol that uses a three way handshake to set up a connection",
    "binary search finds an item in a sorted array in logarithmic time",
    "newtons second law says force equals mass times acceleration",
]


doc_vectors = embedding_model.embed_documents(docs)


def cosine_similarities(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


while True:
    question = input("you : ")
    if question.strip().lower() == "exit":
        break

    question_vector = embedding_model.embed_query(question)

    best_score = -1
    best_doc = None

    for doc, doc_vector in zip(docs, doc_vectors):
        similarity = cosine_similarities(question_vector, doc_vector)
        if similarity > best_score:
            best_score = similarity
            best_doc = doc

    if best_score < 0.65:
        print("no relevant note found")
    else:
        print(f"{best_score:.3f}  {best_doc}")
