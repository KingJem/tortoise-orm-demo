import orjson
from fastapi import APIRouter
from starlette.responses import JSONResponse

from apps.todoList.models import todoListPydantic, TodoList
from fastapi import status

todo = APIRouter()
app = todo


@app.post('/', response_model=todoListPydantic, status_code=status.HTTP_201_CREATED)
async def create_todo(content: todoListPydantic) -> todoListPydantic:
    content_dict = orjson.loads(content.json())
    instance = await TodoList.create(**content_dict)
    return await todoListPydantic.from_tortoise_orm(instance)


@app.get('/{_id}')
async def get_todo(_id: int) -> todoListPydantic:
    instance = await TodoList.get_or_none(id=_id)
    if instance:
        return await todoListPydantic.from_tortoise_orm(instance)
    else:
        return JSONResponse({'msg': f"error,{_id} not found"})


@app.get('/')
async def get_todos():
    data =  await TodoList.all()
    return data


@app.put('/', response_model=todoListPydantic, )
async def update_todo(content: todoListPydantic) -> todoListPydantic:
    content_dict = orjson.loads(content.json())
    instance = await TodoList.update_or_create(**content_dict)
    return await todoListPydantic.from_tortoise_orm(instance)


@app.delete('/{_id}', response_model=todoListPydantic, )
async def delete_todo(_id: int) -> todoListPydantic:
    instance = await TodoList.filter(id=_id).delete()
    return await todoListPydantic.from_tortoise_orm(instance)
