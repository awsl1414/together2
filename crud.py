from fastapi import APIRouter
from typing import Union
from models import Info
from utils import Msg

from schemas import Info_Pydantic, InfoIn_Pydantic

app01 = APIRouter()


@app01.get("/info/all", summary="查询所有")
async def info_all(limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    return await Info_Pydantic.from_queryset(Info.all().offset(skip).limit(limit))


@app01.post("/info/add", summary="添加信息")
async def info_add(name: str, tel: str):
    if len(name) > 0 and len(tel) == 11:
        try:
            int(tel) / 2
        except:
            return Msg("电话输入有误！").msg()
        info_obj = await Info.create(name=name, tel=tel)
        return await InfoIn_Pydantic.from_tortoise_orm(info_obj)
    return Msg("姓名或电话输入有误！").msg()


@app01.post("/info/query", summary="查询信息")
async def info_query(name: str, limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    if len(name) > 0:
        return await Info_Pydantic.from_queryset(
            Info.filter(name=name).offset(skip).limit(limit)
        )
    return Msg("姓名输入有误！").msg()


@app01.put("/info/update", summary="更新信息")
async def info_update(tel: str, re_tel: str):
    if len(tel) == 11 and len(re_tel) == 11:
        try:
            int(tel) / 2
            int(re_tel) / 2
        except:
            return Msg("电话输入有误！")
        return await Info.filter(tel=tel).update(tel=re_tel)
    return Msg("电话输入有误！").msg()


@app01.delete("/info/delete", summary="删除信息")
async def info_delete(name: str):
    if len(name) > 0:
        if await Info.filter(name=name).delete():
            return Msg("成功").msg()
        return Msg("删除失败").msg()
    return Msg("姓名输入有误！").msg()
