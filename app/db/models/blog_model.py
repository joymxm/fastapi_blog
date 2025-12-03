from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..base_class import Base


class Blog(Base):
 
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    slug = Column(String(255), unique=True, nullable=False, index=True)
    content = Column(Text, nullable=False)
    excerpt = Column(Text, nullable=True)  # Short summary/description
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    # updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    # published_at = Column(DateTime(timezone=True), nullable=True)  # When the blog was published
    
    # Status fields
    # is_published = Column(String(20), default='draft', nullable=False)  # draft, published, archived
    # views_count = Column(Integer, default=0, nullable=False)
    
    # Relationships
    author = relationship("User", back_populates="blogs")
    
    # def __repr__(self):
    #     return f"<Blog(id={self.id}, title='{self.title}', author_id={self.author_id})>"

