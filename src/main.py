# -*- coding: utf-8 -*-

import json
from scraper import Scraper
from variables import COUNTERS_ABBR

def pack_counters(values: list, descriptions: list, abbrs: list) -> dict:
    """
        Empacota os dados relacionados a cada contador.
    """
    counters_dict = {}

    for i in range(len(values)):
        counters_dict[abbrs[i]] = {
            "value": values[i],
            "desc": descriptions[i]
        }

    return counters_dict


def dict_to_json(data: dict):
    """
        Converte o dicionário em json
        e salva em um arquivo
    """
    with open("./src/response.json", "w") as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    scraper = Scraper()
    counters_value = scraper.get_all_counters()
    descs = scraper.get_counters_description()
    pack = pack_counters(counters_value, descs, COUNTERS_ABBR)
    dict_to_json(pack)
