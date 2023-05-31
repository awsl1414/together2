from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from uvicorn import run
from crud import app01

app = FastAPI()
app.include_router(app01)
register_tortoise(
    app,
    db_url="sqlite://together2.sqlite",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == "__main__":
    run("main:app", reload=True)
