from uuid import uuid4
from time import perf_counter
from random import choice

from app.core import make_post
from app.command import BaseCommand
from app.models import Item


class RunScript(BaseCommand):

    def run(self):
        tic = perf_counter()

        for item in range(1):
            data = {
                "name": uuid4().hex.upper(),
                "status": choice([True, False])
            }
            result = make_post(model=Item, data=data)
            print(result)

        toc = perf_counter()
        print(f"Time: {toc - tic:0.4f} seconds")
