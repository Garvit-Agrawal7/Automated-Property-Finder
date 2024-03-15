from bs4 import BeautifulSoup
import requests


class ListingsData:
    def __init__(self):
        url = 'https://appbrewery.github.io/Zillow-Clone/'
        self.soup = BeautifulSoup(requests.get(url).text, 'html.parser')
        self.addresses = list()
        self.prices = list()
        self.links = list()

    def get_listings(self):
        def price():
            price_selector = '#zpid_2056905294 > div > div.StyledPropertyCardDataWrapper > div.StyledPropertyCardDataArea-fDSTNn > div > span'
            amounts = self.soup.select(price_selector)
            for amount in amounts:
                amount = amount.getText()[:6].replace(',', '').replace('+', '')
                self.prices.append(amount)
            return self.prices

        def link():
            site_selector = '#zpid_2056905294 > div > div.StyledPropertyCardDataWrapper > a'
            site_ads = self.soup.select(site_selector)
            for site_ad in site_ads:
                self.links.append(site_ad['href'])
            return self.links

        def address():
            address_selector = '#zpid_2056905294 > div > div.StyledPropertyCardDataWrapper > a > address'
            listings = self.soup.select(address_selector)
            for listing in listings:
                place = listing.getText().strip().replace('|', '')
                self.addresses.append(place)
            return self.addresses

        data = []
        for i in range(len(address())):
            data.append([address()[i], price()[i], link()[i]])
        return data
