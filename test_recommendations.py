from app.services.recommendation_service import generate_recommendations
from app.utils.constraint_extractor import extract_constraints

messages = [
    {
        "role": "user",
        "content": "Hiring a senior Java backend engineer with stakeholder communication"
    }
]

constraints = extract_constraints(messages)

recommendations = generate_recommendations(
    query=messages[-1]["content"],
    constraints=constraints
)

for item in recommendations:
    print("=" * 50)
    print(item["name"])