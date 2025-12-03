from sqlalchemy.orm import Session
from db.models.blog_model import Blog
from db.models.user_model import User
from schemas.blog_schema import BlogCreate


def create_new_blog(blog: BlogCreate, db: Session, author_id: int =1):
    # Check if slug already exists
    
    # Create new blog
    new_blog = Blog(
        title=blog.title,
        slug=blog.slug,
        content=blog.content,
        author_id=blog.author_id,
        is_active=True,
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def retrieve_blog(id:int, db: Session ):
    blog= db.query(Blog).filter(Blog.id==id).first()
    return blog

def retrieve_all_blogs(db: Session ):
    blogs= db.query(Blog).filter(Blog.is_active==True).all()
    return blogs    