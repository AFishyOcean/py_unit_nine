import card
import deck

new_card = card.Card(9, "Hearts")
print(new_card.suit)

new_deck = deck.Deck()
print(new_deck.cards[0].rank + "of" + new_deck.cards[0].suit)