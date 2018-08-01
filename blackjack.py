# BLACKJACK GAME

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " " + self.suit


class Deck():

    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        whole_deck = ''

        for card in self.deck:
            whole_deck += '\n' + card.__str__()
        return 'Your deck is: ' + whole_deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        one_card = self.deck.pop()
        return one_card



class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value < 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Please state the amount of your bet: '))
        except ValueError:
            print('Your bet must be an integer number.')
        else:
            if chips.bet > chips.total:
                print("You don't have enough credit. Your current credit is {}. Please state the smaller bet".format(
                    chips.total))
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        player_action = input('Please decide if you want to hit or stand (h/s): ')
        if player_action.lower() == 'h':
            hit(deck, hand)
        elif player_action.lower() == 's':
            print ('Player stands. Dealer is playing.')
            playing = False
        else:
            print('Please try again (h/s).')
            continue
        break


def show_some(player, dealer):
    print('\n Dealer cards: ')
    print('<card hidden> ')
    print(dealer.cards[1])
    print('\n Player cards: ', *player.cards, sep='\n ')



def show_all(player, dealer):
    print('\n Dealer cards: ', *dealer.cards, sep='\n ')
    print('\n Dealer value: ', dealer.value)
    print('\n Player cards: ', *player.cards, sep='\n ')
    print('\n Player value: ', player.value)



def player_busts(player,dealer,chips):
    print('\n Player busts!')
    chips.lose_bet()


def player_wins(player,dealer,chips):
    print('\n Player won!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('\n Dealer busts!')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('\n Player won!')
    chips.lose_bet()

def push(player,dealer):
    print("It is a tie.")


while True:
    # Print an opening statement
    print("Welcome to the BLACK JACK game!")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips) # player_hand, dealer_hand, player_chips
            break


        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        # Dealer busts
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        #Player wins
        elif player_hand.value < dealer_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        # Dealer wins
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        #tie
        else:
            push(player_hand, dealer_hand, player_chips)

    # Inform Player of their chips total
    print('Your total chips are: {}'.format(player_chips.total))

    # Ask to play again
    again = input('Do you want to play again? (y/n)')
    if again == 'y':
        playing = True
        continue
    else:
        print('Thank you for playing!')
        break