from sqlalchemy import BigInteger, DateTime, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime, timezone
from database.database import Base



class User(Base):
    
    __tablename__ = "users"
    
    id : Mapped[int] = mapped_column(primary_key=True) 
    
    telegram_id : Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    
    first_name : Mapped[str] = mapped_column(String(100), nullable=False)
    
    username : Mapped[str] = mapped_column(String(100), nullable=True)
    
    created_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc) )