from groq import Groq

import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_response(query, recommendations, intent):
    """
    Generate grounded conversational response
    """

    recommendation_text = ""

    for item in recommendations:
        recommendation_text += f"""
        Name: {item.get('name', '')}
        Description: {item.get('description', '')}
        URL: {item.get('link', '')}
        """

    prompt = f"""
    You are an SHL assessment recommendation assistant.

    ONLY use the provided assessments.
    NEVER hallucinate assessments.
    NEVER invent URLs.

    Keep responses:
    - concise
    - professional
    - recruiter-focused

    User Query:
    {query}

    Intent:
    {intent}

    Retrieved Assessments:
    {recommendation_text}

    Generate a concise professional response explaining:
    - why these assessments fit
    - what they evaluate

    Keep response under 120 words.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()