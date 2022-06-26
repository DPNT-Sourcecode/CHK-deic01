# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter

PRICE_TABLE = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

OFFERS = {
    "A": (3, 130),
    "B": (2, 45),
}


def checkout(skus):
    raise NotImplementedError()

