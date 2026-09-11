from fastapi import FastAPI
from app.routers.students import router
app = FastAPI()

app.include_router(router)