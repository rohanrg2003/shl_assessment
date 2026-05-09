from app.services.retrieval_service import retrieve_assessments

results = retrieve_assessments(
    "Hiring a Java backend developer with stakeholder communication"
)

for item in results:
    print("=" * 50)
    print(item["name"])
    print(item["link"])