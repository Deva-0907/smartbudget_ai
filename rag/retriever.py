import chromadb
from sentence_transformers import SentenceTransformer


class RAGRetriever:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        client = chromadb.PersistentClient(path="./chroma_db")

        self.collection = client.get_collection(
            "shopping_knowledge"
        )

    def retrieve(self, query):

        embedding = self.model.encode(query).tolist()

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=3
        )

        return results["documents"][0]