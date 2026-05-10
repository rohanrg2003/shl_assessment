def map_test_type(name, description="", keys=None):

    if keys:

        if "Personality & Behavior" in keys:
            return "P"

        if "Simulations" in keys:
            return "S"

        if "Ability & Aptitude" in keys:
            return "A"

        if "Knowledge & Skills" in keys:
            return "K"

    text = f"{name} {description}".lower()

    if any(word in text for word in [
        "personality",
        "behavior",
        "opq",
        "motivation"
    ]):
        return "P"

    if any(word in text for word in [
        "simulation",
        "scenario",
        "customer"
    ]):
        return "S"

    if any(word in text for word in [
        "ability",
        "reasoning",
        "cognitive",
        "aptitude",
        "verify"
    ]):
        return "A"

    return "K"