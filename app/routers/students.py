from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from app.service.student_service import add_student, lookup_student, remove_student, modify_student

class StudentData(BaseModel):
    id: int
    name: str
    score: int

router = APIRouter()
@router.get("/hello")
async def hello():
    return {"message": "Hello FastAPI"}

@router.get("/students/{id}")
async def get_student(id: int):
    result=lookup_student(id)
    if result is None:
        raise HTTPException(status_code=404, detail="Student Not Found")
    return {"id":result.id,"name":result.name,"score":result.score}

@router.post("/students",status_code=201)
async def create_student(student_add: StudentData):
    try:
        result = add_student(student_add)
        if not result:
            raise HTTPException(status_code=409, detail="Student Already Exists")
        return {"message": "已成功添加"}
    except PermissionError:
        raise HTTPException(status_code=500,detail="Failed to Save Student Data")


@router.delete("/students/{id}", status_code=200)
async def delete_student(id: int):
    try:
        result=remove_student(id)
        if not result:
            raise HTTPException(status_code=404, detail="Student Not Found")
        return {"message": "已成功删除"}
    except PermissionError:
        raise HTTPException(status_code=500, detail="Failed to Save Student Data")


class StudentUpdate(BaseModel):
    name: str
    score: int


@router.put("/students/{id}",status_code=200)
async def update_student(id: int, student_update: StudentUpdate):
    try:
        result = modify_student(id,name=student_update.name,score=student_update.score)
        if result:
            return {"message": "已成功修改"}
        raise HTTPException(status_code=404, detail="Student Not Found")
    except PermissionError:
        raise HTTPException(status_code=500, detail="Failed to Save Student Data")