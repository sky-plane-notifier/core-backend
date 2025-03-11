from fastapi import WebSocket
from typing import Annotated
from fastapi import Depends
from typing import Dict, List
from multipledispatch import dispatch
from fastapi.websockets import WebSocketDisconnect

class WebSocketConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, client_id: str, websocket: WebSocket):
        await websocket.accept()
        if client_id not in self.active_connections:
            self.active_connections[client_id] = []
        self.active_connections[client_id].append(websocket)
        print(f"Client with id => {client_id} connected")

    @dispatch(str, WebSocket)
    def disconnect(self, client_id: str, websocket: WebSocket):
        if client_id in self.active_connections:
            self.active_connections[client_id].remove(websocket)
            if not self.active_connections[client_id]:
                del self.active_connections[client_id]

    @dispatch(str)
    def disconnect(self, client_id: str):
        if client_id in self.active_connections:
            del self.active_connections[client_id]

    @dispatch(str, WebSocket, str)
    async def send_message(self, client_id: str, websocket: WebSocket, message: str):
        try:
            await websocket.send_text(message)
        except WebSocketDisconnect:
            self.disconnect(client_id, websocket)

    # send message to all connections of a specific client 
    @dispatch(str, str)
    async def send_message(self, message: str, client_id: str):
        if client_id in self.active_connections:
            for ws in self.active_connections[client_id]:
                try:
                    await self.send_message(message, client_id, ws)
                except WebSocketDisconnect:
                    self.disconnect(client_id, ws)
    
    @dispatch(str, WebSocket, dict)
    async def send_json(self, client_id: str, websocket: WebSocket, json: Dict):
        try:
            await websocket.send_json(json)
        except WebSocketDisconnect:
            self.disconnect(client_id, websocket)

    # send json to all connections of a specific client 
    @dispatch(str, dict)
    async def send_json(self, client_id: str, json: Dict):
        if client_id in self.active_connections:
            for ws in self.active_connections[client_id]:
                try:
                    await self.send_json(client_id, ws, json)
                except WebSocketDisconnect:
                    self.disconnect(client_id, ws)

    @dispatch(str)
    async def broadcast(self, message: str):
        for client_id, connections in self.active_connections.items():
            for ws in connections:
                try:
                    await self.send_message(client_id, ws, message)
                except WebSocketDisconnect:
                    self.disconnect(client_id, ws)

    @dispatch(dict)
    async def broadcast(self, json: Dict):
        for client_id, connections in self.active_connections.items():
            for ws in connections:
                try:
                    await self.send_json(client_id, ws, json)
                except WebSocketDisconnect:
                    self.disconnect(client_id, ws)

    def get_connections(self):
        return self.active_connections

manager = WebSocketConnectionManager()

def get_ws_manager():
    return manager

WSManagerDep = Annotated[WebSocketConnectionManager, Depends(get_ws_manager)]

__all__ = [WSManagerDep, get_ws_manager]