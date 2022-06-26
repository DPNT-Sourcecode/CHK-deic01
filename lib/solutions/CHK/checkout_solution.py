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
    price = 0
    count = Counter(skus)
    for sku in count:
        if sku in OFFERS:
            while count[sku] > OFFERS[sku][0]:
                price += OFFERS[sku][1]
                count[sku] -= OFFERS[sku][0]
        try:
            price += PRICE_TABLE[sku] * count[sku]
        except KeyError:
            return -1
    return price
