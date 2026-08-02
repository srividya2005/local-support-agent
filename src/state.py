from typing import TypedDict, List, Dict


class AgentState(TypedDict):
    question: str
    classification: str

    # Retrieved documents
    retrieved_docs: List[Dict]

    # Combined retrieved text
    context: str

    # Generated answer
    answer: str

    # Source documents
    sources: List[Dict]

    # Verification
    confidence: float
    requires_human: bool
    reason: str