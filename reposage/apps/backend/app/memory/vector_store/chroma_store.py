import chromadb
from app.config.settings import settings


class ChromaMemoryStore:
    def __init__(self) -> None:
        self.client = chromadb.PersistentClient(path=settings.chroma_path)
        self.collection = self.client.get_or_create_collection('reposage_memory')

    def add(self, doc_id: str, text: str, metadata: dict) -> None:
        self.collection.add(ids=[doc_id], documents=[text], metadatas=[metadata])

    def search(self, query: str, n_results: int = 5) -> dict:
        return self.collection.query(query_texts=[query], n_results=n_results)
