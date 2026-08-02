from state import AgentState


def triage_node(state: AgentState) -> AgentState:
    """
    Classify the incoming user question.
    """

    question = state["question"].lower()

    # Questions outside the product knowledge
    if "refund" in question or "subscription" in question:
        state["classification"] = "out_of_scope"

    # Ambiguous questions
    elif len(question.split()) < 4:
        state["classification"] = "requires_clarification"

    # Escalation requests
    elif "escalate" in question or "support ticket" in question:
        state["classification"] = "requires_escalation"

    # Everything else
    else:
        state["classification"] = "answerable"

    print(f"[TRIAGE] Classification: {state['classification']}")

    return state