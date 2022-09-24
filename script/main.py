from uuid import uuid4
from time import perf_counter
from random import choice

from app.command import BaseCommand
from app.models import Item


class RunSqlalchemyOrm(BaseCommand):
    """python setup.py run_sql_orm --param 99999
    """

    def run(self):
        tic = perf_counter()
        total = int(self.param)

        def create():
            with self.db() as session:
                session.begin()
                data = {
                        "name": uuid4().hex.upper(),
                        "status": choice([True, False])
                    }
                db_item = Item(**data)
                session.add(db_item)
                session.commit()

        for item in range(total):
            create()
      
        toc = perf_counter()
        print(f"SQLAlchemy ORM: Total {toc - tic:0.4f} seconds")


class RunSqlalchemyOrmBulkInsert(BaseCommand):
    """python setup.py run_sql_orm_bulk_insert --param 99999
    """

    def run(self):
        tic = perf_counter()

        total = int(self.param)
        with self.db() as session:
            session.begin()
            session.bulk_insert_mappings(
                Item,
                [
                    dict(
                        name=uuid4().hex.upper(),
                        status=choice([True, False])
                    )
                    for item in range(total)
                ]
            )
            session.commit()

        toc = perf_counter()
        print(f"SQLAlchemy ORM bulk_save_objects(): Total {toc - tic:0.4f} seconds")


class RunSqlalchemyOrmAddAll(BaseCommand):
    """python setup.py run_sql_orm_add_all --param 99999
    """

    def run(self):
        tic = perf_counter()

        total = int(self.param)
        with self.db() as session:
            session.begin()
            objects = [
                Item(
                    name=uuid4().hex.upper(),
                    status=choice([True, False])
                )
                for item in range(total)
            ]
            session.add_all(objects)
            session.commit()

        toc = perf_counter()
        print(f"SQLAlchemy ORM add_all(): Total {toc - tic:0.4f} seconds")


class RunSqlalchemyCore(BaseCommand):
    """python setup.py run_sql_core --param 99999
    """

    def run(self):
        tic = perf_counter()

        total = int(self.param)
        with self.db() as session:
            session.begin()
            session.execute(
                Item.__table__.insert(),
                [
                    {
                        "name": uuid4().hex.upper(),
                        'status': choice([True, False])
                    } 
                        for item in range(total)
                ]
            )
            session.commit()

        toc = perf_counter()
        print(f"SQLAlchemy Core: Total {toc - tic:0.4f} seconds")
