import heapq
import contextlib


@contextlib.contextmanager
def exsort(iterable, key=None, reverse=False):
    yield sorted(iterable, key=key)
