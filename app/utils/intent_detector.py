def detect_intent(messages):
    """
    Detect conversational intent
    """

    latest_message = messages[-1]["content"].lower()

    # REFUSAL
    refusal_keywords = [
        "ignore previous instructions",
        "legal advice",
        "financial advice",
        "medical advice"
    ]

    if any(word in latest_message for word in refusal_keywords):
        return "REFUSE"

    # COMPARISON
    comparison_keywords = [
        "compare",
        "difference between",
        "vs",
        "versus"
    ]

    if any(word in latest_message for word in comparison_keywords):
        return "COMPARE"

    # REFINEMENT
    refinement_keywords = [
        "also",
        "add",
        "include",
        "instead",
        "replace"
    ]

    if any(word in latest_message for word in refinement_keywords):
        return "REFINE"

    # VERY VAGUE QUERIES ONLY
    vague_phrases = [
        "need assessment",
        "need a test",
        "need an assessment"
    ]

    if latest_message.strip() in vague_phrases:
        return "CLARIFY"

    # VERY SHORT queries
    if len(latest_message.split()) <= 2:
        return "CLARIFY"

    # DEFAULT
    return "RECOMMEND"