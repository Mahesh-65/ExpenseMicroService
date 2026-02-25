from fastapi import FastAPI, Request
import httpx

app = FastAPI()

AUTH_URL = "http://auth-service:8001"
EXPENSE_URL = "http://expense-service:8002"

@app.api_route("/auth/{path:path}", methods=["GET", "POST"])
async def auth_proxy(path: str, request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            f"{AUTH_URL}/{path}",
            headers=request.headers.raw,
            content=await request.body()
        )
    return response.json()

@app.api_route("/expenses/{path:path}", methods=["GET", "POST"])
async def expense_proxy(path: str, request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            f"{EXPENSE_URL}/expenses/{path}",
            headers=request.headers.raw,
            content=await request.body()
        )
    return response.json()