from setuptools import setup
from script.main import (
    RunSqlalchemyOrm,
    RunSqlalchemyOrmBulkInsert,
    RunSqlalchemyOrmAddAll,
    RunSqlalchemyCore
)


setup(
    cmdclass={
        'run_sql_orm': RunSqlalchemyOrm,
        'run_sql_orm_bulk_insert': RunSqlalchemyOrmBulkInsert,
        'run_sql_orm_add_all' :RunSqlalchemyOrmAddAll,
        'run_sql_core': RunSqlalchemyCore
    }
)
