from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base, User, Blog  # Import all models to ensure they're registered
from api.base_router import api_router


def include_router(app):
    app.include_router(api_router)


def star_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)
    return app


app = star_application()

@app.get("/")
def homepage():
    test_message = {"message": "Hello World"}
    return test_message

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)