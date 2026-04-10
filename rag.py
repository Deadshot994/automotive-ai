from embeddings import search

def generate_answer(query):
    context = search(query)

    # Simple grounded answer (no LLM yet)
    answer = context[0] if context else "I don't know"

    return {
        "context": context,
        "answer": answer
    }