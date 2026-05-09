from app.utils.intent_detector import detect_intent

messages = [
    {
        "role": "user",
        "content": "Hiring a Java backend developer with stakeholder communication"
    }
]

intent = detect_intent(messages)

print(intent)