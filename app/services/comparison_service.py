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

        name = item["name"].lower()

        short_words = [
            word
            for word in name.split()
            if len(word) >= 2
        ]

        if any(
            word in query
            for word in short_words
        ):

            found.append(item["name"])

    return list(set(found))[:3]


def compare_assessments(query):

    names = extract_assessment_names(query)

    matched = []

    for item in catalog:

        if item["name"] in names:

            matched.append(item)

    if len(matched) < 1:

        return (
            "I could not identify enough SHL "
            "assessments to compare."
        )

    return generate_comparison_response(
        matched
    )import json

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