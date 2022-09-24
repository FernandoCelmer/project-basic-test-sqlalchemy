from time import sleep
from app.database import SessionLocal
from sqlalchemy.orm import Session
from threading import Thread


def make_post(model,
              data: dict,
              retry: int = 0,
              max_retry: int = 5,
              db: Session = SessionLocal) -> dict:
    db_item = model(**data)

    with db() as session:
        session.begin()
        try:
            session.add(db_item)
            session.add(db_item)
        except Exception as error:
            session.rollback()

            if retry < max_retry:
                retry += 1
                sleep(3)
                make_post(model, data, retry)
        else:
            session.commit()
            if db_item.id:
                db_item.__dict__.pop("_sa_instance_state")
                return db_item.__dict__


def run_thread(task, thread: int = 1, value: int = 10):
    threads = []
    for n in range(thread):
        t = Thread(target=task, args=(value,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
