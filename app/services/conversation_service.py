from app.utils.intent_detector import detect_intent
from app.utils.constraint_extractor import extract_constraints

from app.services.recommendation_service import (
    generate_recommendations
)

from app.services.llm_service import generate_response
from app.services.comparison_service import (
    compare_assessments
)
from app.utils.test_type_mapper import map_test_type

def build_conversation_context(messages):
    """
    Reconstruct meaningful conversation context
    """

    user_messages = []

    for msg in messages:

        if msg["role"] == "user":
            user_messages.append(msg["content"])

    return " ".join(user_messages)


def process_conversation(messages):
    """
    Main orchestration pipeline
    """

    # Build full conversation context
    conversation_context = build_conversation_context(messages)

    # Latest user message
    latest_query = messages[-1]["content"]

    # Detect intent
    intent = detect_intent(messages)
    # Comparison handling
    if intent == "COMPARE":

        return compare_assessments(conversation_context)
    # Clarification handling
    if intent == "CLARIFY":

        return {
            "reply": (
                "Could you share more details about the role, "
                "required skills, seniority level, or assessment goals?"
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    # Refusal handling
    if intent == "REFUSE":

        return {
            "reply": (
                "I can only assist with SHL assessment "
                "recommendations, comparisons, and hiring-related evaluation guidance."
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    # Extract constraints from FULL conversation
    constraints = extract_constraints(messages)

    # Generate recommendations using FULL context
    recommendations = generate_recommendations(
        query=conversation_context,
        constraints=constraints
    )

    # Generate conversational response
    response_text = generate_response(
        query=conversation_context,
        recommendations=recommendations,
        intent=intent
    )

    # Format recommendations
    formatted_recommendations = []
    for item in recommendations:
        formatted_recommendations.append({
            "name": item.get("name", ""),
            "url": item.get("link", ""),
            "test_type": map_test_type(
                item.get("name", ""),
                item.get("description", "")
    )
})
    return {
        "reply": response_text,
        "recommendations": formatted_recommendations,
        "end_of_conversation": False
    }