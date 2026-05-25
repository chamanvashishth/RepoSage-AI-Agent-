from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.repository import router as repository_router
from app.api.websocket.activity import ws_router

app = FastAPI(title="RepoSage API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(repository_router, prefix="/api/repository", tags=["repository"])
app.include_router(ws_router)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
