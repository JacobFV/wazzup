from sqlmodel import create_engine, Session

# Configure database connection using SQLModel and Supabase
DATABASE_URL = "postgresql://user:password@localhost/database"
engine = create_engine(DATABASE_URL)
session = Session(bind=engine)
