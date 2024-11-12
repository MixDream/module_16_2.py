#.venv\Scripts\activate активация окружения
# uvicorn main:app --reload запуск фаст апи
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Hello World"}

@app.get("/user/{user_id}")
async def get_user(
    user_id: Annotated[int, Path(
        ge=1,
        le=100,
        description="Enter User ID",
        examples={
            "example1": {"value": 1},
            "example2": {"value": 50},
            "example3": {"value": 100}
        }
    )]
) -> dict:
    return {"message": f"User  ID: {user_id}"}

@app.get("/user/{username}/{age}")
async def get_user_info(
    username: Annotated[str, Path(
        min_length=5,
        max_length=20,
        description="Enter username",
        examples={
            "example1": {"value": "UrbanUser "},
            "example2": {"value": "TestUser "},
            "example3": {"value": "AnotherUser "}
        }
    )],
    age: Annotated[int, Path(
        ge=18,
        le=120,
        description="Enter age",
        examples={
            "example1": {"value": 24},
            "example2": {"value": 30},
            "example3": {"value": 120}
        }
    )]
) -> dict:
    return {"message": f"Hello, {username}, Age: {age}"}
