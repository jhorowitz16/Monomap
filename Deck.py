from Card import Card

class Deck:
    """
    represent a deck of cards - either chance or community chest
    """

    def __init__(self, list_of_cards=[]):
        self.cards = list_of_cards
    
    def draw(self):
        """
        return the top card and put it at the bottom
        """
        card = self.cards[0]
        self.cards = self.cards[1:] + [card]
        return card

    def print_deck(self):
        print('-------')
        for c in self.cards:
            print(c)
        print('-------')

    def __str__(self):
        ret_str = ''
        for c in self.cards:
            ret_str += str(c) + ' '
        return '(' + ret_str + ')'

    def __repr__(self):
        return str(self)
            


        

