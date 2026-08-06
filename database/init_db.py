
from database.database import Base, engine

# Import all models
from database.models import User



def init_database() -> None:
    """
    Create all database tables.
    """
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_database()
    print("Database initialized successfully.")