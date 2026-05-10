import json

with open("app/data/shl_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)


def semantic_search(query, top_k=10):

    query = query.lower()

    scored_results = []

    for item in catalog:

        score = 0

        searchable_text = f"""
        {item.get('name', '')}
        {item.get('description', '')}
        {' '.join(item.get('keys', []))}
        """.lower()

        for word in query.split():

            if word in searchable_text:
                score += 1

        if score > 0:
            scored_results.append((score, item))

    scored_results.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [
        item for _, item in scored_results[:top_k]
    ]
def retrieve_assessments(query, top_k=10):
    return semantic_search(query, top_k)
def keyword_search(query, top_k=10):
    return semantic_search(query, top_k)


def retrieve_assessments(query, top_k=10):
    return semantic_search(query, top_k)