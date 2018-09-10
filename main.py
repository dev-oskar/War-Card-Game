from enum import Enum
from enum import IntEnum
from random import *

# Initalize empty deck
full_deck = []
partial_deck = []
player_one_cards = []
player_two_cards = []

# Cards enum for playing cards
class Card(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11  # JOPEK
    QUEEN = 12  # DAMA
    KING = 13  # KRÓL
    ACE = 14  # AS
    JOKER = 15

# Suit enum for playing cards
class Suit(Enum):
    SPADES = 'spades'  # PIK (WINO)
    CLUBS = 'clubs'  # TREFL
    HEARTS = 'hearts'  # SERCA (KIER)
    DIAMONDS = 'diamonds'  # DZWONEK

# Class to hold information for playing cards
class PlayingCard:
    def __init__(self, card_value, card_suit):
        self.card = card_value
        self.suit = card_suit

# Function to deal full deck of cards
def create_deck():
    for suit in Suit:
        for card in Card:
            full_deck.append(PlayingCard(Card(card), Suit(suit)))
    return full_deck

# Draw single card from "deck"
def draw_card(deck):
    rand_card = randint(0, len(deck) -1)
    return deck.pop(rand_card)

# Deal two players for the game of war
def deal_war():
    while len(partial_deck) > 0:
        player_one_cards.append(draw_card(partial_deck))
        player_two_cards.append(draw_card(partial_deck))


create_deck()
partial_deck = list(full_deck)
deal_war()

for i in range(0, len(player_one_cards)):
    if player_one_cards[i].card > player_two_cards[i].card:
        print("Player One wins with: ", player_one_cards[i].card)
        print("Player Two loses with: ", player_two_cards[i].card)
    if player_two_cards[i].card > player_one_cards[i].card:
        print("Player Two wins with: ", player_one_cards[i].card)
        print("Player One loses with: ", player_two_cards[i].card)
    else:
        print("WAR!")