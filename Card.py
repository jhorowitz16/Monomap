# represent each card as an object

class Card:
    
    # shorthand for card types
    CC = 'CC'
    CH = 'CH'
    c_types = [CC, CH]

    # shorthand for move vs collect cards
    COL = 'COL'
    MOV = 'MOV'
    e_types = [MOV, COL]

    def __init__(self, card_type=CC, effect_type=COL, money=0, abs_dist=0, 
            rel_dist=0, text='UNDEF'):
        """
        card_type: chance or community chest
        effect_type: gain something (COL) or move (MOV)
        money: amount to gain (+/-)
        abs_dist: go to that square
        rel_dist: number corresponding to special movement
            0: Back 3
            1: next RR
            2: next util
        """
        self.card_type = card_type
        self.effect_type = effect_type
        self.money = money
        self.abs_dist = abs_dist
        self.rel_dist = rel_dist
        self.text = text

    def __str__(self):
        return self.text



