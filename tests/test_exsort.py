from exsort import exsort
import random
import string
import operator
import itertools

def test_exsort():


    def items():
        while True:
            a = random.choice(string.ascii_letters)
            yield (a, random.randint(0, 20))

    sorted_items = list(exsort(itertools.islice(items(), 10), key=operator.itemgetter(1), chunk_size=2))
    for i in range(len(sorted_items) - 1):
        assert sorted_items[i][1] <= sorted_items[i+1][1]
