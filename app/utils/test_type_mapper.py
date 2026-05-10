def map_test_type(name="", description="", keys=None):

    # SAFETY
    if keys is None:
        keys = []

    # HANDLE STRING CASE
    if isinstance(keys, str):
        keys = [keys]

    # CATEGORY MAPPING
    for key in keys:

        key_lower = key.lower()

        if "personality" in key_lower:
            return "P"

        if "simulation" in key_lower:
            return "S"

        if "ability" in key_lower:
            return "A"

        if "knowledge" in key_lower:
            return "K"

    text = f"{name} {description}".lower()

    # FALLBACKS
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