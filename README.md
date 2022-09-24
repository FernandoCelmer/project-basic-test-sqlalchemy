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
- SQLAlchemy Core: Total 0.5063 seconds

## Test - MySQL

- SQLAlchemy Core: Total 11.2585 seconds
- SQLAlchemy ORM bulk_save_objects(): Total 5.8701 seconds
