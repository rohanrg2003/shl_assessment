from app.services.retrieval_service import (
    retrieve_assessments,
    keyword_search
)


def recommendation_exists(recommendations, keyword):
    """
    Check if recommendation already exists
    """

    for rec in recommendations:
        if keyword.lower() in rec["name"].lower():
            return True

    return False


def generate_recommendations(query, constraints):
    """
    Generate SHL-style recommendation bundles
    """

    # Base semantic retrieval
    recommendations = retrieve_assessments(query, top_k=8)

    final_recommendations = recommendations.copy()

    # Technical roles
    technical_skills = [
        "java",
        "python",
        "sql",
        "aws",
        "cloud",
        "backend",
        "frontend",
        "data science",
        "machine learning"
    ]

    if any(skill in constraints["skills"] for skill in technical_skills):

        # Add cognitive assessment
        if not recommendation_exists(final_recommendations, "verify"):

            cognitive = keyword_search(
                "verify",
                top_k=1
            )

            final_recommendations.extend(cognitive)

        # Add personality assessment
        if not recommendation_exists(final_recommendations, "opq"):

            personality = keyword_search(
                "opq",
                top_k=1
            )

            final_recommendations.extend(personality)

    # Leadership roles
    if constraints["leadership"]:

        leadership_items = keyword_search(
            "leadership",
            top_k=2
        )

        final_recommendations.extend(leadership_items)

    # Communication-heavy roles
    if constraints["communication"]:

        communication_items = keyword_search(
            "business communication",
            top_k=2
        )

        final_recommendations.extend(communication_items)

    # Remove duplicates
    unique = {}

    for item in final_recommendations:
        unique[item["name"]] = item

    final_recommendations = list(unique.values())

    # Limit to top 10
    final_recommendations = final_recommendations[:10]

    return final_recommendations