

# Fastapi、tortoise-orm 、fastapi_views Demo 项目

##  tortoise-orm 中使用  aerich


初始化 之后会多出来一个 `[migrations](migrations)` 文件夹
```shell
aerich init -t settings.settings.TORTOISE_ORM

Success create migrate location ./migrations
Success write config to pyproject.toml

 ```
根据模型生成一个sql 
```shell

aerich init-db
Success create app migrate location migrations/models
Success generate schema for app "models"

```

更新数据库

```shell
aerich  migrate && aerich upgrade

```


## 使用 
pydantic_sqlalchemy 和 fastapi_views  还有 tortoise-orm 之间会产生依赖冲突