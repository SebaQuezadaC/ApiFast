from sqlmodel import SQLModel, create_engine

DATABASE_URL = "postgresql://SEBA:2004@localhost:5432/TEST"
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    from sqlmodel import Session
    with Session(engine) as session:
        yield session
