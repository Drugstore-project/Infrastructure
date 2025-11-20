"""
Main entry point for Auth Service.
"""
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db, Base, engine
from app.schemas import UserCreate, UserOut, TokenOut
from app.crud import create_user, get_user_by_email
from app.security import verify_password, create_access_token

app = FastAPI(title="Auth Service")

# Ensure tables exist (in a real microservice, use Alembic)
Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok", "service": "Auth Service"}

@app.post("/auth/register", response_model=UserOut)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    try:
        user = create_user(db, payload)
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/auth/login", response_model=TokenOut)
def login(
    form: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = get_user_by_email(db, form.username)
    if not user or not verify_password(form.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    role_data = {"id": user.role.id, "name": user.role.name} if user.role else None
    token = create_access_token(subject=user.email, extra={"role": role_data})
    return TokenOut(access_token=token)
