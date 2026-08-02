def out_of_scope_node(state):
    """
    Handle questions outside the supported knowledge base.
    """

    state["answer"] = (
        "This request is outside the scope of the OrbitDesk knowledge base. "
        "I cannot issue refunds or provide legal advice."
    )

    state["sources"] = []

    state["confidence"] = 1.0
    state["requires_human"] = True
    state["reason"] = (
        "Out-of-scope request handled safely."
    )

    print("[OUT_OF_SCOPE] Safe response returned.")

    return state