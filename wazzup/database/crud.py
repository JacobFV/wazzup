from typing import List
from sqlmodel import select
from .models import *
from .database import session

def create_user(user: User) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_user_by_id(user_id: int) -> User:
    statement = select(User).where(User.id == user_id)
    return session.exec(statement).first()

def get_user_by_email(email: str) -> User:
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()

def update_user(user: User) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def delete_user(user: User) -> None:
    session.delete(user)
    session.commit()

# Implement similar CRUD operations for other models

__all__ = [
    "create_user",
    "get_user_by_id",
    "get_user_by_email",
    "update_user",
    "delete_user",
    # Add other CRUD functions
]
