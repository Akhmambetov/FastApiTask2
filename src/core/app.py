from fastapi import FastAPI

from src.api.routes import router

def create_app() -> FastAPI:
    app = FastAPI(title="SSE TAsk 2")
    app.include_router(router)
    return app