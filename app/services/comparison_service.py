import json


with open(
    "app/data/shl_catalog.json",
    "r",
    encoding="utf-8"
) as f:

    catalog = json.load(f)


def extract_assessment_names(query):

    query = query.lower()

    found = []

    for item in catalog:

        name = item.get("name", "").lower()

        if name in query:

            found.append(item)

            continue

        for word in name.split():

            if len(word) > 3 and word in query:

                found.append(item)

                break

    return found[:3]


def compare_assessments(query):

    matched = extract_assessment_names(query)

    if len(matched) < 1:

        return (
            "I could not identify enough SHL "
            "assessments to compare."
        )

    response_parts = []

    response_parts.append(
        "Here is a comparison of the requested SHL assessments:\n"
    )

    for item in matched:

        response_parts.append(
            f"- {item.get('name', 'Unknown Assessment')}: "
            f"{item.get('description', 'No description available.')}"
        )

    response_parts.append(
        "\nThese assessments differ in focus, target skills, "
        "and hiring use cases."
    )

    return "\n".join(response_parts)