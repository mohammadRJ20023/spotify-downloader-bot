
from sqlalchemy.orm import Session
from database.models import User
from sqlalchemy import select


def create_user(
    db : Session, telegram_id : int, first_name : str , username : str | None = None
    ) -> User:
    
    user = User(
        telegram_id = telegram_id,
        first_name = first_name,
        username = username  
    )
    db.add(user)
    
    db.commit()
    
    db.refresh(user)
    
    return user


def get_user_by_telegram_id(db : Session, telegram_id : int) ->User | None :
    
    statement = select(User).where(User.telegram_id == telegram_id)
    
    result = db.execute(statement)
    
    return result.one_or_none()