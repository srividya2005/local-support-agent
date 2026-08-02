from state import AgentState
from utils.vectorstore import index, model, documents, document_names


def retrieve_node(state: AgentState) -> AgentState:
    """
    Retrieve the most relevant documents using FAISS.
    """

    question = state["question"]

    # Create embedding for the question
    query_embedding = model.encode([question]).astype("float32")

    # Search top 3 documents
    distances, indices = index.search(query_embedding, k=3)

    retrieved = []

    for i in indices[0]:
        retrieved.append({
            "document": document_names[i],
            "content": documents[i]
        })

    state["retrieved_docs"] = retrieved

    print("\n[RETRIEVE] Documents Found:")

    for doc in retrieved:
        print("-", doc["document"])

    return state