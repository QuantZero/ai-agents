# Local AI Agent

A small local LLM agent that connects to an IMAP inbox, lists your most recent unread email, and summarizes an email on demand. It uses LangGraph + LangChain tools, and runs against a local Ollama model.

## Features

- Lists only the newest unread email to avoid scanning a large inbox
- Summarizes a specific email by IMAP UID
- Runs as a simple CLI loop

## Requirements

- Python 3.13+
- An IMAP mailbox (Gmail supported with App Password)
- Ollama running locally with the model configured in `main.py`

## Install

Using uv:

```bash
uv sync
```

Or with pip (inside a venv):

```bash
pip install -r <(python -m piptools compile pyproject.toml)
```

## Configuration

Create a `.env` file in this directory:

```bash
IMAP_HOST=imap.gmail.com
IMAP_USER=your_email@gmail.com
IMAP_PASSWORD=your_app_password
```

Notes:

- For Gmail, enable IMAP and generate an App Password.
- `IMAP_PASSWORD` must be present or the app will stop with a debug error.

## Run

```bash
python main.py
```

Then interact in the prompt:

```text
> list my unread emails
> summarize the most recent email
> quit
```

## How it works

- `list_unread_emails` tool: finds unread UIDs and returns only the newest email header
- `summarize_email` tool: fetches the email body and asks the local LLM for a concise summary
- LangGraph routes between the LLM and tool calls automatically

## Customization

- Change the model by editing `CHAT_MODEL` in `main.py`
- Add new tools by decorating functions with `@tool` and registering them in `llm.bind_tools`

## Troubleshooting

- If login fails, check `.env` values and IMAP settings
- Gmail requires 2FA + App Password; standard passwords will fail

## License

Add a license if you plan to share or distribute this project.
