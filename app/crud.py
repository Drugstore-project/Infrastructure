"""
CRUD operations for Auth Service.
"""
from sqlalchemy.orm import Session
from app.models import User, UserRole
from app.schemas import UserCreate
from app.security import hash_password

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, data: UserCreate) -> User:
    if get_user_by_email(db, data.email):
        raise ValueError("Email already registered")

    role = db.query(UserRole).filter(UserRole.id == data.role_id).first()
    if not role:
        raise ValueError("Role not found")

    user = User(
        name=data.name,
        email=data.email,
        cpf=data.cpf,
        phone=data.phone,
        address=data.address,
        password_hash=hash_password(data.password),
        role_id=data.role_id
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
