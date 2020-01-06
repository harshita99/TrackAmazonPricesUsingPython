#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dell
#
# Created:     06-01-2020
# Copyright:   (c) dell 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import requests
from bs4 import BeautifulSoup
URL="https://www.amazon.in/Sony-MDR-1000X-Wireless-Cancellation-Headphones/dp/B0734VL3RG/ref=sr_1_3?keywords=sony+headphones&qid=1578320187&sr=8-3"

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
page=requests.get(URL ,headers=headers)

soup=BeautifulSoup(page.content, 'html.parser')

title=soup.find(id="productTitle")
print(title.string.strip())
price=soup.find(id="priceblock_ourprice")
cprice=price.string.strip('<span class="a-size-medium a-color-price priceBlockBuyingPriceString" id="priceblock_ourprice">')
print(cprice)

