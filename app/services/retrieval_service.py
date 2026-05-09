import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load catalog
with open("app/data/shl_catalog.json", "r", encoding="utf-8-sig") as f:
    catalog = json.load(f)

# Load FAISS index
index = faiss.read_index("app/data/faiss_index.bin")


def retrieve_assessments(query, top_k=5):
    """
    Semantic search for relevant SHL assessments
    """

    # Convert query into embedding
    query_embedding = model.encode([query])

    query_embedding = np.array(query_embedding).astype("float32")

    # Search FAISS
    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        if idx < len(catalog):
            results.append(catalog[idx])

    return results


def keyword_search(keyword, top_k=3):
    """
    Hybrid exact + fuzzy keyword search
    """

    keyword = keyword.lower()

    exact_matches = []
    partial_matches = []

    for item in catalog:

        name = item.get("name", "").lower()

        searchable_text = f"""
        {item.get('name', '')}
        {item.get('description', '')}
        {' '.join(item.get('keys', []))}
        """.lower()

        # PRIORITY 1 → exact name match
        if keyword == name:
            exact_matches.append(item)

        # PRIORITY 2 → keyword inside assessment name
        elif keyword in name:
            partial_matches.append(item)

        # PRIORITY 3 → keyword inside metadata
        elif keyword in searchable_text:
            partial_matches.append(item)

    results = exact_matches + partial_matches

    return results[:top_k]