from graph import graph

question = input("Ask your question: ")

state = {
    "question": question,
    "classification": "",
    "retrieved_docs": [],
    "answer": "",
    "sources": [],
    "confidence": 0.0,
    "requires_human": False,
    "reason": ""
}

result = graph.invoke(state)

print("\n==========================")
print("Classification:", result["classification"])
print("\nAnswer:\n")
print(result["answer"])

print("\nSources:")
for s in result["sources"]:
    print("-", s["document"])

print("\nConfidence:", result["confidence"])
print("Requires Human:", result["requires_human"])
print("Reason:", result["reason"])