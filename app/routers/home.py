from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from faker import Faker
from app.models.Employee import Employee
from app.database import SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize Faker instance
fake = Faker()

@router.api_route("/generate-employees/{count}", methods=["GET", "POST"])
def generate_employees(count: int, db: Session = Depends(get_db)):
    """
    Generate and insert 'count' fake employee records into the database.
    """
    employees = []

    # Generating fake employee data
    for _ in range(count):
        employee = Employee(
            name=fake.name(),
            age=fake.random_int(min=18, max=65),
            gender=fake.random_element(elements=('Male', 'Female', 'Other')),
            department=fake.job(),
            job_title=fake.job(),
            mentor_role=fake.job(),
            skills=", ".join(fake.words(nb=5)),
            interests=", ".join(fake.words(nb=3)),
            experience=fake.random_int(min=0, max=40),
            location=fake.city(),
            education=fake.sentence(),
            project_involvement=", ".join(fake.words(nb=2)),
            employee_status=fake.random_element(elements=('Active', 'Inactive', 'On Leave', 'Terminated')),
            email=fake.unique.email(),
            phone_number=fake.unique.phone_number(),
            manager=fake.name(),
            date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=65),
            date_of_joining=fake.date_this_decade(),
            performance_score=round(fake.pyfloat(min_value=0, max_value=100), 2),
            last_performance_review_date=fake.date_this_year(),
            preferred_work_style=fake.word(),
            languages_spoken=", ".join(fake.words(nb=2)),
            linkedin_profile=fake.url()
        )
        employees.append(employee)

    try:
        db.add_all(employees)  # Add all employees at once
        db.commit()  # Commit the transaction once
        return {"message": f"{count} fake employee records have been created."}
    except Exception as e:
        db.rollback()  # Rollback in case of error
        return {"error": str(e)}
