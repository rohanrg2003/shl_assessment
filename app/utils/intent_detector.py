def detect_intent(messages):

    latest_message = messages[-1]["content"].lower().strip()

    vague_phrases = [
        "need assessment",
        "need a test",
        "need an assessment",
        "i need an assessment",
        "help me hire",
        "what tests",
        "show me assessments",
        "looking for assessment",
        "looking for test"
    ]

    comparison_words = [
        "compare",
        "difference between",
        "vs",
        "versus"
    ]

    refine_words = [
        "also",
        "include",
        "add",
        "instead",
        "change",
        "update"
    ]

    # VAGUE / CLARIFICATION
    if any(p in latest_message for p in vague_phrases):

        if len(latest_message.split()) <= 6:
            return "CLARIFY"

    # COMPARISON
    if any(word in latest_message for word in comparison_words):
        return "COMPARE"

    # REFINE
    if any(word in latest_message for word in refine_words):
        return "REFINE"

    return "RECOMMEND"