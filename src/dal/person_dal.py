from sqlalchemy.orm import Session
from database.models import Person

#CRUD + Get Person methods
def create_person(session: Session, person: Person):
    
    """
    Create a new person in the database.

    Args:
        session (Session): SQLAlchemy session to the database.
        person (Person): Person object to be created in the database.

    Returns:
        None
    """
    
    pass 
def get_person(session: Session, person_id: int):
    
    """
    Get a person from the database.

    Args:
        session (Session): SQLAlchemy session to the database.
        person_id (int): ID of the person to be retrieved from the database.

    Returns:
        Person: Person object from the database.
    """
    
    pass
def update_person(session: Session, person: Person):
    
    """
    Update a person in the database.

    Args:
        session (Session): SQLAlchemy session to the database.
        person (Person): Person object to be updated in the database.

    Returns:
        None
    """
    
    pass

def delete_person(session: Session, person: Person):
    
    """
    Delete a person from the database.

    Args:
        session (Session): SQLAlchemy session to the database.
        person (Person): Person object to be deleted from the database.

    Returns:
        None
    """
    
    pass