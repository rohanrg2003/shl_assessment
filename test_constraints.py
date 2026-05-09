from app.utils.constraint_extractor import extract_constraints

messages = [
    {
        "role": "user",
        "content": "Hiring a senior Java backend engineer with stakeholder communication"
    }
]

constraints = extract_constraints(messages)

print(constraints)