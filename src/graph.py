from langgraph.graph import StateGraph, END

from state import AgentState

from nodes.triage import triage_node
from nodes.retrieve import retrieve_node
from nodes.generate import generate_node
from nodes.verify import verify_node
from nodes.out_of_scope import out_of_scope_node


builder = StateGraph(AgentState)

# -----------------------
# Add Nodes
# -----------------------
builder.add_node("triage", triage_node)
builder.add_node("retrieve", retrieve_node)
builder.add_node("generate", generate_node)
builder.add_node("verify", verify_node)
builder.add_node("out_of_scope", out_of_scope_node)


# -----------------------
# Routing
# -----------------------
def route(state):

    if state["classification"] == "answerable":
        return "retrieve"

    elif state["classification"] == "out_of_scope":
        return "out_of_scope"

    else:
        return "out_of_scope"


builder.set_entry_point("triage")


builder.add_conditional_edges(
    "triage",
    route,
    {
        "retrieve": "retrieve",
        "out_of_scope": "out_of_scope",
    },
)


builder.add_edge("retrieve", "generate")
builder.add_edge("generate", "verify")

builder.add_edge("verify", END)
builder.add_edge("out_of_scope", END)


graph = builder.compile()