#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """Student model for database table"""
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')">

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)