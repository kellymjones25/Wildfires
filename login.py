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

    def _hash_password(self, password: str, salt: Optional[bytes] = None) -> Tuple[bytes, bytes]:
        if salt is None:
            salt = os.urandom(16)
        # PBKDF2-HMAC-SHA256 (secure & stdlib-only)
        pwd_hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100_000)
        return salt, pwd_hash

    def _check_password(self, password: str, salt: bytes, expected_hash: bytes) -> bool:
        test_hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100_000)
        return hmac.compare_digest(test_hash, expected_hash)