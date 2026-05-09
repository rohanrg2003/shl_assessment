import re


TECH_SKILLS = [
    "java",
    "python",
    "sql",
    "aws",
    "cloud",
    "angular",
    "c++",
    "c#",
    "hadoop",
    "spark",
    "kafka",
    "android",
    "frontend",
    "backend",
    "selenium",
    "testing",
    "data science",
    "machine learning"
]

SENIORITY_LEVELS = [
    "entry",
    "junior",
    "mid",
    "senior",
    "lead",
    "manager",
    "director"
]


def extract_constraints(messages):
    """
    Extract hiring constraints from conversation
    """

    full_text = " ".join(
        [msg["content"].lower() for msg in messages]
    )

    constraints = {
        "skills": [],
        "seniority": None,
        "communication": False,
        "leadership": False,
        "personality": False
    }

    # Extract skills
    for skill in TECH_SKILLS:
        if skill in full_text:
            constraints["skills"].append(skill)

    # Extract seniority
    for level in SENIORITY_LEVELS:
        if level in full_text:
            constraints["seniority"] = level
            break

    # Communication detection
    communication_keywords = [
        "stakeholder",
        "communication",
        "client-facing",
        "presentation"
    ]

    if any(word in full_text for word in communication_keywords):
        constraints["communication"] = True

    # Leadership detection
    leadership_keywords = [
        "leadership",
        "manager",
        "director",
        "lead"
    ]

    if any(word in full_text for word in leadership_keywords):
        constraints["leadership"] = True

    # Personality detection
    personality_keywords = [
        "personality",
        "behavior",
        "cultural fit"
    ]

    if any(word in full_text for word in personality_keywords):
        constraints["personality"] = True

    return constraints