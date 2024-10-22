from src.database.models import Person
from src.dal.person_dal import create_person


def create_new_person(person: Person) -> bool:
    """
    Create a new person in the database.

    Args:
        person (Person): Person object to be created in the database.

    Returns:
        None
    """
    try:
        create_person(person)
        return True
    except Exception as e:
        raise e