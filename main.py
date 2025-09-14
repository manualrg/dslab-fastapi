from fastapi import FastAPI
from database import Base, engine
from routes import items, users

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Tutorial Project",
    description="Items (in-memory) + Users (SQLAlchemy + SQLite)",
    version="1.0.0",
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Register routers
app.include_router(items.router)
app.include_router(users.router)
