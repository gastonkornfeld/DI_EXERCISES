import random




# Instructions
# Part 2: Create a deck of cards class.

# Internally, the deck of cards should use another class, a card class. Your requirements are:

# The Deck class should have a deal method to deal a single card from the deck
# After a card is dealt, it is removed from the deck.
# There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)

class Card():
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit




class DeckOfCards():

    def __init__(self, number_of_cards):
        self.number_of_cards = number_of_cards
        self.list_of_cards = []
        
        self.numbers = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.suits = ["heart", "Diamond", "Clubs", "Spades"]
        print("deck of cards:")
        for i in range(len(self.numbers)):
            for j in range(len(self.suits)):
                self.list_of_cards.append(Card(self.numbers[i], self.suits[j] ))
        for i in range(self.number_of_cards):
            print(f"card{i +1}: {self.list_of_cards[i].value} {self.list_of_cards[i].suit}")
        


    def deal(self):
        card_taken = random.choice(self.list_of_cards)
        self.list_of_cards.remove(card_taken)
        print(f"the car taken was {card_taken.value} {card_taken.suit}")

    def shuffle(self):
        self.list_of_cards = []
        for i in range(len(self.numbers)):
            for j in range(len(self.suits)):
                self.list_of_cards.append(Card(self.numbers[i], self.suits[j] ))
        
        random.shuffle(self.list_of_cards)
        print("deck was shuffle, deck:\n")
        for i in range(self.number_of_cards):
            print(f"card{i + 1}: {self.list_of_cards[i].value} {self.list_of_cards[i].suit}")
        

list_of_cards = DeckOfCards(52)

# print(list_of_cards)

list_of_cards.deal()
list_of_cards.shuffle()
