from sqlalchemy.orm import session
from src.database.models import Person

#CRUD + Get Person methods
def create_person(person: Person):
    
    """
    Create a new person in the database.

    Args:
        person (Person): Person object to be created in the database.

    Returns:
        None
    """
    try:
        session.add(person)
        session.commit()
    finally:
        session.close() 
def get_person(person_id: int) -> Person:
    
    """
    Get a person from the database.

    Args:
        person_id (int): ID of the person to be retrieved from the database.

    Returns:
        Person: Person object from the database.
    """
    try:
        return session.get_one(Person,person_id)
    except Exception as e:
        session.rollback()
        raise e 
def update_person(person_id: int, person_data: dict) -> bool:
    
    """
    Update a person in the database.

    Args:
        person (Person): Person object to be updated in the database.

    Returns:
        None
    """
    try:
        session.query(Person).filter_by(id=person_id).update(person_data)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        raise e
    

def delete_person(person: Person):
    
    """
    Delete a person from the database.

    Args:
        person (Person): Person object to be deleted from the database.

    Returns:
        None
    """
    
    try:
        session.delete(person)
        session.commit()
    finally:
        print(session.deleted)
        session.close() 