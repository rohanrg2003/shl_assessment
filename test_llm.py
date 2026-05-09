from app.services.recommendation_service import generate_recommendations
from app.services.llm_service import generate_response
from app.utils.constraint_extractor import extract_constraints

messages = [
    {
        "role": "user",
        "content": "Hiring a senior Java backend engineer with stakeholder communication"
    }
]

query = messages[-1]["content"]

constraints = extract_constraints(messages)

recommendations = generate_recommendations(
    query=query,
    constraints=constraints
)

response = generate_response(
    query=query,
    recommendations=recommendations,
    intent="RECOMMEND"
)

print(response)