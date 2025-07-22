from fastapi import FastAPI
from app.core.db import Base, engine

from app.services.users import router as user_router
from app.services.announcement import router as announce_router
from app.services.lost_found import router as lostfound_router

Base.metadata.create_all(bind=engine)


app = FastAPI(title="CampusHub")

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(announce_router, prefix="/announcements", tags=["Announcements"])
app.include_router(lostfound_router, prefix="/lost_found", tags=["Lost & Found"])
