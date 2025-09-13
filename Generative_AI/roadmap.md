# 18-Day GenAI Roadmap (Sep 13 – Sep 30, 2025)

## Week 1: Foundations + Core APIs

🎯 **Goal:** Build a strong foundation in Node.js + OpenAI/Gemini APIs + LLM fundamentals.

**Sep 13 (Sat) – Kickoff + Setup**
*   Install Node.js, Express.js, LangChain.js, LlamaIndex.js.
*   Explore OpenAI & Gemini SDKs (setup API keys).
*   First API call: text generation with OpenAI.
*   **Hands-on:** Express endpoint that returns a simple LLM response.

**Sep 14 (Sun) [Light] – Theory**
*   How LLMs work (transformers, embeddings, attention).
*   Tokens, context windows, temperature, top-p.
*   Reading: OpenAI & Gemini model families.

**Sep 15 (Mon) – Chat Completion APIs**
*   Build a chatbot with OpenAI Chat API.
*   Compare with Gemini Chat API.
*   **Hands-on:** Multi-turn Express chatbot API.

**Sep 16 (Tue) – LangChain Intro**
*   Basics of LangChain.js: Chains, Prompts, Memory.
*   Implement a conversational memory chain.
*   **Hands-on:** Q&A bot with LangChain memory.

**Sep 17 (Wed) – RAG Foundations**
*   What is RAG, why retrieval matters.
*   Intro to embeddings: OpenAI + Gemini.
*   Vector DBs: Pinecone / Weaviate / pgvector.
*   **Hands-on:** Embed + store + retrieve docs with OpenAI embeddings.

**Sep 18 (Thu) [Light] – Theory**
*   Context window & retrieval strategies.
*   RAG pipeline architecture.
*   LLM evaluation metrics (hallucination, factuality).

## Week 2: Deep Dive into RAG + Indexing

🎯 **Goal:** Build full RAG pipelines, experiment with hybrid search & LlamaIndex.

**Sep 19 (Fri) [Light] – Theory**
*   How LlamaIndex complements LangChain.
*   Document loaders, indices, query engines.
*   Hybrid RAG (semantic + keyword search).

**Sep 20 (Sat) – Vector Databases Hands-on**
*   Setup a vector DB (choose Pinecone / Weaviate / local pgvector).
*   Ingest docs, run similarity search.
*   **Hands-on:** Express route for semantic search.

**Sep 21 (Sun) – LangChain RAG**
*   Build a RAG pipeline with LangChain retriever.
*   Connect retriever → LLM.
*   **Hands-on:** Q&A on custom documents.

**Sep 22 (Mon) [Light] – Theory**
*   Evaluation of RAG systems.
*   Vector DB trade-offs (latency, scale).
*   Chunking strategies (sliding windows, semantic splits).

**Sep 23 (Tue) [Light] – Theory**
*   Chain of Thought (CoT) reasoning.
*   Prompt engineering strategies.
*   Zero-shot, few-shot, tool use prompts.

**Sep 24 (Wed) [Light] – Theory**
*   Fine-tuning vs adapters vs RAG.
*   Model orchestration with multiple providers.
*   Cost optimization for LLM APIs.

**Sep 25 (Thu) [Light] – Theory**
*   MCP (Model Context Protocol) intro.
*   Why MCP matters for tool interop & retrieval.
*   Future of agentic systems.

**Sep 26 (Fri) – LlamaIndex RAG**
*   Use LlamaIndex to index local PDFs.
*   Query engine → OpenAI.
*   **Hands-on:** LlamaIndex Express API.

## Week 3: Advanced Architectures + MCP

🎯 **Goal:** Hybrid RAG, multi-model use, and MCP integration.

**Sep 27 (Sat) – Hybrid RAG**
*   Combine keyword + semantic + reranking retrieval.
*   **Hands-on:** Hybrid retriever pipeline (LangChain + LlamaIndex).

**Sep 28 (Sun) – Tool Use + Multi-LLM Orchestration**
*   LangChain Agents + Tools.
*   Switching between OpenAI & Gemini dynamically.
*   **Hands-on:** Agent that chooses between models for tasks.

**Sep 29 (Mon) – MCP in Practice**
*   Explore Model Context Protocol SDK.
*   Connect external knowledge sources.
*   **Hands-on:** Simple MCP server + Node client.

**Sep 30 (Tue) – Wrap-up Integration**
*   Unify: Express app with LangChain + LlamaIndex + VectorDB + MCP.
*   Run end-to-end hybrid RAG chatbot with multi-model backend.
*   Document setup + architecture notes.