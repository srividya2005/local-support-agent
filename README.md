# Local-First Support Agent Network

## Overview

This project implements a **Local-First Support Agent Network** for the fictional **OrbitDesk** product. It answers support questions using a local knowledge base and a graph-based workflow built with **LangGraph**. All inference runs locally using Hugging Face models, and no hosted LLM APIs are used.

---

## Features

* Local knowledge base search using FAISS
* Graph-based orchestration with LangGraph
* Local response generation using TinyLlama
* Verification and safe fallback responses
* Structured JSON output
* Automated graph routing test

---

## Workflow

User Question

↓

Triage Node

↓

Retrieval Node (FAISS)

↓

Generation Node (TinyLlama)

↓

Verification Node

↓

Final Response

---

## Models Used

### Embedding Model

* sentence-transformers/all-MiniLM-L6-v2

### Generation Model

* TinyLlama/TinyLlama-1.1B-Chat-v1.0

---

## Technologies

* Python
* LangGraph
* Hugging Face Transformers
* Sentence Transformers
* FAISS
* PyTorch
* NumPy
* PyTest

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python src/main.py
```

---

## Run Tests

```bash
pytest
```

---

## Sample Test Cases

* Answerable question
* Multi-document retrieval
* Clarification request
* Out-of-scope request
* Verification fallback

---

## Project Structure

```text
src/
data/
tests/
outputs/
README.md
requirements.txt
graph_diagram.jpeg
```

---

## Hardware Used

* Operating System: Windows 10
* Python: 3.10
* Device: CPU
* RAM: 8 GB (or your actual RAM)

---

## AI Assistance Disclosure

AI coding assistance was used to help implement, debug, and document this project. All code was reviewed, tested, and executed locally before submission.
