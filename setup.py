from setuptools import setup
from script.main import (
    RunSqlalchemyOrm,
    RunSqlalchemyOrmBulkInsert,
    RunSqlalchemyOrmAddAll,
    RunSqlalchemyCore
)


setup(
    cmdclass={
        'run_sqlalchemy_orm': RunSqlalchemyOrm,
        'run_sqlalchemy_orm_bulk_insert': RunSqlalchemyOrmBulkInsert,
        'run_sqlalchemy_orm_add_all' :RunSqlalchemyOrmAddAll,
        'run_sqlalchemy_core': RunSqlalchemyCore
    }
)
