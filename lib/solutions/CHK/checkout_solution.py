# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter

PRICE_TABLE = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
}

OFFERS = {
    "A": (3, 130),
    "B": (2, 45),
}

FREE_OFFERS = {
    "E": (2, "B", 1),
}


def checkout(skus):
    price = 0
    count = Counter(skus)

    for sku in count:
        if sku in OFFERS:
            while count[sku] >= OFFERS[sku][0]:
                price += OFFERS[sku][1]
                count[sku] -= OFFERS[sku][0]
        try:
            price += PRICE_TABLE[sku] * count[sku]
        except KeyError:
            return -1
    return price



