from exsort import exsort
import random
import string
import operator
import itertools

def test_exsort():


    def items():
        while True:
            a = random.choice(string.ascii_letters)
            yield (a, random.randint(0, 2**32))

    with exsort(itertools.islice(items(), 10000), key=operator.itemgetter(1)) as sorted_items:
        assert isinstance(sorted_items, list)
        for i in range(len(sorted_items) - 1):
            assert sorted_items[i][1] <= sorted_items[i+1][1]
