import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DATABASE_URL = "sqlite:///./database.db"

engine = _sql.create_engine(
    url=DATABASE_URL,
    connect_args={"check_same_thread":False}
)

SessionLocal = _orm.sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

BASE = _declarative.declarative_base()