from app.services.retrieval_service import keyword_search

from groq import Groq
import os
from dotenv import load_dotenv
from app.utils.test_type_mapper import map_test_type
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def extract_assessment_names(query):
    """
    Extract assessment names from comparison query
    """

    query = query.lower()

    known_assessments = [
        "opq",
        "verify",
        "verify g+",
        "hipo",
        "business communication",
        "core java"
    ]

    found = []

    for item in known_assessments:

        if item in query:
            found.append(item)

    return found


def compare_assessments(query):
    """
    Compare SHL assessments
    """

    assessment_names = extract_assessment_names(query)

    retrieved = []

    for name in assessment_names:

        results = keyword_search(name, top_k=1)

        if results:
            retrieved.append(results[0])

    if len(retrieved) < 2:

        return {
            "reply": (
                "I could not identify enough SHL assessments "
                "to perform a comparison."
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    comparison_text = ""

    for item in retrieved:

        comparison_text += f"""
        Name: {item.get('name', '')}
        Description: {item.get('description', '')}
        """

    prompt = f"""
    You are an SHL assessment expert.

    Compare the following assessments.

    Explain:
    - primary purpose
    - what each measures
    - ideal use cases
    - major differences

    Keep response concise and recruiter-focused.

    Assessments:
    {comparison_text}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    formatted_recommendations = []

    for item in retrieved:
        formatted_recommendations.append({
            "name": item.get("name", ""),
            "url": item.get("link", ""),
            "test_type": map_test_type(
                item.get("name", ""),
                item.get("description", "")
            )
        })

    return {
        "reply": response.choices[0].message.content.strip(),
        "recommendations": formatted_recommendations,
        "end_of_conversation": False
    }