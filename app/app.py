from fastapi import FastAPI

from app.routes import main_router


def create_app() -> FastAPI:
    """
    Returns FastAPI instance
    """
    app = FastAPI()
    app.include_router(router=main_router)

    return app
