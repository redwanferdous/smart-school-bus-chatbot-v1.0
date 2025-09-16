# smartbus_chatbot.py
# Smart School Bus Chatbot by FronTech
# RAG-based chatbot (PDF → embeddings → GPT)

import numpy as np
from sentence_transformers import SentenceTransformer
import openai  # Keep your API key in Colab secrets, do NOT hardcode
from pypdf import PdfReader

# ----------------------------
# Step 1: Load PDF
# ----------------------------
pdf_path = "YOUR_FILE.pdf"
pdf_reader = PdfReader(pdf_path)
text = ""
for page in pdf_reader.pages:
    text += page.extract_text() + "\n"

# ----------------------------
# Step 2: Chunk text
# ----------------------------
def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

chunks = chunk_text(text)
print("Chunks created:", len(chunks))

# ----------------------------
# Step 3: Create embeddings
# ----------------------------
model = SentenceTransformer('all-MiniLM-L6-v2')
chunk_embeddings = model.encode(chunks)

# ----------------------------
# Step 4: Function to find most relevant chunks
# ----------------------------
def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def find_top_chunks(query, chunks, embeddings, top_n=5):
    query_emb = model.encode([query])[0]
    sims = [cosine_sim(query_emb, emb) for emb in embeddings]
    top_idx = np.argsort(sims)[-top_n:][::-1]
    return [chunks[i] for i in top_idx]

# ----------------------------
# Step 5: GPT query function
# ----------------------------
def ask_gpt_for_answer(query, context):
    """
    Make sure to set your API key in environment or Colab secret:
    openai.api_key = YOUR_OPENAI_KEY
    """
    prompt = f"Use the following context to answer the question:\n\n{context}\n\nQuestion: {query}\nAnswer:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()

# ----------------------------
# Step 6: Chatbot loop
# ----------------------------
print("\nSmart School Bus Chatbot (type 'exit' to quit)")
while True:
    query = input("\nYou: ")
    if query.lower() in ["exit", "quit"]:
        print("Chatbot session ended.")
        break
    top_chunks = find_top_chunks(query, chunks, chunk_embeddings, top_n=5)
    context = "\n\n".join(top_chunks)
    answer = ask_gpt_for_answer(query, context)
    print("\nBot:", answer)
