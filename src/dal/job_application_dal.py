from sqlalchemy.orm import session
from database.models import Person, ResumeData, CoverLetterData

#CRUD + Get JobApplication methods
def create_job_application(personId: int, resume_data: ResumeData, cover_letter_data: CoverLetterData):
    """
    Create a new job application in the database.

    Args:
        session (Session): SQLAlchemy session to the database.
        personId (int): ID of the person associated with the job application.
        resume_data (ResumeData): Resume data associated with the job application.
        cover_letter_data (CoverLetterData): Cover letter data associated with the job application.

    Returns:
        None
    """
    pass
#CRUD + Get CoverLetterData methods
def create_cover_letter_data(resume_data: ResumeData):
    """
    Generate a new cover letter data object.

    Args:
        session (Session): SQLAlchemy session to the database.
        resume_data (ResumeData): Resume data associated with the cover letter data.

    Method calls:
        generate cover letter llm call
    """
    pass

#CRUD + Get Resume methods
def create_resume(job_application: Person, name: str, path: str):
    """
    Create a new resume in the database.

    Args:
        session (Session): SQLAlchemy session to the database.
        person (Person): Person object associated with the resume.
        name (str): Name of the resume.
        path (str): Path to the resume file.

    Method calls:
        generate resume pdf
    Returns:
        None
    """
    pass

#CRUD + Get CoverLetter methods
def create_cover_letter(person: Person, name: str, path: str):
    
    """
    Create a new cover letter in the database.

    Args:
        session (Session): SQLAlchemy session to the database.
        person (Person): Person object associated with the cover letter.
        name (str): Name of the cover letter.
        path (str): Path to the cover letter file.

    Method calls:
        generate cover letter pdf
    Returns:
        None
    """
    pass