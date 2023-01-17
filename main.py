from fastapi import FastAPI

app=FastAPI()

from tortoise.contrib.fastapi import register_tortoise
from tortoise import generate_config

db_config=generate_config(db_url='sqlite://db_file.sqlite',app_modules={'models':['model','aerich.models']})



register_tortoise(app=app,config=db_config)