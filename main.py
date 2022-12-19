from models import Resume
from typing import List
from fastapi import FastAPI, HTTPException
from uuid import UUID, uuid4






db: List[Resume] = [
    Resume(
        id = UUID("78369526-b735-4145-a3a8-32e2148ce241"),
        first_name = "Malki",
        last_name = "Malov",
        email = "malovmalki@gmail.com",
        linkdin_link = "https://linkedin.com/in/malkimalov",
        github_link = "https://github.com/MalkiMalov",
        title = "B.Sc in bioinformatics | Python Developer | Data Science"        
    )
]

app = FastAPI()

@app.get("/")
async def root():
    return "Resume API"

@app.get("/resume/{user_id}")
async def show_resume(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(
        status_code=404,
        detail=f"User with id:{user_id} does not exists"
    )