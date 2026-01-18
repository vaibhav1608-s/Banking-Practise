from fastapi import FastAPI

from app.authorization import router as authorize_router
from app.token import router as token_router
from app.balance import router as balance_router

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")


print(f"DB_HOST loaded as: {DB_HOST}")


app = FastAPI()

app.include_router(authorize_router)
app.include_router(token_router)
app.include_router(balance_router)
