import card

class Deck:

    def __init__(self):
        self.cards = []
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(card.Card(rank, suit))

