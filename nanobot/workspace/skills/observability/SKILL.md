# Observability Skill

You have access to logs and traces from the LMS system.

## Available tools

- `logs_search` — search logs with LogsQL query (e.g. `severity:ERROR`, `_msg:db_query AND severity:ERROR`)
- `logs_error_count` — count errors for a service over a time window (default: last 60 minutes)
- `traces_list` — list recent traces for a service
- `traces_get` — fetch a specific trace by ID

## Rules

- When user asks about errors, call `logs_error_count` first for a summary, then `logs_search` for details
- If you find a trace_id in the logs, call `traces_get` to show the full trace
- Never dump raw JSON — summarize findings: error count, affected endpoints, timestamps
- If no errors found, say so clearly
- Default service name is "backend"

## When user asks "What went wrong?" or "Check system health"

Follow this exact sequence:
1. Call `logs_error_count` to get error summary
2. Call `logs_search` with query `severity:ERROR` to get recent error details
3. Extract any `trace_id` from the error log entries
4. Call `traces_get` with that trace_id to get the full trace
5. Summarize in one coherent response:
   - What failed (endpoint, operation)
   - What the error was (message, type)
   - Where in the trace the failure occurred
   - Likely root cause

## When user asks to create a health check

Use the cron tool to schedule a recurring job. The job should:
- Call `logs_error_count` with minutes=2
- If errors > 0, call `logs_search` with `severity:ERROR` and summarize
- Post result to the current chat
- If no errors, report "System looks healthy"
