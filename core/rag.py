from sentence_transformers import SentenceTransformer


class QASystem:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.documents = self._load_and_validate_documents()
        self.initialize()

    def _load_documents_from_source(self):
        """Implement your actual document loading logic here"""
        # Example: Replace this with your actual document source
        return [
            "This is document 1 about hotel bookings",
            "Document 2 contains booking policies",
            # Add your real documents here
            # Can load from database/CSV/PDF etc.
        ]

    def _load_and_validate_documents(self):
        raw_documents = self._load_documents_from_source()

        clean_docs = [doc for doc in raw_documents
                      if doc and str(doc).strip()]

        if not clean_docs:
            raise ValueError("No valid documents found!")
        return clean_docs

    def initialize(self):
        if not self.documents:
            raise ValueError("No documents to initialize!")

        print(f"Loaded {len(self.documents)} documents")
        self.embeddings = self.model.encode(self.documents)

    def query(self, question: str):
        """Implement your RAG query logic here"""
        question_embedding = self.model.encode(question)
        # Add similarity search and generation logic
        return f"Answer to: {question}"


# Singleton instance for the application
qa_system = QASystem()


def answer_question(question: str):
    """Public API endpoint"""
    return qa_system.query(question)