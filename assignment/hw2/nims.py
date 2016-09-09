# Name: Will Fu
# Section: EE
# nims.py

def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''

    while(pile > 0):
        player1 = int(input("Player1:Plase input a number between 1 and " + str(max_stones) + ": "))

        while(player1 < 1 or player1 > max_stones):
            player1 = int(input("Player1:Plase input a number between 1 and " + str(max_stones) + ": "))        

        winner = "player1"
        pile -= player1

        if(pile <= 0):
            break

        player2 = int(input("Player2:Plase input a number between 1 and " + str(max_stones) + ": "))

        while(player2 < 1 or player2 > max_stones):
            player2 = int(input("Player2:Plase input a number between 1 and " + str(max_stones) + ": "))        

        winner = "player2"
        pile -= player2

    print("Game over")
    return winner

print(play_nims(10, 3))
    
    ## Basic structure of program (feel free to alter as you please):

#    while [pile is not empty]:
#        while [player 1's answer is not valid]:
#            [ask player 1]
#            [execute player 1's move]
#       
#        while [player 2's answer is not valid]:
#            [ask player 2]
#            [execute player 2's move]
#
#    print "Game over"
