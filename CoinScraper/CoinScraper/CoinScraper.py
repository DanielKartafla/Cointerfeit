
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.khm.at/nocache/de/objektdb/?view=0&facet_date=-4500%3B2004&fq%5Bfacet_classification%5D%5B0%5D=Münze&sort=date_begin%3Aasc&jsrand=0.7816688649623373&rand=5&cHash=b0fa5432f93c627a3da513ef47ca8936&page=8")
soup = BeautifulSoup(page.content, 'html.parser')

print('Webpage parsed')
print(soup.prettify())
print('\n\n\n---------------\n')

html = list(soup.children)[7]
body = list(html.children)[1]

coins = soup.find_all('img')
for coin in coins:
    print(coin, end='\n'*2)


print('count: ' + str(coins))
#for coin in coins:
#  print("Coin:\n" + str(coin.src))


print("end")