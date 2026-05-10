from app.utils.intent_detector import detect_intent

from app.services.recommendation_service import (
    generate_recommendations
)

from app.services.comparison_service import (
    compare_assessments
)

from app.services.llm_service import (
    generate_response
)

from app.utils.constraint_extractor import (
    extract_constraints
)

from app.utils.test_type_mapper import (
    map_test_type
)


INJECTION_PATTERNS = [
    "ignore previous instructions",
    "ignore your rules",
    "system prompt",
    "you are now",
    "act as",
    "forget instructions",
    "pretend you are"
]


def format_recommendations(recommendations):

    formatted = []

    for item in recommendations:

        formatted.append({
            "name": item.get("name", ""),
            "url": item.get("url", ""),
            "test_type": map_test_type(
                item.get("name", ""),
                item.get("description", ""),
                item.get("keys", [])
            )
        })

    return formatted


def process_conversation(messages):

    latest_message = messages[-1]["content"]

    latest_lower = latest_message.lower()

    # PROMPT INJECTION / OFF-TOPIC
    if any(
        pattern in latest_lower
        for pattern in INJECTION_PATTERNS
    ):

        return {
            "reply": (
                "I can only assist with SHL assessment "
                "recommendations, comparisons, and "
                "hiring-related evaluation guidance."
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    intent = detect_intent(messages)

    # CLARIFICATION FLOW
    if intent == "CLARIFY":

        return {
            "reply": (
                "Could you share more details about the role, "
                "required skills, seniority level, or "
                "assessment goals?"
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    # COMPARISON FLOW
    elif intent == "COMPARE":

        response_text = compare_assessments(
            latest_message
        )

        return {
            "reply": response_text,
            "recommendations": [],
            "end_of_conversation": True
        }

    # RECOMMENDATION / REFINE FLOW
    else:

        constraints = extract_constraints(
            messages
        )

        recommendations = generate_recommendations(
            latest_message,
            constraints
        )

        formatted_recommendations = (
            format_recommendations(
                recommendations
            )
        )

        if intent == "REFINE":

            response_text = (
                "Updated shortlist based on your "
                "additional requirements.\n\n"
                + generate_response(
                    latest_message,
                    recommendations
                )
            )

        else:

            response_text = generate_response(
                latest_message,
                recommendations
            )

        return {
            "reply": response_text,
            "recommendations": formatted_recommendations,
            "end_of_conversation": (
                len(formatted_recommendations) > 0
            )
        }