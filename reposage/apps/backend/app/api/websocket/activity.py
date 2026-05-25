from fastapi import APIRouter, WebSocket

ws_router = APIRouter()


@ws_router.websocket('/ws/activity')
async def activity_stream(websocket: WebSocket) -> None:
    await websocket.accept()
    await websocket.send_json({"event": "connected", "source": "reposage"})
    while True:
        message = await websocket.receive_text()
        await websocket.send_json({"event": "echo", "message": message})
