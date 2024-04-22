import pytest
from database.models import User, Platform, UserPlatform, Channel, Message, Draft, Subscription, SamplingConfig, GenerationConfig
from database.crud import create_user, get_user_by_id, get_user_by_email, update_user, delete_user

def test_create_user():
    user = User(username="testuser", email="testuser@example.com", password_hash="password")
    created_user = create_user(user)
    assert created_user.id is not None
    assert created_user.username == "testuser"
    assert created_user.email == "testuser@example.com"

def test_get_user_by_id():
    user = User(username="testuser", email="testuser@example.com", password_hash="password")
    created_user = create_user(user)
    retrieved_user = get_user_by_id(created_user.id)
    assert retrieved_user is not None
    assert retrieved_user.id == created_user.id

def test_get_user_by_email():
    user = User(username="testuser", email="testuser@example.com", password_hash="password")
    created_user = create_user(user)
    retrieved_user = get_user_by_email(created_user.email)
    assert retrieved_user is not None
    assert retrieved_user.email == created_user.email

def test_update_user():
    user = User(username="testuser", email="testuser@example.com", password_hash="password")
    created_user = create_user(user)
    created_user.username = "updateduser"
    updated_user = update_user(created_user)
    assert updated_user.username == "updateduser"

def test_delete_user():
    user = User(username="testuser", email="testuser@example.com", password_hash="password")
    created_user = create_user(user)
    delete_user(created_user)
    deleted_user = get_user_by_id(created_user.id)
    assert deleted_user is None

# Write similar tests for other CRUD operations and models

