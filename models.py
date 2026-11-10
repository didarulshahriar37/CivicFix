from datetime import datetime, timezone
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    role: str = "resident"

# Task C2
class Issue(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    category: str
    location: str
    status: str = "Reported"
    reporter_id: int = Field(foreign_key="user.id")

# Task C3
class Comment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    body: str
    author_id: int = Field(foreign_key="user.id")
    issue_id: int = Field(foreign_key="issue.id")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))