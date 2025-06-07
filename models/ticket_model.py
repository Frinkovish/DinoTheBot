from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from config import DATABASE_URL

Base = declarative_base()

class Ticket(Base):
    __tablename__ = 'tickets'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    username = Column(String)
    message = Column(String)
    category = Column(String)
    priority = Column(String)
    resolved = Column(Boolean, default=False)
    response = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Ticket(id={self.id}, user={self.username}, category={self.category}, priority={self.priority})>"

# Database setup
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)