from fastapi import FastAPI
from app.database import engine, Base
from app.routes import user

app = FastAPI()

# Tworzenie tabel w bazie danych
Base.metadata.create_all(bind=engine)

# Rejestracja tras
app.include_router(user.router)
