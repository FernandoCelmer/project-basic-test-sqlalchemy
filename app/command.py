from setuptools import Command
from app.database import SessionLocal

class BaseCommand(Command):

    description = 'Run Script'
    user_options = [('param=', 'i', 'input param')]

    def initialize_options(self):
        self.param = None

    def finalize_options(self):
        self.db = SessionLocal

    def run(self):
        pass
