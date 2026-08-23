import json
from typing import Any

from .config import Settings
from .model import generate_reply


def handler(event: dict[str, Any], _context: Any) -> dict[str, Any]:
    """Yandex Cloud Function entry point."""
    body = event.get("body", event)
    if isinstance(body, str):
        body = json.loads(body or "{}")
    question = str(body.get("question", "")).strip()
    if not question:
        return {"statusCode": 400, "body": json.dumps({"error": "question is required"})}

    answer = generate_reply(question, Settings())
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"answer": answer}, ensure_ascii=False),
    }
