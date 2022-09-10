from setuptools import setup
from service.main import RunScript


setup(
    cmdclass={
        'run_script': RunScript,
    }
)
