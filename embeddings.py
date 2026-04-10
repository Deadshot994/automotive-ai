from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from data import vehicles, manuals

# Load model 
model = SentenceTransformer('all-MiniLM-L6-v2')


def prepare_texts():
    texts = []

    # Vehicle data → convert to natural language
    for v in vehicles:
        text = f"""
        {v['name']} is a {v['type']} with {v['seats']} seats.
        Engine: {v['engine']}, Transmission: {v['transmission']}, Fuel: {v['fuel']}.
        Features: {', '.join(v['features'])}.
        Safety: {', '.join(v['safety'])}.
        Oil change: {v['service']['oil']}.
        Tire rotation: {v['service']['tire']}.
        Brake inspection: {v['service']['brake']}.
        Warranty: {v['service']['warranty']}.
        """
        texts.append(text.strip())   

    # Manual data
    for m in manuals:
        texts.append(m["text"].strip())  

    return texts


# Prepare data
texts = prepare_texts()

# Convert to embeddings 
embeddings = model.encode(texts, convert_to_numpy=True)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)


def search(query):
    # Encode query
    q_emb = model.encode([query], convert_to_numpy=True)

    # Search top 3
    D, I = index.search(q_emb, k=3)

    # Return matching texts
    return [texts[i] for i in I[0]]