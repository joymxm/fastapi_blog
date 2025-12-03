from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..base_class import Base


class User(Base):
    """
    User model representing a user/author in the blog system
    """
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    # full_name = Column(String(100), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    # is_superuser = Column(Boolean, default=False, nullable=False)
    
    # Timestamps
    # created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    # updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=True)
    
    # Relationships
    blogs = relationship("Blog", back_populates="author", cascade="all, delete-orphan")
    
    # def __repr__(self):
    #     return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"
