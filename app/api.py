from fastapi import APIRouter
from app.scanner import run_port_scan, run_ping_scan
from pydantic import BaseModel

router = APIRouter()

class ScanRequest(BaseModel):
    host: str
    ports: str = None

@router.post("/scan/port")
async def port_scan(request: ScanRequest):
    result = await run_port_scan(request.host, request.ports)
    return {"status": "success", "data": result}

@router.post("/scan/ping")
async def ping_scan(request: ScanRequest):
    result = await run_ping_scan(request.host)
    return {"status":"success", "data": result}