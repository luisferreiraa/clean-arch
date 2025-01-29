from fastapi import FastAPI
from clean_arch.presentation.routers import user
from clean_arch.infrastructure.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user.router)
