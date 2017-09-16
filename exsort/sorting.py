import heapq
import tempfile
import itertools
import pickle


def exsort(iterable, key=None, reverse=False, chunk_size=2**16):
    # divide the iterable and dump into temp file as pickle
    sorted_chunks = []
    while True:
        iterator = itertools.islice(iterable, chunk_size)
        chunk = tempfile.TemporaryFile()

        for item in sorted(iterator, key=key, reverse=reverse):
            pickle.dump(item, chunk)

        if chunk.tell() > 0:
            chunk.seek(0)
            sorted_chunks.append(chunk)
        else:
            break

    def load(chunk):
        while True:
            try:
                yield pickle.load(chunk)
            except EOFError:
                break

    return heapq.merge(*map(load, sorted_chunks), key=key, reverse=reverse)
