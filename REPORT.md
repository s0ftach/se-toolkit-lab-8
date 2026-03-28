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

## Task 2B — Web client

Asked "What can you do in this system?" — agent listed all capabilities including LMS tools, file management, web search, memory system, and scheduling.

Asked "Which lab has the lowest pass rate?" — agent called lms_labs then lms_completion_rate for each lab and returned:
- Lab 02 and Lab 03 tied at 89.1% completion rate
- Lab 08 has 0% but no students enrolled yet

## Task 3C — Observability MCP tools

**Normal conditions:**
No errors in the last hour. The backend service shows 0 errors in the past 60 minutes.

**With PostgreSQL stopped:**
Yes, there are 5 errors in the last hour:
- 4 recent db_query errors: `[Errno -2] Name or service not known` (DNS/connection issues reaching the database)
- 1 older UniqueViolationError from pipeline sync (duplicate key on learner_external_id_key)

## Task 4A — Multi-step investigation

With PostgreSQL stopped, asked "What went wrong?". The agent used logs_error_count and logs_search tools to find db_query errors with "[Errno -2] Name or service not known" indicating the backend could not reach the database. Trace ID was extracted and traces_get was called to confirm the failure span.

## Task 4B — Proactive health check

Created a health check cron job running every 2 minutes. While PostgreSQL was stopped, the agent proactively reported database connection errors in the chat. After restarting PostgreSQL, the agent reported the system looks healthy.

## Task 4C — Bug fix and recovery

**Root cause:** In `backend/app/routers/items.py`, the `get_items` endpoint caught all exceptions and raised `HTTP 404 Not Found` instead of letting the real error propagate. This masked database connection failures as "Items not found".

**Fix:** Removed the try/except block from `get_items` so exceptions propagate to the global exception handler which returns HTTP 500 with the real error details.

**Post-fix failure check:** After fix, stopping PostgreSQL and calling GET /items/ returns:
`{"detail": "[Errno -2] Name or service not known", "type": "gaierror", "path": "/items/"}` with status 500.

**Healthy follow-up:** After restarting PostgreSQL, GET /items/ returns 200 with the full items list.
