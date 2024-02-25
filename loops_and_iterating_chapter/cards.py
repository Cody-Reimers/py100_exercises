suits = ["Clubs", "Diamond", "Hearts", "Spades"]
ranks = [
    "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "Jack", "Queen", "King", "Ace",
]

deck = []
for suit in suits:
    for rank in ranks:
        card = f"{rank} of {suit}"
        deck.append(card)

print(deck)