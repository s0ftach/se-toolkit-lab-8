## Task 1A — Bare agent

**Q: What is the agentic loop?**

The agentic loop is the iterative cycle that AI agents follow to accomplish tasks. It typically consists of these core steps:

1. Perceive — Gather information from the environment (user input, files, APIs, tools, etc.)
2. Think/Reason — Process the information, plan actions, and make decisions
3. Act — Execute actions using available tools (read/write files, run commands, call APIs, etc.)
4. Observe — Receive feedback from the actions taken (outputs, errors, results)
5. Repeat — Continue the loop until the goal is achieved or a stopping condition is met

**Q: What labs are available in our LMS?**

The agent hallucinated — it looked at local workspace files instead of querying the LMS backend, because it has no tools yet.


## Task 1B — Agent with LMS tools

**Q: What labs are available?**

Lab ID | Title
-------|------
Lab 01 | Products, Architecture & Roles
Lab 02 | Run, Fix, and Deploy a Backend Service
Lab 03 | Backend API: Explore, Debug, Implement, Deploy
Lab 04 | Testing, Front-end, and AI Agents
Lab 05 | Data Pipeline and Analytics Dashboard
Lab 06 | Build Your Own Agent
Lab 07 | Build a Client with an AI Coding Agent
Lab 08 | lab-08

**Q: Describe the architecture of the LMS system**

The LMS is a multi-service platform following a microservices architecture orchestrated via Docker Compose. Core components: LMS Backend (FastAPI), Nanobot Agent (AI interface), MCP Server (exposes LMS tools), React/Flutter frontends, PostgreSQL database, Qwen Code API (LLM proxy), Observability stack (VictoriaLogs, VictoriaTraces, OTel Collector), and Caddy as reverse proxy/gateway.

## Task 1C — Skill prompt

**Q: Show me the scores**

The agent fetched pass rates for all labs and displayed them in a table format with average scores and attempt counts per task. It showed data for Labs 01-08, with key insights like highest average score (Lab 07 Task 1 at 76.9%) and most attempts (Lab 01 setup at 3,124).
