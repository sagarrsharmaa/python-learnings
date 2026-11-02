from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings


load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")


vector = embedding_model.embed_query("delhi is the capital of india")

print(type(vector))
print(len(vector))
print(vector[:3])


sentances = [
    "delhi is the capital of india",
    "virat kohli is a famous cricketer",
    "shah rukh khan is a famous bollywood actor",
]

vectors = embedding_model.embed_documents(sentances)
print(type(vectors))
print(len(vectors))
print(vectors[0][:3])


small_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001", output_dimensionality=32
)

small_vector = small_model.embed_query("delhi is the capital of india")

print(len(small_vector))
print(small_vector[:3])
