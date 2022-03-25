import requests
import re
from mtgsdk import Card
from mtgsdk import Set


class MTG(object):
    def __init__(self):
        self.sdk = None
        self.applicable_sets = ['NEO']
    def getCards_MTG_SDK(self):

        mtg_sets = self.applicable_sets
        for mtg_set in mtg_sets:

            card_data = self.requestCards(f'https://api.magicthegathering.io/v1/cards?set={mtg_set}&page=1')

            response = card_data['response']
            cards = card_data['cards']

            # number of pages of cards
            pages = re.search(r'page=\d+', response.headers['Link']).group()
            pages = int(pages.split('=')[1])

            for i in range(pages):
                cards += self.requestCards(f'https://api.magicthegathering.io/v1/cards?set={mtg_set}&page={i+1}')['cards']
                print(f'Page {i+1} of {mtg_set}: Saved!')

    def requestCards(self, url):
        response = requests.get(url)
        cards = response.json()['cards']
        modified_cards = []
        for card in cards:
            card = {
                'name': card['name'],
                'manaCost': '' if not 'manaCost' in card else ''.join(
                    [char for char in card['manaCost'] if
                     char not in ('{', '}')]
                ),
                'cmc': card['cmc'],
                'type': card['type'],
                'rarity': card['rarity'],
                'set': card['set'],
                'text': '' if not 'text' in card else card['text'],
                'imageUrl': '' if not 'imageUrl' in card else card['imageUrl']
            }
            modified_cards.append(card)

        return {'response': response, 'cards': modified_cards}

    """
    def saveCards(cards):
        cards = sorted(cards, key=lambda card: card['name'])
        for i, _key in enumerate(cards):
            if cards[i]['name'] != cards[i - 1]['name']:
                serialzer = CardSerializer(data=cards[i])
                if serialzer.is_valid():
                    serialzer.save()
    """