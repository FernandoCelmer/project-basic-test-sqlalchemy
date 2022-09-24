from time import sleep, perf_counter
from threading import Thread

def run_thread(task, value: int = 1):
    threads = []
    for n in range(value):
        t = Thread(target=task, args=(1))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
