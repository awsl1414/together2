from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

# 中间件配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许的域名，["*"]表示允许所有
    allow_credentials=True,  # 是否允许发送 Cookie
    allow_methods=["*"],  # 允许的 HTTP 方法；
    allow_headers=["*"],  # 允许的请求 Header
)

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=9000)
    # run("main:app", reload=True)
