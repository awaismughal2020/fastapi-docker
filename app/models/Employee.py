from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base

# Define the Base class, if not already defined
Base = declarative_base()

class Employee(Base):  # assuming you have Base from SQLAlchemy's declarative base
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String)
    department = Column(String)
    job_title = Column(String)
    mentor_role = Column(String)
    skills = Column(String)
    interests = Column(String)
    experience = Column(Integer)
    location = Column(String)
    education = Column(String)
    project_involvement = Column(String)
    employee_status = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    manager = Column(String)
    date_of_birth = Column(Date)
    date_of_joining = Column(Date)
    performance_score = Column(Float)
    last_performance_review_date = Column(Date)
    preferred_work_style = Column(String)
    languages_spoken = Column(String)
    linkedin_profile = Column(String)
