# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter

PRICE_TABLE = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
}

OFFERS = {
    "A": {
        3: 130,
        5: 200,
    },
    "B": {2: 45},
}

FREE_OFFERS = {
    "E": (2, "B", 1),
    "F": (2, "F", 1),
}


def checkout(skus):
    price = 0
    count = Counter(skus)
    for sku in FREE_OFFERS:
        while count[sku] >= FREE_OFFERS[sku][0]:
            price += PRICE_TABLE[sku] * FREE_OFFERS[sku][0]
            if FREE_OFFERS[sku][2] <= count[FREE_OFFERS[sku][1]]:
                count[FREE_OFFERS[sku][1]] -= FREE_OFFERS[sku][2]
            count[sku] -= FREE_OFFERS[sku][0]
    for sku in count:
        if sku in OFFERS:
            while count[sku] >= min(OFFERS[sku].keys()):
                offer_count = max(
                    [key for key in OFFERS[sku].keys() if key <= count[sku]]
                )
                price += OFFERS[sku][offer_count]
                count[sku] -= offer_count
        try:
            price += PRICE_TABLE[sku] * count[sku]
        except KeyError:
            return -1
    return price



