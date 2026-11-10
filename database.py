import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, Session, create_engine

load_dotenv()

print("Loaded DATABASE_URL:", os.getenv("DATABASE_URL"))
print("Current directory:", os.getcwd())

engine = create_engine(os.environ["DATABASE_URL"], echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session