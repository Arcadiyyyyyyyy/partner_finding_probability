import uvicorn
from fastapi import FastAPI
from src import calculate_router, general_router


app = FastAPI()
app.include_router(general_router)
app.include_router(calculate_router)


if __name__ == "__main__":
    """Launched with `poetry run python app` at root level"""
    uvicorn.run("app.__main__:app", host="0.0.0.0", port=8000, reload=True)
