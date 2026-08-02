import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

documents = []
document_names = []

# Path to knowledge base
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

KB_PATH = os.path.join(
    BASE_DIR,
    "data",
    "knowledge_base"
)

# Read all markdown files
for file in sorted(os.listdir(KB_PATH)):
    if file.endswith(".md"):
        path = os.path.join(KB_PATH, file)

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        documents.append(text)
        document_names.append(file)

print(f"Loaded {len(documents)} documents.")

# Create embeddings
embeddings = model.encode(documents)

embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

print("FAISS Index Created Successfully!")

# ----------------------------
# Test Search
# ----------------------------

query = "Can a read-only user create API credentials?"

query_embedding = model.encode([query]).astype("float32")

distances, indices = index.search(query_embedding, k=3)

print("\nTop Results:\n")

for i in indices[0]:
    print(document_names[i])