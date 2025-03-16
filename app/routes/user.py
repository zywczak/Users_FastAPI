from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import UserDB
from app.schemas.user import UserCreate, UserListResponse, UserResponse

router = APIRouter()

# GET /users - Pobierz listę użytkowników z paginacją i filtrowaniem
@router.get("/users", response_model=UserListResponse)
def get_users(
    db: Session = Depends(get_db),
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0),
    name: str | None = None
):
    query = db.query(UserDB)
    if name:
        query = query.filter(UserDB.name.ilike(f"%{name}%"))
        
    total_users = query.count()  # Liczba pasujących użytkowników
    users = query.offset(offset).limit(limit).all()

    return UserListResponse(
        total=total_users,
        users=users
    )

# POST /users - Dodaj użytkownika
@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(UserDB).filter(UserDB.email == user.email).first():
        raise HTTPException(status_code=400, detail="User with this email already exists")

    new_user = UserDB(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# GET /users/{id} - Pobierz użytkownika po ID
@router.get("/users/{id}", response_model=UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# PUT /users/{id} - Aktualizuj użytkownika
@router.put("/users/{id}", response_model=UserResponse)
def update_user(id: int, user_update: UserCreate, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.name = user_update.name
    user.email = user_update.email
    db.commit()
    db.refresh(user)
    return user

# DELETE /users/{id} - Usuń użytkownika
@router.delete("/users/{id}", status_code=204)
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return