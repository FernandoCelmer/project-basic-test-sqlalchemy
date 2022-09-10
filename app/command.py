from setuptools import Command

class BaseCommand(Command):

    description = 'Run Script'
    user_options = [('param=', 'i', 'input param')]

    def initialize_options(self):
        self.param = None

    def finalize_options(self):
        pass

    def run(self):
        pass
