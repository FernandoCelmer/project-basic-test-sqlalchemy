import datetime
from uuid import uuid4
from time import perf_counter
from random import choice

from app.core import run_thread
from app.command import BaseCommand
from app.models import Item


class RunSqlalchemyOrm(BaseCommand):
    """python setup.py run_sql_orm --value 1 --thread 10
    """

    def run(self):
        run_thread(
            task=self.create,
            thread=self.thread,
            value=self.value
        )


    def create(self, value):
        tic = perf_counter()

        total = value
        def _create():
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
            _create()
      
        toc = perf_counter()
        time_result = float(f'{toc - tic:0.4f}')
        print(f"SQLAlchemy ORM: Total [{datetime.timedelta(seconds=time_result):0.4f}]")


class RunSqlalchemyOrmBulkInsert(BaseCommand):
    """python setup.py run_sql_orm_bulk_insert --value 1 --thread 10
    """

    def run(self):
        run_thread(
            task=self.create,
            thread=self.thread,
            value=self.value
        )

    def create(self, value):
        tic = perf_counter()

        total = value
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
            time_result = float(f'{toc - tic:0.4f}')
            print(f"SQLAlchemy ORM bulk_save_objects(): Total [{datetime.timedelta(seconds=time_result)}]")


class RunSqlalchemyOrmAddAll(BaseCommand):
    """python setup.py run_sql_orm_add_all --value 1 --thread 10
    """

    def run(self):
        run_thread(
            task=self.create,
            thread=self.thread,
            value=self.value
        )

    def create(self, value):
        tic = perf_counter()

        total = value
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
        time_result = float(f'{toc - tic:0.4f}')
        print(f"SQLAlchemy ORM add_all(): Total [{datetime.timedelta(seconds=time_result)}]")


class RunSqlalchemyCore(BaseCommand):
    """python setup.py run_sql_core --value 1 --thread 10
    """

    def run(self):
        run_thread(
            task=self.create,
            thread=self.thread,
            value=self.value
        )

    def create(self, value):
        tic = perf_counter()

        total = value
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
        time_result = float(f'{toc - tic:0.4f}')
        print(f"SQLAlchemy Core: Total [{datetime.timedelta(seconds=time_result)}]")
