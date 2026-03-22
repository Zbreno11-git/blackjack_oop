from random import shuffle

#Deck basic definitions
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')
#Values of each card
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}

game_on = True

class Card:
    #Represents a card
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    #Represents the whole deck (52 cards)
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    def shuffle(self):
        shuffle(self.deck)
    def deal(self):
        return self.deck.pop()


class Player:
    #Managa chips, bets, and actual hand
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []

    def __str__(self):
        return f'Player {self.name} has {self.chips} chips!'

    def aposta(self):
        #Requests and validates the bet amount against the player's balance.
        bet = int(input('Enter your bet: '))
        while bet > self.chips:
            print("You don't have enough chips!")
            bet = int(input('Enter your bet: '))
            continue
        else:
            return bet
    def add_card(self, new_card):
        self.hand.append(new_card)
    def add_chips(self, new_chips):
        self.chips += new_chips
    def loss_chips(self, new_chips):
        self.chips -= new_chips

class Dealer:
    #Represents the Dealer (House) with its own hand.
    def __init__(self, name):
        self.name = name
        self.hand = []
    def add_card(self, new_card):
        self.hand.append(new_card)

#Helper functions for bet management
def ganhar_bet(a = 0):
    p1.add_chips((a * 2))

def perder_bet(a = 0):
    p1.loss_chips(a)

#Terminal display functions
def show_some():
    print('Player one: ')
    for c in p1.hand:
        print(f'->{c}', end=' ')

    print('\nDealer: ')
    print(f'-> {dealer.hand[0]}')

def show_all():
    print('Player one: ')
    for c in p1.hand:
        print(f'->{c}', end=' ')
    print('\nDealer: ')
    for c in dealer.hand:
        print(f'->{c}', end=' ')


def hit_stand():
    while True:
        h_s = str(input('Hit or stand? ')).lower()
        if h_s == 'hit':
            p1.add_card(new_deck.deal())
            show_some()
            if calculate_hand(p1.hand) > 21:
                break
        elif h_s == 'stand':
            print("\nPlayer stands... Dealer's turn: ")
            break
        else:
            print('Invalid input. Try again!')

#Calculates hand total, treating Ace as 11 or 1 as needed
def calculate_hand(hand):
    total = 0
    aces = 0
    for c in hand:
        if c.rank != 'Ace':
            total += c.value
        else:
            aces += 1
            total += 11
        #Adjust for Aces if total exceeds 21
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def dealer_play():
    while True:
        dealer_hand = calculate_hand(dealer.hand)
        if dealer_hand < 17:
            dealer.add_card(new_deck.deal())
        else:
            break
    return dealer_hand

#Compares scores to determine the round winner.
def check_winner(a):
    total_player = calculate_hand(p1.hand)

    if total_player == a:
        return 0
    elif total_player > a:
        return 1
    else:
        return 2

p1 = Player('Player One', 100)

while game_on:
    print('='*10, 'WELCOME TO BLACKJACK'.center(10), '='*10)

    new_deck = Deck()
    new_deck.shuffle()

    dealer = Dealer('Dealer')

    p1.hand = []
    dealer.hand = []

    print(f'\nPlayer One Chips: {p1.chips}')

    aposta = p1.aposta()

    for card in range(2):
        p1.add_card(new_deck.deal())
        dealer.add_card(new_deck.deal())

    show_some()

    print('\nPlayer turn: ')

    hit_stand()

    actual_value = calculate_hand(p1.hand)
    if actual_value > 21:
        print('\nPlayer bust... Dealer wins!')
        perder_bet(aposta)
        continue
    else:
        dealer_total = dealer_play()

        if dealer_total > 21:
            print('\nDealer bust... Player wins!')
            show_all()
            ganhar_bet(aposta)
            print(f'\nPlayer One Chips: {p1.chips}')
            continue
        else:
            show_all()
            print(f'\nYour hand value: -> {actual_value}')
            print(f'\nDealer hand value: -> {dealer_total}\n')

    show_all()

    winner = check_winner(dealer_total)

    if winner == 0:
        print("\n->It's a draw! Bet returned!")
    if winner == 1:
        print('\n->Player wins!')
        ganhar_bet(aposta)
        print(f'\nPlayer One Chips: {p1.chips}')
    if winner == 2:
        print('\n->Dealer wins!')
        perder_bet(aposta)
        print(f'\nPlayer One Chips: {p1.chips}')

    if p1.chips == 0:
        print("\nYou're out of chips! - Dealer wins!")
        break

    continuar = str(input('Do you want to play again? [y/n] ')).lower()
    if continuar == 'y':
        game_on = True
        continue
    if continuar == 'n':
        print('Goodbye!')
        game_on = False
