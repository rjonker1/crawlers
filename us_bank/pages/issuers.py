import logging

from bs4 import BeautifulSoup
from us_bank.models.issuer_view_model import IssuerViewModel

class IssuersPage:
    def __init__(self, html):
        self._html = html
        self._issuers = []
        self._soup = BeautifulSoup(self._html, 'html.parser')
    
    def Parse(self):
        dealTable = self._soup.findAll('table', id='search-for-deals-results')
        if(dealTable is None):
            logging.debug('Deal Table does not exist')
            return
        
        for row in dealTable:
            link = row.find_all('a')
            print(link)
            dealName = link.text
            href = (row['href'])
            if(dealName != 'Top' and dealName != '0 Consolidated Pmt Data File (Public ABS/MBS)'):
                issuer = IssuerViewModel(href, dealName, None)
                self._issuers.append(issuer)
    
    @property
    def Issuers(self):
        return self._issuers

    
