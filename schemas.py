from tortoise.contrib.pydantic import pydantic_model_creator
from models import Info

Info_Pydantic = pydantic_model_creator(Info, name="Info")
InfoIn_Pydantic = pydantic_model_creator(Info, name="InfoIn")
