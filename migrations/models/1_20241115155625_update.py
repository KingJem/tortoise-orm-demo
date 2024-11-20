from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "todoList" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "content" VARCHAR(50) NOT NULL,
    "before_time" TIMESTAMP NOT NULL,
    "is_delete" INT NOT NULL,
    "create_time" TIMESTAMP NOT NULL,
    "update_time" TIMESTAMP NOT NULL,
    "done_time" TIMESTAMP NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "todoList";"""
