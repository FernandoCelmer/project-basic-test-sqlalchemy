from setuptools import Command
from app.database import SessionLocal

class BaseCommand(Command):

    description = 'Run Script'
    user_options = [
        ('value=', 'i', 'input value'),
        ('thread=', 'i', 'input thread')
    ]

    def initialize_options(self):
        self.value = 10
        self.thread = 1

    def finalize_options(self):
        self.db = SessionLocal
        self.value = int(self.value)
        self.thread = int(self.thread)

    def run(self):
        pass
