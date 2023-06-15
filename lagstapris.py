
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests
import re
   
#ua = UserAgent()
#print(ua.chrome)
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
header = {'User-Agent':str(ua)}
print(header)
url = "https://www.inet.se/hitta?q=laptop%203070"
url = "https://www.elgiganten.se/gaming/gaming-pc/gaming-laptop?filter=30877%253AGeForce%20RTX%203070"
htmlContent = requests.get(url, headers=header)
#soup = BeautifulSoup(htmlContent.text, 'html.parser')
soup = BeautifulSoup(htmlContent.text, 'html5lib')
#htmlContent.json()
#re.compile(r'crummy\.com/')
all_li = soup.find_all("li", {"data-test-id": re.compile(r'search_product')})
elgiganten = soup.find_all("div", {"class": "product-tile__information information"})
#print(all_li)

for li in all_li:
    print(li.get_text())
for li in elgiganten:
    print(li.get_text())
print(htmlContent.text)
