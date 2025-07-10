from src.retriever import get_top_k_docs

def build_prompt(query, docs):
    context = "\n\n".join([doc.page_content for doc in docs])

    # Detect if user wants a bullet format
    bullet_keywords = ["mention", "list", "in points", "bullet", "summarize", "give in points"]
    lower_query = query.lower()
    wants_bullets = any(kw in lower_query for kw in bullet_keywords)

    prompt = f"""
You are a helpful AI assistant.

Use only the information from the CONTEXT to answer the QUESTION clearly and correctly.

{"""
If the answer involves listing multiple items, format your response as properly spaced bullet points like:

• First point  
• Second point  
• Third point  
""" if wants_bullets else "Write in grammatically correct and concise sentences."}

---

CONTEXT:
{context}

QUESTION:
{query}

ANSWER:
"""
    return prompt

def generate_answer(query, embedder, llm):
    docs = get_top_k_docs(query, embedder, k=5)  # Using more chunks = better context
    prompt = build_prompt(query, docs)
    response = llm(prompt)
    return response, docs
