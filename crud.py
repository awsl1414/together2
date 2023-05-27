from fastapi import APIRouter
from typing import List, Union
from models import Info

from schemas import Info_Pydantic, InfoIn_Pydantic

app01 = APIRouter()


@app01.get("/info/all", summary="查询所有", response_model=List[Info_Pydantic])
async def info_all(limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    return await Info_Pydantic.from_queryset(Info.all().offset(skip).limit(limit))


@app01.post("/info/add", summary="添加信息", response_model=Info_Pydantic)
async def info_add(name: str, tel: int):
    info_obj = await Info.create(name=name, tel=tel)
    return await InfoIn_Pydantic.from_tortoise_orm(info_obj)


@app01.post("/info/query", summary="查询信息")
async def info_query(limit: int = 10, page: int = 1, name: Union[str, None] = None):
    skip = (page - 1) * limit
    return await Info_Pydantic.from_queryset(
        Info.filter(name=name).offset(skip).limit(limit)
    )


@app01.put("/info/update", summary="更新信息")
async def info_update(name: str, tel: int):
    return await Info.filter(name=name).update(tel=tel)


@app01.delete("/info/delete", summary="删除信息")
async def info_delete(name: str):
    if await Info.filter(name=name).delete():
        return {"msg": "删除失败"}
    return {"msg": "成功"}
