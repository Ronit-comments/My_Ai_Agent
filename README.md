# 🤖 FRIDAY AI — Personal AI Assistant

FRIDAY is a personal AI assistant project inspired by Tony Stark's FRIDAY.

The goal of this project is to gradually build a Python-based AI assistant that can understand user requests, route them to the appropriate functionality, interact with the computer, search the web, work with PDFs and files, perform calculations, and maintain useful conversation memory.

This project is being developed step-by-step as I learn AI, APIs, automation, memory systems, and agent-based architectures.

> 🚧 **Status: Active Development**
>
> 🧠 **Current Milestone: Shared Memory Integration**

---

# 🎯 Project Goal

The long-term goal is to build a personal AI assistant that can:

* Understand natural-language requests
* Maintain conversation context
* Remember important information
* Perform calculations
* Search and interact with the web
* Search information from PDFs
* Work with files
* Open and control applications
* Automate computer tasks
* Eventually support voice interaction
* Eventually become a more autonomous AI agent

The project is being built incrementally rather than trying to implement everything at once.

---

# 🧠 Current Capabilities

FRIDAY currently contains the following components:

### 🗣️ Gemini Conversation

FRIDAY uses Google's Gemini API for normal conversations.

It can:

* Answer general questions
* Understand conversation context
* Generate natural-language responses
* Use stored memory when relevant

---

### 🧭 Request Router

FRIDAY has an `agent_router.py` module that classifies user requests.

Depending on the request, FRIDAY can route it toward:

```text
User Request
     │
     ▼
Agent Router
     │
     ├── Computer
     ├── Web
     ├── Calculator
     ├── PDF
     ├── File
     └── Conversation
```

The router is currently used to decide which part of the system should handle a request.

> Note: This project is **not currently a multi-agent system**. These are task-specific modules/functions that are routed by the main FRIDAY controller.

---

# 💻 Computer Control

FRIDAY includes a computer-control component through:

```text
computer_loop.py
```

This is intended to allow FRIDAY to perform computer-related tasks based on user instructions.

The computer-control functionality is still under active development.

Future improvements will make computer interaction more reliable and capable.

---

# 🌐 Web Tasks

FRIDAY includes:

```text
web_agent.py
```

which handles web-related requests.

The goal is to allow FRIDAY to perform tasks involving websites and web information.

---

# 🛠️ Utility Tasks

FRIDAY includes a utility system for handling tasks such as:

* Calculations
* PDF searches
* File-related operations

The utility functionality is handled through:

```text
utility_agent.py
```

and supporting tools.

---

# 📄 PDF Search

FRIDAY includes a PDF search capability through:

```text
pdf_tool.py
```

This allows the system to search information from PDFs instead of relying only on the model's existing knowledge.

This functionality is part of the foundation for eventually expanding FRIDAY into a more advanced document/RAG system.

---

# 🧠 Memory System

One of the major milestones in the project is the addition of a shared memory system.

FRIDAY currently has three memory components.

```text
              FRIDAY
                 │
                 ▼
          Memory Manager
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
   Short-Term  Long-Term  Semantic
     Memory      Memory    Memory
```

---

## 1. Short-Term Memory

Short-term memory stores recent conversation messages.

It allows FRIDAY to use recent conversation context when answering follow-up questions.

For example:

```text
User: I am learning Python.

User: What should I learn next?
```

FRIDAY can use the previous conversation to understand what the second question refers to.

---

## 2. Long-Term Memory

Long-term memory stores conversation information in a persistent database.

This provides a foundation for remembering information beyond the immediate conversation.

---

## 3. Semantic Memory

FRIDAY also has a semantic memory system.

Important information can be analyzed and stored as semantic memories.

For example:

```text
User:
I am building a personal AI assistant called FRIDAY.
```

The memory extraction system can determine that this information may be useful to remember.

Later, FRIDAY can retrieve relevant semantic information when answering a request.

---

# 🧩 Memory Manager

The project now contains:

```text
memory_manager.py
```

This provides a common interface for working with the different memory components.

The memory manager is responsible for:

* Retrieving recent conversation history
* Retrieving long-term memories
* Searching semantic memories
* Building relevant context
* Saving conversations
* Analyzing important information
* Saving important semantic memories

The general flow is:

```text
User Request
     │
     ▼
Memory Manager
     │
     ├── Recent Conversation
     ├── Long-Term Memory
     └── Semantic Memory
             │
             ▼
        Build Context
             │
             ▼
          Gemini
             │
             ▼
          Response
             │
             ▼
       Save Conversation
             │
             ▼
     Analyze Important Info
             │
             ▼
      Semantic Memory
```

---

# 🏗️ Current Project Structure

```text
FRIDAY/
│
├── friday_agent.py
│
├── agent_router.py
├── computer_loop.py
├── web_agent.py
├── utility_agent.py
│
├── memory_manager.py
├── memory.py
├── long_term_memory.py
├── semantic_memory.py
├── memory_extractor.py
├── context_manager.py
│
├── tools.py
├── pdf_tool.py
│
├── .env
├── .gitignore
└── README.md
```

---

# 🔄 How FRIDAY Currently Works

The main flow of the application is:

```text
                    ┌───────────────┐
                    │     USER      │
                    └───────┬───────┘
                            │
                            ▼
                   ┌────────────────┐
                   │ friday_agent.py│
                   └───────┬────────┘
                           │
                           ▼
                   ┌────────────────┐
                   │ agent_router.py│
                   └───────┬────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
     Computer           Web            Utility
     Function           Agent           Agent
          │                │                │
          └────────────────┼────────────────┘
                           │
                           ▼
                    Gemini / Response
                           │
                           ▼
                    Memory Manager
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
         Short-Term   Long-Term    Semantic
           Memory       Memory      Memory
```

For normal conversation, FRIDAY retrieves relevant memory before sending the request to Gemini.

---

# 🔐 Environment Variables

FRIDAY uses a `.env` file to store the Gemini API key.

Create:

```env
GEMINI_API_KEY=your_api_key_here
```

Never commit your `.env` file to GitHub.

Recommended `.gitignore` entries:

```gitignore
.env
__pycache__/
*.pyc
```

---

# 📦 Installation

Clone the repository and install the required dependencies.

```bash
pip install google-genai python-dotenv
```

Additional dependencies may be required depending on the computer-control, PDF, web, and memory components being used.

---

# ▶️ Running FRIDAY

Run:

```bash
python friday_agent.py
```

FRIDAY will start with:

```text
====================================
          🤖 FRIDAY AI
====================================

Type 'exit' to stop.

You:
```

Enter:

```text
exit
```

to stop the assistant.

---

# 🧪 Example

A normal conversation might look like:

```text
You: My favorite programming language is Python.

🧠 FRIDAY is thinking...
📌 Task type: conversation

🤖 FRIDAY:
That's great! Python is an excellent language
for AI and machine learning.
```

Later:

```text
You: What is my favorite programming language?

🧠 FRIDAY is thinking...
📌 Task type: conversation

🤖 FRIDAY:
Your favorite programming language is Python.
```

This demonstrates the purpose of the newly integrated memory system.

---

# 🛠️ Technologies

Current technologies used in the project include:

* Python
* Google Gemini API
* Google GenAI SDK
* python-dotenv
* Database-based memory
* Semantic memory
* PDF processing
* Computer automation
* Web automation/search
* Modular Python architecture

---

# 📌 Current Milestone

## Shared Memory Integration

The current milestone focuses on making FRIDAY capable of maintaining information across conversations.

Previously, the system primarily processed the current request.

Now, the system can retrieve:

```text
Recent Conversation
        +
Long-Term Memory
        +
Semantic Memory
        ↓
   Relevant Context
        ↓
      Gemini
```

This provides the foundation for making FRIDAY feel more like a persistent personal assistant rather than a simple chatbot.

---

# 🚧 Current Limitations

FRIDAY is still under development.

Currently:

* The project is not a true multi-agent system.
* The router uses task categories to select existing functionality.
* Computer automation is still being developed.
* Web automation is still being developed.
* Memory retrieval can still be improved.
* Semantic memory extraction can be improved.
* Voice interaction has not yet been implemented.
* Autonomous planning has not yet been implemented.
* The system is not yet fully autonomous.

These are intentional future development areas.

---

# 🔮 Future Goals

The planned development path includes:

## Phase 1 — Core Assistant

* [x] Gemini integration
* [x] Request classification
* [x] Normal conversation
* [x] Calculator functionality
* [x] PDF search
* [x] Basic computer tasks
* [x] Web tasks

## Phase 2 — Memory

* [x] Short-term memory
* [x] Long-term memory
* [x] Semantic memory
* [x] Memory extraction
* [x] Context management
* [x] Shared memory manager
* [ ] Improve memory relevance
* [ ] Improve memory retrieval
* [ ] Better memory cleanup

## Phase 3 — Computer Assistant

* [ ] More reliable application control
* [ ] Better file management
* [ ] Browser control
* [ ] Application launching
* [ ] More advanced computer automation
* [ ] Task verification

## Phase 4 — Voice

* [ ] Speech-to-text
* [ ] Text-to-speech
* [ ] Wake word
* [ ] Voice commands
* [ ] Voice responses

## Phase 5 — Advanced AI Agent

* [ ] Task planning
* [ ] Multi-step task execution
* [ ] Better tool selection
* [ ] Self-verification
* [ ] Agentic workflows
* [ ] More advanced reasoning

## Phase 6 — FRIDAY Interface

* [ ] FRIDAY-inspired UI
* [ ] Real-time activity display
* [ ] Memory visualization
* [ ] Task status
* [ ] Voice interface
* [ ] Computer activity monitoring

## Phase 7 — Advanced Architecture

Once the core system is stable, the project may evolve toward:

* [ ] True multi-agent architecture
* [ ] Agent-to-agent communication
* [ ] Agent orchestration
* [ ] LangGraph integration
* [ ] FastAPI backend
* [ ] React frontend
* [ ] RAG improvements
* [ ] Advanced tool calling
* [ ] Deployment

---

# 📈 Development Philosophy

FRIDAY is being built incrementally.

Instead of immediately using a large collection of frameworks, the project is being developed from the fundamentals:

```text
Python
   ↓
APIs
   ↓
Gemini
   ↓
Tools
   ↓
Task Routing
   ↓
Computer/Web/PDF Functions
   ↓
Memory
   ↓
Context Management
   ↓
Advanced Agent Architecture
   ↓
Multi-Agent System
```

This approach makes it easier to understand how each part of the assistant actually works.

---

# 🎯 Long-Term Vision

The long-term vision is to build FRIDAY into a personal AI system capable of understanding natural language and taking useful actions on the user's computer.

The eventual system should be able to move from:

```text
"Answer my question."
```

toward:

```text
"Understand what I want,
plan what needs to happen,
use the appropriate tools,
perform the task,
verify the result,
and remember what is important."
```

The current memory milestone is an important step toward that goal.

---

# 📊 Project Status

| Component               | Status        |
| ----------------------- | ------------- |
| Python Core             | 🟢 Working    |
| Gemini Integration      | 🟢 Working    |
| Request Router          | 🟢 Working    |
| Normal Conversation     | 🟢 Working    |
| Calculator              | 🟢 Working    |
| PDF Search              | 🟢 Working    |
| Web Tasks               | 🟡 Developing |
| Computer Control        | 🟡 Developing |
| Short-Term Memory       | 🟢 Working    |
| Long-Term Memory        | 🟢 Working    |
| Semantic Memory         | 🟢 Working    |
| Memory Manager          | 🟢 Integrated |
| Voice                   | 🔴 Planned    |
| Advanced Planning       | 🔴 Planned    |
| True Multi-Agent System | 🔴 Future     |
| FRIDAY UI               | 🔴 Planned    |

---

# 🚀 Current Milestone Summary

**Milestone:** Shared Memory Integration

FRIDAY can now use a centralized memory system consisting of:

```text
Short-Term Memory
       +
Long-Term Memory
       +
Semantic Memory
       ↓
Memory Manager
       ↓
Relevant Context
       ↓
FRIDAY Response
```

This milestone establishes the foundation for the next stage of development: making FRIDAY more capable at understanding context, performing computer tasks, and eventually becoming a more autonomous personal AI assistant.

---

## 👨‍💻 Author

**Ronit Soni**

AI/ML Learner | Python Developer | Building FRIDAY

---

## ⭐ Project Status

🚧 **Actively building and improving FRIDAY**

This repository documents the development journey from a basic Python AI assistant toward a more capable personal AI system.
