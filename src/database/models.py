from sqlalchemy import String, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List
import datetime
#The models defined correpond to database tables. the CRUD operations are handled in the dal.py file. 

class Base(DeclarativeBase):
    pass

class Person(Base):
    __tablename__ = "person"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(70), nullable=False)
    email: Mapped[str] = mapped_column(String(70), nullable=True)
    phone: Mapped[str] = mapped_column(String(20), nullable=True)
    address: Mapped[str] = mapped_column(String(200), nullable=True)
    website_name: Mapped[str] = mapped_column(String(200), nullable=True)
    website_link: Mapped[str] = mapped_column(String(200), nullable=True)

    resume_data: Mapped[List["ResumeData"]] = relationship(back_populates="person")
    job_applications: Mapped[List["JobApplication"]] = relationship(back_populates="person")

class ResumeData(Base):
    __tablename__ = "resume_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    person_id: Mapped[int] = mapped_column(ForeignKey("person.id"))
    summary: Mapped[str] = mapped_column(String(1000), nullable=True)

    person: Mapped["Person"] = relationship(back_populates="resume_data")
    education: Mapped[List["Education"]] = relationship(back_populates="resume_data")
    skills: Mapped[List["Skill"]] = relationship(back_populates="resume_data")
    work_experience: Mapped[List["WorkExperience"]] = relationship(back_populates="resume_data")
    projects: Mapped[List["Project"]] = relationship(back_populates="resume_data")
    certifications: Mapped[List["Certification"]] = relationship(back_populates="resume_data")
    References: Mapped[List["Reference"]] = relationship(back_populates="resume_data")

class Education(Base):
    __tablename__ = "education"

    id: Mapped[int] = mapped_column(primary_key=True)
    resume_data_id: Mapped[int] = mapped_column(ForeignKey("resume_data.id"))
    school: Mapped[str] = mapped_column(String(100), nullable=False)
    degree: Mapped[str] = mapped_column(String(100), nullable=False)
    field_of_study: Mapped[str] = mapped_column(String(100), nullable=False)
    start_date: Mapped[str] = mapped_column(String(100), nullable=False)
    end_date: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    responsibilities: Mapped[List[str]] = mapped_column(String(100), nullable=False)

    resume_data: Mapped["ResumeData"] = relationship(back_populates="education")

class Skill(Base):
    __tablename__ = "skills"

    id: Mapped[int] = mapped_column(primary_key=True)
    resume_data_id: Mapped[int] = mapped_column(ForeignKey("resume_data.id"))
    skill: Mapped[str] = mapped_column(String(100), nullable=False)

    resume_data: Mapped["ResumeData"] = relationship(back_populates="skills")

class WorkExperience(Base):
    __tablename__ = "work_experience"

    id: Mapped[int] = mapped_column(primary_key=True)
    resume_data_id: Mapped[int] = mapped_column(ForeignKey("resume_data.id"))
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    company: Mapped[str] = mapped_column(String(100), nullable=False)
    location: Mapped[str] = mapped_column(String(100), nullable=False)
    start_date: Mapped[str] = mapped_column(String(100), nullable=False)
    end_date: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)

    resume_data: Mapped["ResumeData"] = relationship(back_populates="work_experience")

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    resume_data_id: Mapped[int] = mapped_column(ForeignKey("resume_data.id"))
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    link: Mapped[str] = mapped_column(String(100), nullable=False)

    resume_data: Mapped["ResumeData"] = relationship(back_populates="projects")

class Certification(Base):
    __tablename__ = "certifications"

    id: Mapped[int] = mapped_column(primary_key=True)
    resume_data_id: Mapped[int] = mapped_column(ForeignKey("resume_data.id"))
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    link: Mapped[str] = mapped_column(String(100), nullable=False)

    resume_data: Mapped["ResumeData"] = relationship(back_populates="certifications")

class Reference(Base):
    __tablename__ = "references"

    id: Mapped[int] = mapped_column(primary_key=True)
    resume_data_id: Mapped[int] = mapped_column(ForeignKey("resume_data.id"))
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    email: Mapped[str] = mapped_column(String(100), nullable=True)
    phone: Mapped[str] = mapped_column(String(100), nullable=True)
    company: Mapped[str] = mapped_column(String(100), nullable=True)

class JobApplication(Base):
    __tablename__ = "job_applications"

    id: Mapped[int] = mapped_column(primary_key=True)
    person_id: Mapped[int] = mapped_column(ForeignKey("person.id"))
    job_title: Mapped[str] = mapped_column(String(100), nullable=False)
    company: Mapped[str] = mapped_column(String(100), nullable=False)
    location: Mapped[str] = mapped_column(String(100), nullable=False)
    job_type: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    job_url: Mapped[str] = mapped_column(String(300), nullable=False)
    applied: Mapped[bool] = mapped_column(nullable=False, default=False)
    applied_date: Mapped[datetime.datetime] = mapped_column(nullable=False, server_default=func.now())

    person: Mapped["Person"] = relationship(back_populates="job_applications")
    ResumeData: Mapped["ResumeData"] = relationship(back_populates="job_applications")
    CoverLetterData: Mapped["CoverLetterData"] = relationship(back_populates="job_applications")
    Resume: Mapped["Resume"] = relationship(back_populates="job_applications")
    CoverLetter: Mapped["CoverLetter"] = relationship(back_populates="job_applications")

class CoverLetterData(Base):
    __tablename__ = "cover_letter_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    salutation: Mapped[str] = mapped_column(String(1000), nullable=False)
    introduction: Mapped[str] = mapped_column(String(1000), nullable=False)
    lead_in: Mapped[str] = mapped_column(String(1000), nullable=False)
    outro: Mapped[str] = mapped_column(String(1000), nullable=False)
    signature: Mapped[str] = mapped_column(String(100), nullable=False)

    person: Mapped["JobApplication"] = relationship(back_populates="cover_letter_data")
    cover_letter_points: Mapped["CoverLetterPoints"] = relationship(back_populates="cover_letter_data")

class CoverLetterPoints(Base):
    __tablename__ = "cover_letter_points"

    id: Mapped[int] = mapped_column(primary_key=True)
    cover_letter_data_id: Mapped[int] = mapped_column(ForeignKey("cover_letter_data.id"))
    point: Mapped[str] = mapped_column(String(1000), nullable=False)

    cover_letter_data: Mapped["CoverLetterData"] = relationship(back_populates="cover_letter_points")

class Resume(Base):
    __tablename__ = "resumes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    path: Mapped[str] = mapped_column(String(100), nullable=False)

    job_application: Mapped["JobApplication"] = relationship(back_populates="resume")

class CoverLetter(Base):
    __tablename__ = "cover_letters"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    path: Mapped[str] = mapped_column(String(100), nullable=False)

    job_application: Mapped["JobApplication"] = relationship(back_populates="cover_letter")