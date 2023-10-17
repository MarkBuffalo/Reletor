#!/usr/bin/env python3

import requests
import sys
from bs4 import BeautifulSoup


class RealtorSavedParser:

    def __init__(self):
        self.file_name = sys.argv[1]
        self.parse_realtor_html(self.get_soup_from_html_file())

    def get_soup_from_html_file(self):
        with open(self.file_name, "r") as f:
            file = f.read()
            return BeautifulSoup(file, "html.parser")

    def parse_realtor_html(self, soup):
        output = ""
        for item in soup.find_all("div", {"class": "card-content"}):
            address = ""
            url = ""
            for link in item.find_all("a", {"class": "card-anchor"}):
                address = link['aria-label'].replace("Property detail for", "")
                url = link['href']

            sqft = item.find_all("span", {"class": "meta-value"})[0].text
            acres = item.find_all("span", {"class": "meta-value"})[1].text
            price = item.find_all("div", {"class": "card-price"})[0].text
            beds = item.find_all("span", {"data-testid": "meta-value"})[0].text
            baths = item.find_all("span", {"data-testid": "meta-value"})[1].text

            output += "\t".join([address, price, beds, baths, sqft, acres, url]) + "\n"

        print("\t".join(["ADDRESS", "PRICE", "BEDROOMS", "BATHROOMS", "SQFT", "ACRES", "URL"]))
        print(output)


if __name__ == "__main__":
    r = RealtorSavedParser()
