from setuptools import setup
from script.main import RunScript


setup(
    cmdclass={
        'run_script': RunScript,
    }
)
