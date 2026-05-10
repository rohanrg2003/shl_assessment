def generate_response(query, recommendations):

    if not recommendations:

        return (
            "I could not find suitable SHL assessments "
            "for the provided requirements."
        )

    top_names = []

    for item in recommendations[:3]:

        name = str(
            item.get("name", "Assessment")
        )

        top_names.append(name)

    joined = ", ".join(top_names)

    return (
        f"For this role, I recommend {joined}. "
        "These assessments align with the required "
        "skills, competencies, and hiring goals."
    )