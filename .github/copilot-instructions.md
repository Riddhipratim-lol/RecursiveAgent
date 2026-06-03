# GitHub Copilot Repository Instructions: LangChain & LangGraph (Modern Stack)

You are an expert AI Engineer specializing in LangChain (LCEL) and LangGraph. When generating ghost text, autocomplete blocks, refactoring, or chatting, you must strictly adhere to the following production-grade architecture patterns, library versions, and coding styles.

---

## 1. Framework Separation & Paradigm Choice
* **LangChain (LCEL) for Chains:** Use LangChain Expression Language (LCEL) with the pipe (`|`) operator for linear sequences (e.g., Prompt | Model | Parser) or straightforward Retrieval-Augmented Generation (RAG) pipelines.
* **LangGraph for Agents:** Shift to LangGraph whenever the system requires multi-turn loops, conditional branching, human-in-the-loop interventions, state persistence, or multi-agent orchestration.

---

## 2. Recommended Repository Layout & Code Structure
Adhere to this modular, clear separation of configuration, orchestration, chains, and tools:

```text
my_agent_project/
│
├── .github/
│   └── copilot-instructions.md  # This configuration file
├── src/
│   ├── chains/
│   │   ├── __init__.py
│   │   ├── rag_chain.py        # Standalone LangChain LCEL chains
│   │   └── extraction_chain.py # LangChain Structured Output setups
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── state.py            # Pydantic state schemas for LangGraph
│   │   ├── nodes.py            # Graph business logic & LLM invocations
│   │   └── graph.py            # LangGraph compilation & checkpointing
│   ├── tools/
│   │   └── custom_tools.py     # LangChain @tool definitions used by both
│   └── main.py                 # Application entry point / execution loop
├── requirements.txt            # Explicit pinned versions
└── README.md