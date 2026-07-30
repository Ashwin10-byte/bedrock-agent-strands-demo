# Amazon Bedrock for Beginners – From First Prompt to AI Agent

[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![AWS Bedrock](https://img.shields.io/badge/AWS-Amazon%20Bedrock-orange.svg)](https://aws.amazon.com/bedrock/)
[![Framework](https://img.shields.io/badge/Framework-Strands%20Agents-purple.svg)](https://strandsagents.com/)

Companion repository for the YouTube video and blog: **Amazon Bedrock for Beginners – From First Prompt to AI Agent**.

This repo contains code samples that take you from your first Bedrock API call to a fully working AI agent. By the end, you'll build a **University FAQ Chatbot** equipped with:
- **Knowledge Bases (RAG)** for contextual document retrieval.
- **Guardrails** for content safety and policy enforcement.
- **Tool Use (Function Calling)** for dynamic course lookups.
- **Strands Agents SDK** to orchestrate all components into a coherent agent.

---

## 🏛️ System Architecture

The diagram below illustrates how the user interacts with the final Strands-powered Agent and how requests flow through Bedrock's foundational models, guardrails, vector database, and custom tools:

```mermaid
flowchart TD
    User([👤 User / Terminal]) <--> Agent[🤖 Strands Agent]
    
    subgraph AWS Bedrock Environment
        Agent <--> Guardrails{🛡️ Bedrock Guardrails}
        Guardrails -->|Blocked| BlockedMsg[❌ Blocked Response]
        
        Guardrails -->|Pass| LLM[🧠 Nova Lite LLM]
        
        LLM <-->|RAG Search| KB[(📚 Knowledge Base
S3 Vectors / FAQ Docs)]
        LLM <-->|Function Call| Tools[🔧 Course Lookup Tool]
    end

    LLM --> FinalAns[💬 Response to User]
```
