# SessionLocal, engine

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings


#Postgress:
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Dabase url is ", SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)



# SQLite uses check_same_thread=False
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})


# Create session factory
# SESSIONLOCAL = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine,
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()