from fastapi import FastAPI, Request, Response
import httpx

app = FastAPI()

AUTH_URL = "http://auth-service:8001"
EXPENSE_URL = "http://expense-service:8002"

@app.get("/")
def health():
    return {"status": "healthy"}

@app.api_route("/auth/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def auth_proxy(path: str, request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            f"{AUTH_URL}/{path}",
            headers=dict(request.headers),
            content=await request.body()
        )

    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=dict(response.headers)
    )

@app.api_route("/expenses/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def expense_proxy(path: str, request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method,
            f"{EXPENSE_URL}/{path}",
            headers=dict(request.headers),
            content=await request.body()
        )

    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=dict(response.headers)
    )
