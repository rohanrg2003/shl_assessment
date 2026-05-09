# SHL Conversational Assessment Recommender

A conversational AI system for recommending SHL assessments based on hiring requirements, conversational refinements, and recruiter-focused queries.

## Features

- Semantic assessment retrieval
- Hybrid keyword augmentation
- Multi-turn conversational memory
- Intent detection
- Constraint extraction
- SHL assessment comparison flow
- Dynamic test type mapping
- Grounded LLM responses
- Refusal handling

## Tech Stack

- FastAPI
- FAISS
- Sentence Transformers
- Groq Llama 3.3 70B
- Python

## API Endpoints

### Health Check

GET `/health`

### Chat Endpoint

POST `/chat`

## Sample Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring a senior Java backend engineer"
    }
  ]
}
```

## Local Setup

```bash
pip install -r requirements.txt

uvicorn app.main:app --reload
```

## Architecture

The system uses:
- sentence-transformer embeddings
- FAISS semantic retrieval
- hybrid keyword augmentation
- conversational orchestration
- grounded LLM response generation

## Evaluation

The system was tested against:
- clarification queries
- technical hiring scenarios
- leadership recommendations
- refinement conversations
- assessment comparisons
- refusal scenarios
- multi-turn conversational memory