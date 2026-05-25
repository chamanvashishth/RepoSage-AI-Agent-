# RepoSage

RepoSage is a production-oriented autonomous repository cognition and maintenance platform.
It combines repository analysis, AI-assisted issue reasoning, patch planning, validation workflows,
and pull-request generation into a single full-stack system.

## Core Capabilities

- Ingest GitHub repositories for analysis.
- Build repository cognition (imports, dependency relations, framework signals, topology summaries).
- Detect engineering issues (TODO/FIXME markers, cyclic dependencies, structural risk indicators).
- Persist semantic memory for prior analyses to support retrieval and learning loops.
- Expose API + WebSocket activity streams for orchestration and UI updates.
- Provide an interactive frontend dashboard for repository analysis and cognition visibility.

## Monorepo Structure

```text
reposage/
├── apps/
│   ├── backend/
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   ├── api/
│   │   │   ├── analysis/
│   │   │   ├── config/
│   │   │   ├── database/
│   │   │   ├── memory/
│   │   │   ├── schemas/
│   │   │   └── services/
│   │   ├── requirements.txt
│   │   └── tests/
│   └── frontend/
│       ├── app/
│       ├── components/
│       ├── services/
│       ├── store/
│       └── types/
├── docker/
├── .github/workflows/
├── docker-compose.yml
└── README.md
```

## Tech Stack

### Frontend
- Next.js (App Router)
- React + TypeScript
- Zustand

### Backend
- FastAPI
- Pydantic v2
- SQLAlchemy 2 (async)
- GitPython
- NetworkX
- ChromaDB

### Infrastructure
- Docker + Docker Compose
- GitHub Actions (backend/frontend/docker/security workflow stubs)

## Backend API

Base prefix: `/api/repository`

- `POST /analyze` — Analyze a repository URL and produce cognition + issue outputs.
- `GET /issues` — Return detected issues from latest analysis.
- `GET /graph?repository_url=...` — Return dependency graph nodes/edges.
- `GET /topology?repository_url=...` — Return topology summary.
- `GET /cognition?repository_url=...` — Return cognition metrics.
- `POST /fix` — Queue a fix intent for an issue.
- `POST /validate` — Return validation plan/check outputs.
- `POST /pull-request` — Produce PR payload summary.
- `GET /memory?query=...` — Query semantic memory store.
- `GET /activity` — Return activity events.

WebSocket:
- `WS /ws/activity` — Activity stream/echo channel.

## Local Development

### 1) Configure environment

Copy environment values from:

- `reposage/.env.example`

Set at minimum:
- `OPENAI_API_KEY` (if using OpenAI features)
- `GITHUB_CLIENT_ID`, `GITHUB_CLIENT_SECRET`
- `DATABASE_URL`
- `REDIS_URL`

### 2) Run with Docker Compose

From repository root:

```bash
docker compose -f reposage/docker-compose.yml up --build
```

Services:
- Backend API: `http://localhost:8000`
- Frontend: `http://localhost:3000`

### 3) Run backend directly (optional)

```bash
cd reposage/apps/backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Current Implementation Notes

- Repository analysis currently emphasizes Python import graph extraction and baseline issue detection.
- Framework detection is heuristic-based (`package.json`, Python project signals).
- Memory persistence is backed by ChromaDB via a local persistent path.
- Frontend dashboard currently includes a working repository analyze flow with live result state.

## Roadmap

- Add richer multi-language AST parsing (Tree-sitter backed pipeline).
- Expand autonomous patch generation + sandbox validation workflow.
- Add deeper architecture/topology visualization in frontend.
- Integrate GitHub OAuth + branch/commit/PR execution paths.
- Add comprehensive test suites and CI quality gates.

## License

TBD.
