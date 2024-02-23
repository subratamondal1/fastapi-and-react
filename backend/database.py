"""SQL Database Setup with SQLAlchemy: Manage database connections and models.

This module establishes a connection to the SQLite database, defines a base class for database models,
and creates a session maker for efficient database interaction. It acts as the foundation for persisting data in your FastAPI application.
"""
import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DATABASE_URL = "sqlite:///./database.db"

# Create a database engine for connecting and interacting with the database
engine: _sql.Engine = _sql.create_engine(
    url=DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a session maker for opening database sessions efficiently
SessionLocal = _orm.sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Define a base class for all database models to inherit from
Base = _declarative.declarative_base()
