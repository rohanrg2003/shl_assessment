import json

from app.services.llm_service import (
    generate_comparison_response
)


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

        # Exact full name match
        if name in query:

            found.append(item)

            continue

        # Partial word match
        for word in name.split():

            if len(word) > 3 and word in query:

                found.append(item)

                break

    return found[:3]


def compare_assessments(query):

    matched = extract_assessment_names(query)

    if not matched:

        return (
            "I could not identify enough SHL "
            "assessments to compare."
        )

    response = generate_comparison_response(
        matched
    )

    # SAFETY
    if not isinstance(response, str):

        response = str(response)

    return response