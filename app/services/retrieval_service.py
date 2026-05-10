import json


with open("app/data/shl_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)


HIGH_PRIORITY_KEYWORDS = {
    "java": 5,
    "backend": 4,
    "engineer": 3,
    "developer": 4,
    "software": 4,
    "programming": 5,
    "coding": 5,
    "technical": 4,

    "leadership": 5,
    "leader": 4,
    "manager": 4,
    "executive": 4,
    "director": 4,

    "personality": 5,
    "behavioral": 5,
    "behavior": 4,
    "motivation": 4,
    "competency": 4,
    "opq": 5,

    "communication": 4,
    "stakeholder": 4,

    "cognitive": 5,
    "reasoning": 5,
    "ability": 4,

    "simulation": 5,
    "customer": 3,
    "support": 3,
    "sales": 3,

    "graduate": 4,
    "entry": 3,
    "senior": 4
}


NEGATIVE_KEYWORDS = [
    "aerospace",
    "aeronautical",
    "ceramic",
    "civil",
    "chemical",
    "automotive"
]


def calculate_score(query, searchable_text):

    score = 0

    query_words = query.split()

    # BASIC KEYWORD MATCHING
    for word in query_words:

        if word in searchable_text:

            score += HIGH_PRIORITY_KEYWORDS.get(word, 1)

    # BOOST JAVA / SOFTWARE / BACKEND
    if any(word in query for word in [
        "java",
        "backend",
        "developer",
        "software",
        "programming",
        "coding"
    ]):

        if any(keyword in searchable_text for keyword in [
            "java",
            "backend",
            "developer",
            "coding",
            "programming",
            "automata",
            "software"
        ]):
            score += 12

    # BOOST PERSONALITY
    if any(word in query for word in [
        "personality",
        "behavioral",
        "behavior",
        "motivation",
        "soft skills"
    ]):

        if any(keyword in searchable_text for keyword in [
            "opq",
            "personality",
            "behavior",
            "motivation",
            "competency",
            "leadership"
        ]):
            score += 18

        # EXTRA BOOST FOR SOFTWARE / TECH ROLES
        if any(word in query for word in [
            "software",
            "developer",
            "engineer",
            "technical",
            "java"
        ]):

            if any(keyword in searchable_text for keyword in [
                "opq",
                "personality",
                "competency",
                "behavior"
            ]):
                score += 20

    # BOOST LEADERSHIP
    if any(word in query for word in [
        "leadership",
        "leader",
        "director",
        "executive",
        "manager"
    ]):

        if any(keyword in searchable_text for keyword in [
            "leadership",
            "hipo",
            "manager",
            "executive",
            "leadership report"
        ]):
            score += 15

    # BOOST COGNITIVE / REASONING
    if any(word in query for word in [
        "cognitive",
        "reasoning",
        "ability"
    ]):

        if any(keyword in searchable_text for keyword in [
            "verify",
            "reasoning",
            "ability",
            "cognitive"
        ]):
            score += 15

    # BOOST SIMULATIONS
    if any(word in query for word in [
        "simulation",
        "customer",
        "support",
        "sales"
    ]):

        if "simulation" in searchable_text:
            score += 12

    # PENALIZE IRRELEVANT ENGINEERING
    for negative in NEGATIVE_KEYWORDS:

        if negative in searchable_text:
            score -= 8

    return score


def semantic_search(query, top_k=10):

    query = query.lower()

    scored_results = []

    for item in catalog:

        searchable_text = f"""
        {item.get('name', '')}
        {item.get('description', '')}
        {' '.join(item.get('keys', []))}
        """.lower()

        score = calculate_score(
            query,
            searchable_text
        )

        if score > 0:

            scored_results.append(
                (score, item)
            )

    scored_results.sort(
        key=lambda x: x[0],
        reverse=True
    )

    unique_results = []

    seen_names = set()

    for _, item in scored_results:

        name = item.get("name", "")

        if name not in seen_names:

            unique_results.append(item)

            seen_names.add(name)

        if len(unique_results) >= top_k:
            break

    return unique_results


def keyword_search(query, top_k=10):
    return semantic_search(query, top_k)


def retrieve_assessments(query, top_k=10):
    return semantic_search(query, top_k)