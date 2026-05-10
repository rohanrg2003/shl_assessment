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
    )