# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter
import csv
import pathlib
import re


def process_price_table():
    PRICE_TABLE = {}
    OFFERS = {}
    FREE_OFFERS = {}
    GROUP_OFFERS = {}
    path = pathlib.Path(__file__).parent.joinpath("price_table.csv")
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter="|")
        rows = list(reader)
    for row in rows:
        sku = row[0].strip()
        price = int(row[1].strip())
        sku_offers = row[2].strip()
        PRICE_TABLE[sku] = price
        if "any" in sku_offers:
            group = tuple(re.search(r"\((.*)\)", s).group(1).split(","))
            GROUP_OFFERS[]
        elif "for" in sku_offers:
            OFFERS[sku] = process_offers(sku_offers, sku)
        elif "get" in sku_offers:
            FREE_OFFERS[sku] = process_free_offer(sku_offers, sku)
    return PRICE_TABLE, OFFERS, FREE_OFFERS


def get_offer_count(offer: str, sku: str):
    return int(offer[: offer.index(sku)])


def process_offers(offers: str, sku: str):
    offers_dict = {}
    for offer in offers.split(","):
        count = get_offer_count(offer, sku)
        price = int(offer.split("for")[1].strip())
        offers_dict[count] = price
    return offers_dict


def process_free_offer(offer: str, sku: str):
    count = get_offer_count(offer, sku)
    offer_sku = offer.split("one")[1].strip()[0]
    return (count, offer_sku, 1)


def checkout(skus):
    PRICE_TABLE, OFFERS, FREE_OFFERS = process_price_table()
    price = 0
    count = Counter(skus)
    for sku in FREE_OFFERS:
        while count[sku] >= FREE_OFFERS[sku][0]:
            price += PRICE_TABLE[sku] * FREE_OFFERS[sku][0]
            if sku == FREE_OFFERS[sku][1]:
                min_count = FREE_OFFERS[sku][0] + FREE_OFFERS[sku][2]
            else:
                min_count = FREE_OFFERS[sku][2]
            if min_count <= count[FREE_OFFERS[sku][1]]:
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


