import os
import faiss
import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

# Load API Key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -----------------------------
# Step 1: Load Data
# -----------------------------
def load_data(file_path):
    with open(file_path, "r") as f:
        return f.read()

# -----------------------------
# Step 2: Chunk Text
# -----------------------------
def chunk_text(text, chunk_size=100):
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i+chunk_size]))
    
    return chunks

# -----------------------------
# Step 3: Create Embeddings
# -----------------------------
def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return np.array(response.data[0].embedding, dtype=np.float32)

# -----------------------------
# Step 4: Build Vector Store
# -----------------------------
def build_faiss_index(chunks):
    embeddings = [get_embedding(chunk) for chunk in chunks]
    dim = len(embeddings[0])

    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    return index, embeddings

# -----------------------------
# Step 5: Retrieve
# -----------------------------
def retrieve(query, index, chunks, k=2):
    query_embedding = get_embedding(query)
    D, I = index.search(np.array([query_embedding]), k)
    
    return [chunks[i] for i in I[0]]

# -----------------------------
# Step 6: Generate Answer
# -----------------------------
def generate_answer(query, context):
    prompt = f"""
    Answer the question using the context below.

    Context:
    {context}

    Question:
    {query}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# -----------------------------
# MAIN FLOW
# -----------------------------
def main():
    text = load_data("data/sample.txt")
    chunks = chunk_text(text)

    index, embeddings = build_faiss_index(chunks)

    while True:
        query = input("\nAsk a question (or type 'exit'): ")

        if query.lower() == "exit":
            break

        retrieved_chunks = retrieve(query, index, chunks)
        context = "\n".join(retrieved_chunks)

        answer = generate_answer(query, context)

        print("\nAnswer:", answer)


if __name__ == "__main__":
    main()
