from tortoise.contrib.fastapi import register_tortoise


from fastapi import APIRouter

from apps.student.models import Student

student_app = APIRouter()
app = student_app


@app.get('/{}')
async def student():
    # 获取id为100的用户，如果数据不存在，将返回 `None`
    student = await Student.get_or_none(id=100)
    if student:
        print(student.name)
    else:
        print("student not found")