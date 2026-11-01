# Trip Buddy agent

One AI trip planner for a group of friends, built up in 15 small lessons: a SQLite database, embeddings and ChromaDB retrieval, an LLM chain, RAG, tool calling, a ReAct agent with a Gradio chat UI, an MCP server, short- and long-term memory, and a second agent reached over A2A.

The write-up, with every command, error and fix from my run, is on my blog: [Trip Buddy: one agent, built up in 15 lessons](https://vineetganti.com/blog/trip-buddy-agent).

## Credits

The lesson code comes from **Scaler Academy's AI Bootcamp**, which my [Agentic AI blog series](https://vineetganti.com/blog/series/agentic-ai) follows. All credit for the lessons and the Trip Buddy story goes to them. My changes, made with Claude Code while running the lessons:

- `pyproject.toml`, so `uv sync` can build the environment (the files came with a `uv.lock` but no project file).
- `trip_llm.py`, a shared `make_llm()` that every LLM lesson calls. It uses Google Gemini through LangChain's native `ChatGoogleGenerativeAI` client instead of OpenAI, because tool calls through Gemini's OpenAI-compatible endpoint failed with a 400 on the second turn.
- `.env.example` with the two Gemini settings, and a default model that new API keys can use.

## The lessons

| Files | Topic | Needs a key? |
| --- | --- | --- |
| `trip_01` – `trip_03` | SQLite, sentence embeddings, ChromaDB retrieval with metadata filters | No |
| `trip_04` – `trip_05` | An LLM chain (prompt → model → parser), then RAG | Yes |
| `trip_06` – `trip_08` | Tool calling, a fixed two-chain pipeline, then the full agent with a Gradio UI | Yes |
| `trip_mcp_server.py`, `trip_09` – `trip_10` | An MCP server (tools, resources, prompts), a hand-driven client, then the agent using it | 09: no, 10: yes |
| `trip_memory.py`, `trip_11` – `trip_13` | Semantic, episodic and procedural memory, the save pipeline, and an agent that remembers | 11: no, 12–13: yes |
| `trip_guide_agent.py`, `trip_14` – `trip_15` | A Local Guide agent over A2A, a hand-driven client, then Trip Buddy asking it for help | Yes |

## Run it

You need Python 3.11+ and [uv](https://docs.astral.sh/uv/getting-started/installation/).

```powershell
git clone https://github.com/vineetganti/trip-buddy-agent.git
cd trip-buddy-agent
uv sync                              # creates .venv from pyproject.toml and uv.lock
Copy-Item .env.example .env          # then paste your key after GEMINI_API_KEY=
uv run trip_01_sqlite_basics.py
```

Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey). `GEMINI_MODEL` defaults to `gemini-flash-lite-latest`; `gemini-2.5-flash` returned a 404 for a new key.

If `uv` isn't on your PATH (for example, you installed it with `pip`), use `python -m uv run <file>`, or activate `.venv` and run `python <file>`.

- **Gradio apps** (lessons 08, 10, 13, 15) open at http://127.0.0.1:7860.
- **MCP** (lessons 09 and 10): you don't start `trip_mcp_server.py` yourself. The client lessons launch it as a subprocess over stdio.
- **A2A** (lessons 14 and 15): start the guide first and leave it running.

  ```powershell
  uv run trip_guide_agent.py           # terminal 1, serves http://127.0.0.1:9999
  uv run trip_14_a2a_client_demo.py    # terminal 2
  ```

  Its Agent Card is at http://127.0.0.1:9999/.well-known/agent-card.json.
- **Memory** (lessons 11–13) is saved in `memory_store/` and `memory_store_demo/`: a SQLite file `long_term.db` for facts and rules, and a ChromaDB folder `episodes/` for past trips. Delete the folders, or use the app's **Forget everything** button, to start clean.

Keep `.env` out of git. It's already in `.gitignore`.
