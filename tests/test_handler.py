import json

from helpdesk_agent.handler import handler


def test_handler_returns_a_local_fallback_without_cloud_credentials():
    result = handler({"body": json.dumps({"question": "Где мой заказ?"})}, None)

    assert result["statusCode"] == 200
    assert "поддержки" in json.loads(result["body"])["answer"]


def test_handler_rejects_an_empty_question():
    result = handler({"body": "{}"}, None)

    assert result["statusCode"] == 400
