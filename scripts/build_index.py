import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load catalog
with open("app/data/shl_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

documents = []

for item in catalog:
    text = f"""
    Name: {item.get('name', '')}
    Description: {item.get('description', '')}
    Job Levels: {' '.join(item.get('job_levels', []))}
    Keys: {' '.join(item.get('keys', []))}
    """

    documents.append(text)

# Generate embeddings
embeddings = model.encode(documents, show_progress_bar=True)

# Convert to numpy
embeddings = np.array(embeddings).astype("float32")

# Save embeddings
np.save("app/data/embeddings.npy", embeddings)

# Build FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save FAISS index
faiss.write_index(index, "app/data/faiss_index.bin")

print("FAISS index built successfully!")