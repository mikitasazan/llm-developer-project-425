### Hexlet tests and linter status:
[![Actions Status](https://github.com/mikitasazan/llm-developer-project-425/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/mikitasazan/llm-developer-project-425/actions)
## Support agent

This repository contains the first deployable slice of the support agent:

- `src/helpdesk_agent/handler.py` is a Yandex Cloud Function entry point;
- `src/helpdesk_agent/model.py` calls a Yandex AI Studio endpoint and has a
  safe local fallback;
- `.env.example` documents runtime configuration without storing secrets.

Run local checks with:

```bash
PYTHONPATH=src python -m pytest
```

Set `AISTUDIO_API_KEY` and `AISTUDIO_MODEL_URI` before deploying the function.
