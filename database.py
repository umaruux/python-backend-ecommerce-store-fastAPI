from sqlalchemy import create_engine  # Imports the function that creates the database connection manager.
from sqlalchemy.orm import DeclarativeBase  # Imports the base class for defining ORM models.

DATABASE_URL = "sqlite:///./shop.db"  # Points SQLAlchemy to shop.db in the current project folder.


class Base(DeclarativeBase):  # Creates the parent class that our database models will inherit from.
    pass  # The class has no extra behavior of its own; SQLAlchemy provides the model functionality.


engine = create_engine(  # Creates the SQLAlchemy engine, which manages database connections.
    DATABASE_URL,  # Tells the engine which database to connect to.
    connect_args={"check_same_thread": False},  # Lets FastAPI use SQLite across different threads.
)