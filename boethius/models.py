from sqlalchemy import Column, Integer, String, Time, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    lectures = relationship("Lecture", backref="class")

class Lecture(Base):
    __tablename__ = "lectures"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    professor = Column(String)
    start_time = Column(Time)
    end_time = Column(Time)
    days = Column(String)

    class_id = Column(Integer, ForeignKey("class.id"))
    discussions = relationship("Discussion", backref="lecture")

class Discussion(Base):
    __tablename__ = "discussions"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    instructor = Column(String)
    start_time = Column(Time)
    end_time = Column(Time)
    days = Column(String)

