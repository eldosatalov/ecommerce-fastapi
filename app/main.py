from fastapi import FastAPI
import logging
from app.api.main import router as api_router
from app.database import db

logger = logging.getLogger(__name__)


app = FastAPI(title="Async Fast API", version="0.4")

app.include_router(api_router, prefix="/api")

@app.on_event("startup")
async def startup():
    await db.create_all()


@app.on_event("shutdown")
async def shutdown():
    await db.close()


@app.get("/", include_in_schema=False)
async def health():
    return {"message": "It worked!!"}
