# Simplified game logic to model Monopoly space distributions

import random
from Card import Card
from Deck import Deck
random.seed(0)

TURNS = 100
NUM_SQUARES = 40 
GO_TO_JAIL = 30 
JAIL = 10 
ROWS = 4
PER_ROW = 9

# spaces
GO_SPACE = 0
JAIL_SPACE = 9
CC_SPACES = [2, 17, 33]
CH_SPACES = [7, 22, 36]

# strings
CH = 'CH'
CC = 'CC'


# debugging
ROLL_DEBUG = False 
MOVE_DEBUG = False 
COUNT_DEBUG = False
END_TURN_DEBUG = False 
DECK_DEBUG = True

spaces_strings = \
['GO.', 'MED', 'CC1', 'BAL', 'ITX', 'RR1', 'ORI', 'CH1', 'VER', 'CON',
'JAL', 'SCP', 'ECO', 'STA', 'VIR', 'RR2', 'STJ', 'CC2', 'TEN', '.NY',
'FPK', 'KEN', 'CH3', 'IND', 'ILL', 'RR3', 'ATL', 'VEN', '.WW', 'MAR',
'GTJ', 'PAC', 'NCA', 'CC4', 'PEN', 'RR4', 'CH4', 'PPL', 'LTX', 'BWK']

for i in CC_SPACES + CH_SPACES:
    print (spaces_strings[i])

ss = spaces_strings



def simple():
    # for now, each space is represented as an integer 0 to 36
    print('----------------- begin ------------------') 
    freq = [0 for _ in range(NUM_SQUARES)]

    # initialize the player at Go
    player_pos = GO_SPACE 

    def roll():
        """
        roll is the sum of the two dice, followed by T/F for doubles
        """
        def die():
            return random.randint(1, 6) 
        result = (die(), die())
        debug(result, ROLL_DEBUG)
        return (sum(result), result[0] == result[1])
    


    def move(count):
        """
        count refers to turn number
        don't move if count is 3 and roll returns a double
        roll the dice, and update player position
        update frequency table
        """

        debug(">>> " + str(count), COUNT_DEBUG)

        nonlocal player_pos
        # roll
        r = roll()
        if r[1] and count == 3:
            # don't make the move...
            debug("go to jail from 3 doubles", MOVE_DEBUG)
            player_pos = JAIL
            freq[player_pos] += 1
            return True

        player_pos = (player_pos + r[0]) % NUM_SQUARES 

        # check jail
        if player_pos == GO_TO_JAIL:
            # hit the go to jail spot on the board, go to jail 
            # distinguish this from actual jail spot tho
            freq[player_pos] += 1
            player_pos = JAIL
            debug("go to jail " + str(ss[player_pos]), MOVE_DEBUG)
            return True

        # pending: deal with cards that can end a turn
        if player_pos in CC_SPACES:
            debug(str(ss[player_pos]), MOVE_DEBUG)
            card = cc_deck.draw()
            debug("community chest card " + str(card), MOVE_DEBUG)


        elif player_pos in CH_SPACES:
            debug(str(ss[player_pos]), MOVE_DEBUG)
            card = ch_deck.draw()
            debug("chance card " + str(card), MOVE_DEBUG)
            

        # normal roll - update the frequency of the square
        freq[player_pos] += 1

        debug("successful move to " + str(ss[player_pos]), MOVE_DEBUG)
        # continue when double
        return not r[1]


    def turn():
        """
        take a single player turn - updating positions, ignoring effects
        cap at three "moves"
        move() deals with movement
        """
        count = 0  # turn counter
        end = False
        while not end:
            count += 1
            end = move(count)
        debug("\n---------- ", END_TURN_DEBUG)


    for _ in range(TURNS):
        turn()

    def display_freq():
        print('///////////////////////////')
        for row in range(ROWS):
            for i in range(10):
                print(ss[i + row*10], '|||', freq[i + row*10])
            print('.............')
        print('///////////////////////////')

    display_freq()

    # sort by frequency
    pairs = []
    for i in range(NUM_SQUARES):
        pair = (ss[i], freq[i])
        pairs += [pair]
    pairs.sort(key=lambda x: x[1])
    for pair in pairs:
        print(pair[0], '|||', pair[1])




def build_cc_deck():
    """ 
    for now - hard coding the cards that matter, plus blank cards (collect)
    one global community chest deck for the whole simulation

    """
    # community chest is Go, Jail, then money
    CC_Deck = []
    for i in range(14):
        c = Card('CC', 'COL', i, 0, 0, str(i))
        CC_Deck.append(c) 
    go = Card('CC', 'MOV', 0, GO_SPACE, 0, "go to go")
    jail = Card('CC', 'MOV', 0, JAIL_SPACE, 0, "go to jail")
    CC_Deck += [go, jail]
    random.shuffle(CC_Deck)
    CC_Deck = Deck(CC_Deck)
    if DECK_DEBUG:
        CC_Deck.print_deck()
    return CC_Deck
    

def build_ch_deck():
    """ 
    for now - hard coding the cards that matter, plus blank cards (collect)
    one global chance deck for the whole simulation

    """
    # community chest is Go, Jail, then money
    CH_Deck = []
    for i in range(16):
        c = Card('CH', 'COL', i, 0, 0, str(i))
        CH_Deck.append(c) 
    go = Card('CH', 'MOV', 0, GO_SPACE, 0, "go to go")
    jail = Card('CH', 'MOV', 0, JAIL_SPACE, 0, "go to jail")
    CH_Deck += [go, jail]
    random.shuffle(CH_Deck)
    CH_Deck = Deck(CH_Deck)
    if DECK_DEBUG:
        CH_Deck.print_deck()
    return CH_Deck


def draw_card(deck):
    """
    pop the top card from the deck, move it to the bottom, and return
    """
    return (deck[0], deck[1:] + [deck[0]])



# utils
def debug(s, b):
    if b:
        print (s)
        

cc_deck = build_cc_deck()
print(cc_deck)
ch_deck = build_ch_deck()

simple()
print(cc_deck)
