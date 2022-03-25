import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
                         '537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}

cards_NeonDynasty2022_mythic = [
    'Ao+the+Dawn+Sky', 'Atsushi+the+Blazing+Sky', 'Blade+of+the+Oni',
    'Explosive+Singularity', 'Hidetsugu+Consumes+All', 'Jin-Gitaxias+Progress+Tyrant',
    'Jugan+Defends+the+Temple', 'Junji+the+Midnight+Sky', 'Kairi+the+Swirling+Sky',
    'Kaito+Shizuki', 'Kodama+of+the+West+Tree', 'Kura+the+Boundless+Sky', 'Nashi+Moon+Sages+Scion',
    'Spirit-Sisters+Call', 'Tamiyo+Compleated+Sage', 'Tezzeret+Betrayer+of+Flesh', 'The+Kami+War',
    'The+Wandering+Emperor'

    ]

for i in cards_NeonDynasty2022_mythic:

    url = 'https://www.mtggoldfish.com/price/Kamigawa+Neon+Dynasty/' + i
    #url = 'https://www.mtggoldfish.com/price/Kamigawa+Neon+Dynasty/Ao+the+Dawn+Sky#paper'

    r = requests.get(url)

    #print(r.text)

    soup = BeautifulSoup(r.text, 'html.parser')
    #print(soup.title.text)


    #cardName = soup.find('h3', {'class':'gatherer-name'}).text
    price = soup.find('div', {'class':'price-box-price'}).text
    print(i)
    print(price)