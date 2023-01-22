# Card Game

import random
from random import randint
from random import shuffle

card_suit = ['h', 's', 'c', 'd']
class crazy8CPU():

    def __init__(self):
        '''none -> none
        initializies all the lists for player and cpu.
        Sets up suits, ranks, value of cards, the deck, play pile, players' hands, and crazy 8 suit'''
        self.suit = ['h', 's', 'c', 'd']
        self.cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.value = [2, 3, 4, 5, 6, 7, 50, 9, 10, 10, 10, 10, 10, 1]
        self.deck = list((x, y) for x in self.suit for y in self.cards)
        self.player = []
        self.dealer = []
        self.play_pile = []
        self.suit_8 = '' # needed for crazy 8 card to change suit

    def value_of_cards(self, card):
        ''' str -> Num
        Takes a card from self.cards and gives the pertaining value
        to each card, respectively based on rank'''
        return self.value[self.cards.index(card[1])]
     
    def deal_cards(self):
        '''sig: None -> None
        Shuffles the deck and gives 5 cards to each player and dealer
        '''
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
        shuffle(self.deck)
        for i in range(5):
            self.player.append(self.deck.pop())
            self.dealer.append(self.deck.pop())
        self.play_pile = self.deck.pop()
        print("Welcome to CRAZY 8...just place a card that matches the play pile's suit or rank.")
        print("Cards with 8 allows you to chance the suit.")
        print("Cards with 2 makes someone draw 2.")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")

    def valid_player(self, inpu):
        '''sig: str (Card) -> Number
        sees if the players card is valid for play.
        makes each card '''
        if inpu.isdigit() == False:
            return 0
        if int(inpu) > len(self.player): # makes sure user uses a card that exists 
            print('\nThe number of card is greater than total cards in hand.')
            print('Please input valid card')
            return 0
        if self.player[int(inpu)-1][1] == '8': # if crazy 8 is played...user must input new suit
                self.play_pile = self.player.pop(int(inpu)-1)
                self.suit_8 = ''
                while self.suit_8 not in card_suit:
                    self.suit_8 = input("Input a new suit: h, s, c, d\n")
                print("\nThe new suit is:", self.suit_8)
                return 1
        if self.suit_8 != '': #when crazy 8 is played, and player places a card with the chosen suit
            if self.player[int(inpu)-1][0] == self.suit_8:
                self.play_pile = self.player.pop(int(inpu)-1)
                self.suit_8 = ''
                return 1
            else:
                print("\nNot a valid suit. \nTry again.")
                return 0

        if self.suit_8 == '': # regular play 
            if self.player[int(inpu)-1][0] == self.play_pile[0] or self.player[int(inpu)-1][1] == self.play_pile[1]:
                self.play_pile = self.player.pop(int(inpu)-1)
                return 1
            else:
                print("Invalid card. Place a card with valid suit or number")
                print("\nTry again.")
                return 0
                        
    def player_play(self):
        '''Sig: None -> None
        Functions as gameplay for player1 by user inputting a number of a card they want to play'''
        played = 0
        dop = ''
        print("\nPlayer's turn. Please place a card or draw.")
        while len(self.deck)>0 and played == 0:
            print("\nPlayer's cards:", self.player)
            print("\nPlay pile:", self.play_pile)
            dop = input("Enter 0 if you need to draw a card. Otherwise, input valid card.\n")
            if dop == "0": # just to draw a card 
                self.player.append(self.deck.pop())
            else:
                played = self.valid_player(dop) # this activates the method for when cards are played, including crazy 8
        if len(self.player) == 0:
            print("You are out of cards.")
            return
        elif len(self.deck) == 0:
            print("Deck is empty.")
            return
        else:
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
            self.dealer_play()
    

    def dealer_valid(self):
        '''sig: None -> None
        Determines whether a card in dealer hand is valid for play'''
        if len([card for card in self.dealer if card[1] == '8']) > 0:
            self.play_pile = [card for card in self.dealer if card[1] == '8'][0]
            self.dealer.remove(self.play_pile)
            dealer_suits = [card[0] for card in self.dealer]
            self.new_suit = max(set(dealer_suits), key=dealer_suits.count)
            print("\nNew suit is :", self.suit_8)
            return 1
        if self.suit_8 != '':
            matching = []
            for card in self.dealer:
                if card[0] == self.suit_8:
                    matching.append(card)
            if len(matching) > 0:
                matching_values = list(map(self.value_of_cards, matching))
                self.play_pile = matching[matching_values.index(max(matching_values))]
                self.dealer.remove(self.play_pile)
                self.suit_8 = ''
                return 1
            else:
                return 0
        if self.suit_8 == '':
            matching = []
            for card in self.dealer:
                if card[0] == self.play_pile[0] or card[1] == self.play_pile[1]:
                    matching.append(card)
            if len(matching) > 0:
                matching_values = list(map(self.value_of_cards, matching))
                self.play_pile = matching[matching_values.index(max(matching_values))]
                self.dealer.remove(self.play_pile)
                return 1
            else:
                return 0

        
                

    def dealer_play(self):
        '''sig: none -> ???
        this acts as the computer's turn.
        can draw a card until can be played, or just play a card. automatic'''
        print("\nDealer's turn.")
        played = 0
        i = 0 # accumulates the number of cards the dealer drew
        while len(self.deck)>0 and played == 0:
            played = self.dealer_valid() #a method that sees if a card in dealer's deck is valid
            if played == 0:
                self.dealer.append(self.deck.pop()) # acts as dealer's draw from deck
                i +=1 # accumulates the num of cards drew
        print("Dealer drew", i, "cards.")
        if len(self.dealer) == 0:
            print("Dealer is out of cards.")
            return
        elif len(self.deck) == 0:
            print("Deck is empty.")
            return
        else:
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
            self.player_play()
        
        
   
    def points(self): # works
        '''sig: none -> none
        calculates points and prints who won'''
        p_points = 0
        d_points = 0
        for card in self.player:
            p_points = p_points + self.value_of_cards(card)
        for card in self.dealer:
            d_points = d_points + self.value_of_cards(card)

        print("Player's points", p_points)
        print("Dealer's points", d_points)

        if p_points < d_points:
            print("Player wins!!!!!!")
        elif p_points > d_points:
            print("Dealer wins. ;( D:")
        else:
            print("DRAW!!!!!")
    

def run_crazy8():
    '''sig: None -> None
    runs the Crazy8 game: vs. computer or vs another player'''
    x = 0 
    while x != "1" or x != "2":
        x = input("\nPlease select the amount of players: 1, 2\nor input 'exit' to exit game.\n")
        
        if x == "exit".lower():
            exit()
        elif int(x) == 2:
            Run = crazy8()
            Run.deal_cards()
            Run.player1_play()
            Run.player2_play()
            Run.dealer_play()
            Run.points()
        elif int(x) == 1:
            Run = crazy8CPU() # class with just 1 player
            Run.deal_cards()
            Run.player_play()
            Run.dealer_play()
            Run.points()
        
            
    else:
        print("Try again.")
        

run_crazy8()

        
        
    
