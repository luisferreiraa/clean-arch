# infrastructure/models/post.py
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from clean_arch.infrastructure.database import Base


class PostModel(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    # Relação com UserModel
    user = relationship('UserModel', back_populates='posts')
