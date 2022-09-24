# [project-basic-test-sqlalchemy]

![GitHub followers](https://img.shields.io/github/followers/FernandoCelmer?label=FernandoCelmer&style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/FernandoCelmer/project-basic-test-sqlalchemy?style=for-the-badge)

## ✔️ About
This repository contains a basic Python project for performing database operations using the SQLAlchemy ORM.

## 🚀 Stack

- [Python](https://www.python.org/) 
- [SQLAlchemy](https://www.sqlalchemy.org/)

# Instructions

<details>
  <summary>Installing Local Project with [PIP]</summary>
  <br>
  
 - Create a new Python virtual environment
```bash
virtualenv -p python3.9 venv
```
 - Activate the virtual environment
```bash
source venv/bin/activate
```
 - Install requirements with PIP
```bash
pip install -r requirements.txt
```
</details>

## Running

| Option                              | Command                                                           |
| :---------------------------------: | :---------------------------------------------------------------: |
| SQLAlchemy ORM	                    | `python setup.py run_sql_orm --param 99999`                |
| SQLAlchemy ORM add_all()	          | `python setup.py run_sql_orm_add_all --param 99999`        |
| SQLAlchemy ORM bulk_save_objects()	| `python setup.py run_sql_orm_bulk_insert --param 99999`    |
| SQLAlchemy Core	                    | `python setup.py run_sql_core --param 99999`               |

## Test - SQLite

- SQLAlchemy ORM: Total 5.3358 seconds
- SQLAlchemy ORM add_all(): Total 4.8070 seconds
- SQLAlchemy ORM bulk_save_objects(): Total 0.7364 seconds
- **SQLAlchemy Core: Total 0.5063 seconds**

## Test - MySQL

- SQLAlchemy ORM: --
- SQLAlchemy ORM add_all(): --
- **SQLAlchemy ORM bulk_save_objects(): Total 5.8701 seconds**
- SQLAlchemy Core: Total 11.2585 seconds

## Test - Mysql (1000:Inserts) * (10:Threads)

<details>
  <summary>SQLAlchemy ORM</summary>

</details>

<details>
  <summary>SQLAlchemy ORM add_all()</summary>

  
</details>
  
<details>
  <summary>SQLAlchemy ORM bulk_save_objects()</summary>

    running run_sql_orm_bulk_insert
    SQLAlchemy ORM bulk_save_objects(): Total [0:00:00.853800]
    SQLAlchemy ORM bulk_save_objects(): Total [0:00:01.749000]
    SQLAlchemy ORM bulk_save_objects(): Total [0:00:01.771200]
    SQLAlchemy ORM bulk_save_objects(): Total [0:00:01.773400]
    SQLAlchemy ORM bulk_save_objects(): Total [0:00:01.776300]
    SQLAlchemy ORM bulk_save_objects(): Total [0:00:01.945100]
    SQLAlchemy ORM bulk_save_objects(): Total [0:00:01.912700]
    SQLAlchemy ORM bulk_save_objects(): Total [0:00:01.929000]
    SQLAlchemy ORM bulk_save_objects(): Total [0:00:02.022500]
    SQLAlchemy ORM bulk_save_objects(): Total [0:00:02.732800]

</details>
  
<details>
  <summary>SQLAlchemy Core</summary>

    running run_sql_core
    SQLAlchemy Core: Total [0:00:00.791400]
    SQLAlchemy Core: Total [0:00:01.689200]
    SQLAlchemy Core: Total [0:00:01.733400]
    SQLAlchemy Core: Total [0:00:01.730500]
    SQLAlchemy Core: Total [0:00:01.688000]
    SQLAlchemy Core: Total [0:00:01.728900]
    SQLAlchemy Core: Total [0:00:01.718400]
    SQLAlchemy Core: Total [0:00:01.691300]
    SQLAlchemy Core: Total [0:00:01.713200]
    SQLAlchemy Core: Total [0:00:01.835200]

</details>
