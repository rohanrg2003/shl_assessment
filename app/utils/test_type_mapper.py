def map_test_type(name, description=""):
    """
    Dynamically map SHL assessment type
    """

    text = f"{name} {description}".lower()

    # Personality
    personality_keywords = [
        "opq",
        "personality",
        "behavior",
        "motivation",
        "occupational personality"
    ]

    # Cognitive
    cognitive_keywords = [
        "verify",
        "ability",
        "reasoning",
        "numerical",
        "deductive",
        "inductive",
        "cognitive"
    ]

    # Simulations
    simulation_keywords = [
        "simulation",
        "customer service",
        "virtual",
        "scenario",
        "role play"
    ]

    # Technical / knowledge
    technical_keywords = [
        "java",
        "python",
        "sql",
        "aws",
        "technical",
        "coding",
        "framework"
    ]

    if any(word in text for word in personality_keywords):
        return "P"
    if any(word in text for word in simulation_keywords):
        return "S"
    
    if any(word in text for word in cognitive_keywords):
        return "C"

    if any(word in text for word in technical_keywords):
        return "K"

    # Default fallback
    return "K"