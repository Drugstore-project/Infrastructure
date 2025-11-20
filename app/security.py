"""
Security utilities for password hashing and JWT token management.
"""
from datetime import datetime, timedelta, timezone
from passlib.hash import bcrypt
from jose import jwt
from app.config import settings

def hash_password(plain: str) -> str:
    return bcrypt.hash(plain)

def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.verify(plain, hashed)

def create_access_token(
    subject: str,
    expires_minutes: int | None = None,
    extra: dict | None = None
) -> str:
    expire = datetime.now(tz=timezone.utc) + timedelta(
        minutes=expires_minutes or settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode = {"sub": subject, "exp": expire}
    if extra:
        to_encode.update(extra)
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
