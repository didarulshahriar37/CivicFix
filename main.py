from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from database import create_db_and_tables, get_session
from models import User, Issue, Comment
from pydantic import BaseModel

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

class UserCreate(BaseModel):
    email: str
    role: str = "resident"

class IssueCreate(BaseModel):
    title: str
    description: str
    category: str
    location: str
    reporter_id: int

# Task D1
@app.get("/issues", response_model=list[Issue])
def list_issues(session: Session = Depends(get_session)):
    return session.exec(select(Issue)).all()

# Task E1
@app.post("/users", response_model=User, status_code=201)
def create_user(data: UserCreate, session: Session = Depends(get_session)):
    user = User(email=data.email, role=data.role)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# Task E2
@app.post("/issues", response_model=Issue, status_code=201)
def create_issue(data: IssueCreate, session: Session = Depends(get_session)):
    reporter = session.get(User, data.reporter_id)
    if reporter is None:
        raise HTTPException(status_code=404, detail="Reporter not found")
    
    issue = Issue(**data.model_dump(), status="Reported")

    session.add(issue)
    session.commit()
    session.refresh(issue)
    return issue

# Task E3
@app.get("/issues/{issue_id}", response_model=Issue)
def get_issue_by_id(issue_id: int, session: Session = Depends(get_session)):
    issue = session.get(Issue, issue_id)
    if issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")

    return issue

# Task E4
@app.put("/issues/{issue_id}", response_model=Issue)
def edit_issue(issue_id: int, data: IssueCreate, session: Session = Depends(get_session)):
    issue = session.get(Issue, issue_id)
    if issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")

    reporter = session.get(User, data.reporter_id)
    if reporter is None:
        raise HTTPException(status_code=404, detail="Reporter not found")

    issue.title = data.title
    issue.description = data.description
    issue.category = data.category
    issue.location = data.location
    issue.reporter_id = data.reporter_id

    session.add(issue)
    session.commit()
    session.refresh(issue)

    return issue

# Task E5
@app.delete("/issue/{issue_id}")
def delete_issue(issue_id: int, session: Session = Depends(get_session)):
    issue = session.get(Issue, issue_id)
    if issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")

    session.delete(issue)
    session.commit()

    return {"message": "Issue deleted"}