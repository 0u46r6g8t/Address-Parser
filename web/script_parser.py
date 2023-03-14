from requests import request, utils
from bs4 import BeautifulSoup
import re

class Parser:    
    def __init__(self):
        self.place_search = None
        self._url_parser = 'https://www.google.com/search?channel=fs&client=ubuntu&q='
        self.data = []
        
    # Format string to get url
    def format_string(self, name):
        self.place_search = name.replace(" ", "+").lower()

        return self.place_search
    
    def format_reverse(self):
        return str(self.place_search.replace("+", " ")).capitalize()

    # Split address by format to return 
    def split_address(self, address):
        return address.split(', ')
        
    # Proccess response and return data with address, cep and city
    def soup_data(self, parser_req):
        try:
            soup = BeautifulSoup(parser_req, 'html.parser')
            address = soup.find('span', class_='LrzXr').text

            return self.split_address(address)
        except Exception as e: 
            return 'Activity not found'
        
    # Get request with headers in url
    def get_headers(self):
        headers = utils.default_headers()

        headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0' })

        return headers
        
    def get_data(self, name=''):
        try:
            if(name):
                new_url = self._url_parser + self.format_string(name)
                
                headers = self.get_headers()
                
                request_data = request('GET', new_url, headers=headers)

                return self.soup_data(request_data.text)
        except Exception as e: 
            return 'Activity not found'
