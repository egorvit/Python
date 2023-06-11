class Cell:

    def __init__(self, number):
        self.number = number
        self.busy = False


class Board:

    def __init__(self):
        self.cell_lst = [Cell(i) for i in range(1, 10)]

    def square(self):
        print("\n")
        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(self.cell_lst[0].number, self.cell_lst[1].number, self.cell_lst[2].number))
        print('\t_____|_____|_____')

        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(self.cell_lst[3].number, self.cell_lst[4].number, self.cell_lst[5].number))
        print('\t_____|_____|_____')

        print("\t     |     |")

        print("\t  {}  |  {}  |  {}".format(self.cell_lst[6].number, self.cell_lst[7].number, self.cell_lst[8].number))
        print("\t     |     |")
        print("\n")

    def replacement(self, number_cell, number_player):

        if number_player == 1:
            self.cell_lst[number_cell].busy = True
            self.cell_lst[number_cell].number = 'X'
        elif number_player == 2:
            self.cell_lst[number_cell].busy = True
            self.cell_lst[number_cell].number = 'O'


class Player:

    def __init__(self, name, player_number):
        self.name = name
        self.lst_move = list()
        self.player_number = player_number

    def move(self, number_cell, board):
        if not board.cell_lst[number_cell - 1].busy:
            board.replacement(number_cell - 1, self.player_number)
            self.lst_move.append(number_cell)
        else:
            print(f'Клетка {number_cell} уже занята!')
            print('Выберете другую клетку\n')


def check_win(player):
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for lst_combination in solution:
        check = 0
        for i in player.lst_move:
            if i in lst_combination:
                check += 1
        if check == 3:
            return True


def game(player_1, player_2, board):
    count = 1
    while count != 10:
        board.square()
        if count % 2 != 0:
            number = int(input('Выберете клетку для хода: '))
            player_1.move(number, board)
        elif count % 2 == 0:
            number_2 = int(input('Выберете клетку для хода: '))
            player_2.move(number_2, board)

        if count >= 5 and check_win(player_1):
            print('Игрок {name} победил(а)!'.format(name=player_1.name))
            break
        elif count >= 5 and check_win(player_2):
            print('Игрок {name} победил(а)!'.format(name=player_2.name))
            break
        count += 1
    else:
        print('Ничья!')


game_board = Board()
name_1 = input('Введите имя первого игрока: ')
name_2 = input('Введите имя второго игрока: ')
player_name_1 = Player(name_1, 1)
player_name_2 = Player(name_2, 2)

game(player_name_1, player_name_2, game_board)