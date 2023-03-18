from dataclasses import dataclass
@dataclass
class Card:
    rank: str
    suit: str
    ab: str

card1 = Card("Q", "hearts")
card2 = Card("Q", "hearts")
print(card1 == card2)
# True
print(card1.rank)
# 'Q'
print(card1)
Card(rank='Q', suit='hearts')