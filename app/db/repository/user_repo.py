from sqlalchemy.orm import Session
from db.models.user_model import User
from db.models.blog_model import Blog  # Import Blog so SQLAlchemy can resolve the relationship
from schemas.user_schema import UserCreate
from core.hashing import Hasher


def create_new_user(user: UserCreate, db: Session):
    # Generate username from email (take part before @)
    # username = user.email.split("@")[0]
    username = user.username
    
    # Check if username already exists, if so append a number
    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        # Find a unique username by appending a number
        counter = 1
        while True:
            new_username = f"{username}_{counter}"
            existing = db.query(User).filter(User.username == new_username).first()
            if not existing:
                username = new_username
                break
            counter += 1
    
    # Create new user with generated username
    new_user = User(
        username=username,
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        is_active=True,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user