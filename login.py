from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional, Tuple
import os
import hashlib
import hmac

class Role(str, Enum):
    ADVISOR = "Advisor"
    TEACHER = "Teacher"
    STUDENT = "Student"

@dataclass
class User:
    username: str
    password_salt: bytes
    password_hash: bytes
    role: Role

class LoginManager:
    """
    Simple in-memory login/auth manager.
    - add_user(username, password, role)
    - authenticate(username, password) -> User | None
    - get_role(username) -> Role | None
    - is_advisor/teacher/student(username) -> bool
    """
    def __init__(self) -> None:
        self._users: Dict[str, User] = {}