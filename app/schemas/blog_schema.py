from typing import Optional
from datetime import datetime
import re
from pydantic import BaseModel, Field, model_validator


# Base schema with common fields
class BlogCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255, description="Blog post title")
    slug: Optional[str] = Field(None, min_length=1, max_length=255, description="URL-friendly slug (auto-generated if not provided)")
    content: str = Field(..., min_length=1, description="Blog post content")
    author_id: int = Field(..., description="ID of the author/user")

    @model_validator(mode='before')
    @classmethod
    def generate_slug(cls, values):
        if isinstance(values, dict):
            # Only generate slug if not already provided and title exists
            if 'slug' not in values or not values.get('slug'):
                if 'title' in values and values.get('title'):
                    title = str(values['title'])
                    # Convert to lowercase and replace spaces with hyphens
                    slug = title.lower().strip()
                    # Replace spaces and multiple spaces with single hyphen
                    slug = re.sub(r'\s+', '-', slug)
                    # Remove special characters except hyphens
                    slug = re.sub(r'[^a-z0-9-]', '', slug)
                    # Remove multiple consecutive hyphens
                    slug = re.sub(r'-+', '-', slug)
                    # Remove leading/trailing hyphens
                    slug = slug.strip('-')
                    values['slug'] = slug
        return values





# # Schema for updating blog (all fields optional)
# class BlogUpdate(BaseModel):
#     title: Optional[str] = Field(None, min_length=1, max_length=255)
#     slug: Optional[str] = Field(None, min_length=1, max_length=255)
#     content: Optional[str] = Field(None, min_length=1)
#     excerpt: Optional[str] = None
#     is_active: Optional[bool] = None


# Schema for blog response (excludes author_id, includes author info)
class ShowBlog(BaseModel):    
    title: str    
    content: str
    created_at: datetime
    
    class Config:
        from_attributes = True  # Allows conversion from SQLAlchemy models (Pydantic v2)


# Schema with author details (for detailed views)
class BlogWithAuthor(ShowBlog):
    author_email: Optional[str] = None
    author_username: Optional[str] = None
    
    class Config:
        from_attributes = True
