from fastapi import FastAPI, Request
from typing import Callable
from fastapi.templating import Jinja2Templates
from fastapi.responses import StreamingResponse, HTMLResponse
from datetime import datetime
import asyncio
import random
from typing import AsyncGenerator

app = FastAPI()

templates = Jinja2Templates(directory="public")

# Serve the root page using Jinja2Templates
@app.get("/", response_class=HTMLResponse)
async def serve_root_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Reusable event generator function
async def event_generator(data_func: Callable[[], str], interval: int) -> AsyncGenerator[str, None]:
    while True:
        yield f"data: {data_func()}\n\n"
        await asyncio.sleep(interval)

# SSE endpoint to send the current time to the client
@app.get("/synchronizetime")
async def synchronizetime() -> StreamingResponse:
    return StreamingResponse(event_generator(lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 1), media_type="text/event-stream")

# SSE endpoint to send a random joke to the client
@app.get("/jokes")
async def jokes() -> StreamingResponse:
    return StreamingResponse(event_generator(send_random_joke_to_client, 10), media_type="text/event-stream")

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