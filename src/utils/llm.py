
from transformers import pipeline

print("Loading pipeline...")

pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    device=-1
)

print("Loaded!")


def generate_answer(prompt):
    result = pipe(
        prompt,
        max_new_tokens=40,
        do_sample=False,
        return_full_text=False
    )

    return result[0]["generated_text"].strip()