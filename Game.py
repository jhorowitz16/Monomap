# Simplified game logic to model Monopoly space distributions

import random

TURNS = 1000000
NUM_SQUARES = 36
GO_TO_JAIL = 27
JAIL = 9
ROWS = 4
PER_ROW = 9


# debugging
ROLL_DEBUG = False 
MOVE_DEBUG = False 
COUNT_DEBUG = False
END_TURN_DEBUG = False 

spaces_strings = \
['GO.', 'MED', 'CC1', 'BAL', 'ITX', 'RR1', 'ORI', 'CH1', 'VER', 'CON',
'JAL', 'SCP', 'ECO', 'STA', 'VIR', 'RR2', 'STJ', 'CC2', 'TEN', '.NY',
'FPK', 'KEN', 'CH3', 'IND', 'ILL', 'RR3', 'ATL', 'VEN', '.WW', 'MAR',
'GTJ', 'PAC', 'NCA', 'CC4', 'PEN', 'RR4', 'CH4', 'PPL', 'LTX', 'BWK']

ss = spaces_strings

def simple():
    # for now, each space is represented as an integer 0 to 36
    print('----------------- begin ------------------') 
    freq = [0 for _ in range(36)]
    jail_counts = []

    def roll():
        """
        roll is the sum of the two dice, followed by T/F for doubles
        """
        def die():
            return random.randint(1, 6) 
        result = (die(), die())
        debug(result, ROLL_DEBUG)
        return (sum(result), result[0] == result[1])
    
    player_pos = 0


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
        nonlocal jail_counts
        jail_counts += [count]
        debug("\n---------- ", END_TURN_DEBUG)


    for _ in range(TURNS):
        turn()

    def display_freq():
        print('///////////////////////////')
        for row in range(ROWS):
            for i in range(len(freq)//ROWS):
                print(ss[i + row*PER_ROW], '|||', freq[i + row*PER_ROW])
            print('.............')
        print('///////////////////////////')

    display_freq()
    import pdb; pdb.set_trace()


def debug(s, b):
    if b:
        print (s)
        
simple()
