from service.main import RunScript

from setuptools import setup

setup(
    cmdclass={
        'run_script': RunScript,
    }
)
