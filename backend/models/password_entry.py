from dataclasses import dataclass
from typing import Optional


@dataclass
class PasswordEntry:
    id: int
    service: str
    username: str
    category: str
    url: Optional[str] = None
    note: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    
    def display_name(self) -> str:
        return f"{self.service} ({self.username})"