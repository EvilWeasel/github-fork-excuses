from langchain.embeddings.spacy_embeddings import SpacyEmbeddings
import numpy as np
from scipy.spatial.distance import cosine
import sys

# Initialisiere SpaCy-Embeddings
embedder = SpacyEmbeddings()

def nearest_neighbor(embedding, candidates):
    embeddings = embedder.embed_documents(candidates)
    distances = [cosine(embedding, candidate) for candidate in embeddings]
    return candidates[np.argmin(distances)]

if __name__ == "__main__":
    user_prompt = sys.argv[1]  # User-Prompt aus der Kommandozeile
    user_embedding = embedder.embed_query(user_prompt)

    # Lade excuses aus der Datei
    with open("excuses.txt", "r", encoding="utf-8") as f:
        excuses = f.readlines()

    excuses = [e.strip() for e in excuses]  # Zeilenumbrüche entfernen

    # Finde die passendste Ausrede
    best_excuse = nearest_neighbor(user_embedding, excuses)

    print(f"Passende Ausrede: {best_excuse}")
