"""Handling large DB query results with SQLAlchemy using LIMIT & OFFSET."""
from random import randint

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

BATCH_SIZE = 20  # limit results to 20 per query

MALE = "M"
FEMALE = "F"


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    sex = Column(String(1))
    age = Column(Integer)


def get_next_batch(session, offset):
    """Return batches of 20 results and filter by men aged over 18."""
    return session.query(Person).filter(
        Person.sex == MALE, Person.age >= 18).limit(BATCH_SIZE).offset(offset)


def get_all_models(session):
    """Generator function yielding models in batches of 20."""
    offset = 0
    while True:
        models = get_next_batch(session, offset)
        count = models.count()
        if count == 0:
            print("No more models to retrieve, exiting.")
            break
        offset += models.count()
        yield models, count


def set_up_fixtures(session):
    """Add models to the in memory SQLite DB."""
    for idx in range(500):
        sex = MALE if idx % 2 == 0 else FEMALE
        session.add(Person(sex=sex, age=randint(1, 100)))
    session.commit()


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session = Session()
    try:
        set_up_fixtures(session)
        total = 0
        for batch, batch_size in get_all_models(session):
            total += batch_size
            print(f"Processing next {batch_size} models (total {total}).")
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
