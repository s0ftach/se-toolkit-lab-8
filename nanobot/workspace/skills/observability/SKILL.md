# Observability Skill

You have access to logs and traces from the LMS system.

## Available tools

- `logs_search` — search logs with LogsQL query (e.g. `level:error`, `_stream:{service="backend"} AND level:error`)
- `logs_error_count` — count errors for a service over a time window (default: last 60 minutes)
- `traces_list` — list recent traces for a service
- `traces_get` — fetch a specific trace by ID

## Rules

- When user asks about errors, call `logs_error_count` first for a summary, then `logs_search` for details
- If you find a trace_id in the logs, call `traces_get` to show the full trace
- Never dump raw JSON — summarize findings: error count, affected endpoints, timestamps
- If no errors found, say so clearly
- Default service name is "backend"
