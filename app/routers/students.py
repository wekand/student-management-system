from fastapi import APIRouter, HTTPException, Depends
from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.service.student_service import add_student, lookup_student, remove_student, modify_student, \
    StudentAlreadyExistsError, StudentNotFoundError

Score = Annotated[int, Field(ge=0, le=100)]

class StudentData(BaseModel):
    id: int
    name: str
    score: Score

class StudentResponse(BaseModel):
    id: int
    name: str
    score: int

class MessageResponse(BaseModel):
    message: str

class StudentUpdate(BaseModel):
    name: str
    score: Score
router = APIRouter()
@router.get("/hello")
async def hello():
    return {"message": "Hello FastAPI"}

@router.get("/students/{id}", response_model=StudentResponse)
async def get_student(student_id: int,db:Session=Depends(get_db)):
    result = lookup_student(db,student_id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    return result

@router.post("/students",status_code=201,response_model=MessageResponse)
async def create_student(student: StudentData,db:Session=Depends(get_db)):
    try:
        add_student(db,student)
        return {"message": "已成功添加"}
    except StudentAlreadyExistsError:
        raise HTTPException(status_code=409, detail="Student Already Exists")


@router.delete("/students/{id}", status_code=200,response_model=MessageResponse)
async def delete_student(student_id: int,db:Session=Depends(get_db)):
    try:
        remove_student(db,student_id)
        return {"message": "已成功删除"}
    except StudentNotFoundError:
        raise HTTPException(status_code=404, detail="Student Not Found")
@router.put("/students/{id}",status_code=200,response_model=MessageResponse)
async def update_student(student_id: int, student_update: StudentUpdate,db:Session=Depends(get_db)):
    try:
        modify_student(db,student_id,student_update.name,student_update.score)
        return {"message": "已成功修改"}
    except StudentNotFoundError:
        raise HTTPException(status_code=404, detail="Student Not Found")