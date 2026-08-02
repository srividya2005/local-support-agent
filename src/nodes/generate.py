from utils.llm import generate_answer


def generate_node(state):
    """
    Generate an answer using the retrieved knowledge base documents.
    """

    question = state["question"]
    retrieved_docs = state.get("retrieved_docs", [])

    # No documents found
    if not retrieved_docs:
        state["answer"] = "I do not have enough information from the knowledge base."
        state["context"] = ""
        state["sources"] = []

        print("\n[GENERATE] No documents retrieved.")

        return state

    # Build context from the top 3 retrieved documents
    context = ""

    for doc in retrieved_docs:
        context += f"\n\nSource: {doc['document']}\n"
        context += doc["content"]

    # Keep the prompt short for TinyLlama
    context = context[:1500]

    prompt = f"""
You are an enterprise support assistant.

Answer ONLY using the knowledge base below.

Rules:
1. Use ONLY the information provided.
2. Do NOT make up facts.
3. If the answer is not available, say:
   "I do not have enough information from the knowledge base."
4. Keep the answer short (2-4 sentences).

Knowledge Base:
{context}

Question:
{question}

Answer:
"""

    answer = generate_answer(prompt)

    state["answer"] = answer.strip()
    state["context"] = context

    # Save source documents
    state["sources"] = [
        {"document": doc["document"]}
        for doc in retrieved_docs
    ]

    print("\n[GENERATE] Answer generated.")

    return state