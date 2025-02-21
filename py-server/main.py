from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from typing import AsyncGenerator, Callable
from datetime import datetime
import asyncio
import random

app = FastAPI()

# Serve static files from the 'public' directory
@app.get("/", response_class=HTMLResponse)
async def index() -> HTMLResponse:
    with open("public/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)

# Reusable event generator function
async def event_generator(
    request: Request, 
    data_func: Callable[[], str], 
    interval: int
    ) -> AsyncGenerator[str, None]:
    while True:
        if await request.is_disconnected():
            break
        yield f"data: {data_func()}\n\n"
        await asyncio.sleep(interval)

# SSE endpoint to send the current time to the client
@app.get("/synchronizetime")
async def synchronizetime(request: Request) -> StreamingResponse:
    
    return StreamingResponse(event_generator(
        request=request,
        data_func=send_time_to_client,
        interval=1
        ), media_type="text/event-stream")

# SSE endpoint to send a random joke to the client
@app.get("/jokes")
async def jokes(request: Request) -> StreamingResponse:
    
    return StreamingResponse(event_generator(
        request=request,
        data_func=send_random_joke_to_client,
        interval=10
        ), media_type="text/event-stream")

def send_time_to_client() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def send_random_joke_to_client() -> str:
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the bicycle fall over? Because it was two-tired!"
    ]
    
    return jokes[random.randint(0, len(jokes) - 1)]

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)