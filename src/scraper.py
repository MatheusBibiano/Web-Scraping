# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from variables import URL, DRIVER_PATH


class Scraper:
    def __init__(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)
        browser.get(URL)
        self.soup = BeautifulSoup(browser.page_source, "html.parser")
        browser.quit()

    def get_all_counters(self) -> list:
        """
            Retorna todos os contadores da página.
        """
        self.soup.find(attrs={"rel": "oil_years"}).clear()

        counters = []
        elements = self.soup.find_all(attrs={"class": "rts-counter"})

        for el in elements:
            el_list = list(el.children)
            counter = ""

            for i in range(1, len(el_list), 2):
                counter += el_list[i].text

            if len(counter) != 0:
                counters.append(int(counter))

        return counters

    def get_counters_description(self) -> list:
        """
            Retorna todas as descrições dos contadores.
        """
        descs = []

        for el in self.soup.find_all(attrs={"class": "counter-item-double"}):
            el["class"] = "counter-item"
        
        for el in self.soup.find_all(attrs={"class": "counter-item"}):
            descs.append(el.text)

        return descs
