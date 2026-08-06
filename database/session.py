"""
Database Session Management
"""

from sqlalchemy.orm import sessionmaker
from database.database import engine


# Create session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False,)