def detect_intent(messages):

    if not messages:
        return "CLARIFY"

    latest_message = (
        messages[-1]
        .get("content", "")
        .lower()
        .strip()
    )

    vague_phrases = [
        "assessment",
        "test",
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

    # REFINE FIRST
    if any(
        word in latest_message
        for word in refine_words
    ):
        return "REFINE"

    # COMPARISON
    if any(
        word in latest_message
        for word in comparison_words
    ):
        return "COMPARE"

    # VERY SHORT VAGUE QUERY
    if len(latest_message.split()) <= 4:
        return "CLARIFY"

    # VAGUE PHRASES
    if any(
        p in latest_message
        for p in vague_phrases
    ):

        if len(latest_message.split()) <= 8:
            return "CLARIFY"

    return "RECOMMEND"