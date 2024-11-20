import os
from sys import prefix

import uvicorn
from fastapi import FastAPI
from fastapi import Request, Response, APIRouter
from starlette.middleware.cors import CORSMiddleware

from apps.todoList.todo import todo
from apps.student.student import student_app
from tortoise.contrib.fastapi import register_tortoise
from settings.settings import TORTOISE_ORM
# from apps.class_views.demo import class_view_router

import time

app = FastAPI(debug=True)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.include_router(todo, prefix='/todo', tags=['todo'])
app.include_router(student_app, prefix='/student', tags=['student'])


# app.include_router(class_view_router, prefix='/te', tags=['te'])

##注册数据库
register_tortoise(
    app=app,
    config=TORTOISE_ORM,
    generate_schemas=True,  # 如果数据库为空，则自动生成对应表单，生产环境不要开
    add_exception_handlers=True,  # 生产环境不要开，会泄露调试信息
)
origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=["*"])  #noqa


if __name__ == '__main__':
    os.environ['PYTHONASYNCIODEBUG'] = '1'
    uvicorn.run("main:app", host="0.0.0.0", port=5800, reload=True, workers=2,loop="uvloop")
