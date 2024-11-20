import os

from dotenv import load_dotenv

load_dotenv('../.env')

DEBUG = True if os.getenv('ENV') == 'dev' else False

TORTOISE_ORM = {
    "connections": {
        "default": {
            'engine': 'tortoise.backends.sqlite',
            'credentials': {
                'file_path': './db/db.sqlite3',

            }
        }
    },
    "apps": {
        "models": {
            "models": [
                "apps.student.models",
                "apps.todoList.models",
                "aerich.models"
            ],
            "default_connection": "default",
        }
    },
    "use_tz": False,  # 建议不要开启，不然存储日期时会有很多坑，时区转换在项目中手动处理更稳妥。
    "timezone": "Asia/Shanghai"
}
