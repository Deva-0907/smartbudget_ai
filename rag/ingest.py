import os
import chromadb

from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create Chroma client
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="shopping_knowledge"
)

documents_folder = "documents"

for filename in os.listdir(documents_folder):

    if filename.endswith(".txt"):

        filepath = os.path.join(documents_folder, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        embedding = model.encode(text).tolist()

        collection.add(
            ids=[filename],
            documents=[text],
            embeddings=[embedding]
        )

print("Knowledge Base Created Successfully!")