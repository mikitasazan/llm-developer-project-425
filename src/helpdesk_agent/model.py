import json
import urllib.request

from .config import Settings


def generate_reply(question: str, settings: Settings) -> str:
    """Ask the configured model, with a deterministic local fallback."""
    if not settings.api_key or not settings.model_uri:
        return "Спасибо за вопрос. Мы получили обращение и передали его в службу поддержки."

    payload = {
        "modelUri": settings.model_uri,
        "completionOptions": {"stream": False, "temperature": 0.2, "maxTokens": 300},
        "messages": [
            {"role": "system", "text": "Ты вежливый оператор службы поддержки. Отвечай кратко и по делу."},
            {"role": "user", "text": question},
        ],
    }
    request = urllib.request.Request(
        settings.api_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Api-Key {settings.api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        body = json.loads(response.read().decode("utf-8"))
    return body["result"]["alternatives"][0]["message"]["text"]
