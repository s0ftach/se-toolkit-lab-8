import json
import os

config_path = "/app/nanobot/config.json"
workspace_path = "/app/nanobot/workspace"

with open(config_path) as f:
    config = json.load(f)

config["providers"]["custom"]["apiKey"] = os.environ.get("LLM_API_KEY", "")
config["providers"]["custom"]["apiBase"] = os.environ.get("LLM_API_BASE_URL", "")
config["agents"]["defaults"]["model"] = os.environ.get("LLM_API_MODEL", "coder-model")
config["agents"]["defaults"]["provider"] = "custom"
config["agents"]["defaults"]["workspace"] = workspace_path

config["gateway"]["host"] = os.environ.get("NANOBOT_GATEWAY_CONTAINER_ADDRESS", "0.0.0.0")
config["gateway"]["port"] = int(os.environ.get("NANOBOT_GATEWAY_CONTAINER_PORT", "18790"))

config["tools"]["mcpServers"]["lms"]["env"]["NANOBOT_LMS_BACKEND_URL"] = os.environ.get("NANOBOT_LMS_BACKEND_URL", "")
config["tools"]["mcpServers"]["lms"]["env"]["NANOBOT_LMS_API_KEY"] = os.environ.get("NANOBOT_LMS_API_KEY", "")
config["tools"]["mcpServers"]["lms"]["env"]["VICTORIALOGS_URL"] = os.environ.get("VICTORIALOGS_URL", "http://victorialogs:9428")
config["tools"]["mcpServers"]["lms"]["env"]["VICTORIATRACES_URL"] = os.environ.get("VICTORIATRACES_URL", "http://victoriatraces:10428")

if "webchat" not in config["channels"]:
    config["channels"]["webchat"] = {}
config["channels"]["webchat"]["enabled"] = True
config["channels"]["webchat"]["allow_from"] = ["*"]
config["channels"]["webchat"]["host"] = os.environ.get("NANOBOT_WEBCHAT_CONTAINER_ADDRESS", "0.0.0.0")
config["channels"]["webchat"]["port"] = int(os.environ.get("NANOBOT_WEBCHAT_CONTAINER_PORT", "8765"))
config["channels"]["webchat"]["access_key"] = os.environ.get("NANOBOT_ACCESS_KEY", "")

resolved_path = "/app/nanobot/config.resolved.json"
with open(resolved_path, "w") as f:
    json.dump(config, f, indent=2)

os.execvp("nanobot", ["nanobot", "gateway", "--config", resolved_path, "--workspace", workspace_path])
