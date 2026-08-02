import sys
import os

sys.path.append(os.path.abspath("src"))

from graph import graph


def test_out_of_scope():

    state = {
        "question": "Refund my subscription",
        "classification": "",
        "retrieved_docs": [],
        "context": "",
        "answer": "",
        "sources": [],
        "confidence": 0.0,
        "requires_human": False,
        "reason": ""
    }

    result = graph.invoke(state)

    assert result["classification"] == "out_of_scope"