from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

print("Model loaded successfully!")

text = "Can a read-only user create API credentials?"

embedding = model.encode(text)

print("Embedding created successfully!")
print("Embedding length:", len(embedding))