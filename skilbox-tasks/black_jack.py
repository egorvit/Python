import random


class Card:

    suits = ["Черви", "Буби", "Пики", "Крести"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit='', rank=''):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + "/" + self.suit


class Deck:

    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        num = len(self.cards)
        for i in range(num):
            j = random.randrange(i, num)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def extract(self, player, amount):
        try:
            if amount == 2:
                card_1 = self.cards.pop()
                card_2 = self.cards.pop()
                player.cards_player.append(card_1)
                player.cards_player.append(card_2)
            elif amount == 1:
                card_1 = self.cards.pop()
                player.cards_player.append(card_1)
        except IndexError:
            print('Карт больше нет!')


class Player:

    def __init__(self, name):
        self.name = name
        self.cards_player = []

    def info(self):
        for card in self.cards_player:
            print(card.__str__(), end=' | ')

    def counting(self):
        summ = 0
        for card in self.cards_player:
            if card.rank == 'Ace' and summ < 21:
                summ += 11
            elif card.rank == 'Ace' and summ >= 21:
                summ += 1
            elif card.rank == 'Jack' or card.rank == 'Queen' or card.rank == 'King':
                summ += 10
            else:
                summ += int(card.rank)
        return summ


def game(player, deck):
    print('Добро пожаловать в игру!')
    deck.extract(player, 2)
    while True:
        player.info()
        ask = input('Взять еще крату? Взять/Хватит: ').lower()
        if ask == 'взять':
            deck.extract(player, 1)
            if player.counting() > 21:
                print('Вы сгорели!')
                break
        elif ask == 'хватит':
            break
    return player.counting()


def computer_game(player, deck):
    deck.extract(player, 2)
    num = random.randint(0, 1)
    while True:
        if num == 1:
            deck.extract(player, 1)
            if player.counting() > 21:
                break
        else:
            break

    return player.counting()


name = input('Как вас зовут? ')
computer = Player('Computer')
man = Player(name)
test_deck = Deck()
test_deck.shuffle()
result_man = game(man, test_deck)
result_computer = computer_game(computer, test_deck)
print('\nВаш результат {}: {}'.format(name, result_man))
man.info()
print('\nРезультат компьютера: {}'.format(result_computer))
computer.info()



