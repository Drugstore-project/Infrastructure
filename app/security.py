"""
Security utilities for password hashing and JWT token management.
"""
from datetime import datetime, timedelta, timezone
import bcrypt
from jose import jwt
from app.config import settings

def hash_password(plain: str) -> str:
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(plain.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(plain: str, hashed: str) -> bool:
    # Check the password against the hash
    return bcrypt.checkpw(plain.encode('utf-8'), hashed.encode('utf-8'))

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
