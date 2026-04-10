from embeddings import search

def generate_answer(query):
    context = search(query)

    # Simple answer
    answer = context[0] if context else "I don't know"

    return {
        "context": context,
        "answer": answer
    }