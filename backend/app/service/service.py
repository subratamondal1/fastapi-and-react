from ..database import database as _database

def create_database():
    return _database.BASE.metadata.create_all(bind=_database.engine)