import time
import os
import sys
import random


def clear(s):
    time.sleep(s)
    os.system("cls||clear")


def board_size():
    clear(0)
    board_size = input("Board size: (X * X size)\n\n- ")
    while True:
        if board_size.isnumeric():
            print("\nLoading board size...")
            return int(board_size)
        else:
            print("\nLoading default board size...")
            return 3


def init_board(board_size=3):
    board = []
    for row in range(board_size):
        row = []
        for col in range(board_size):
            row.append(".")
        board.append(row)
    return board


def change_player(player):
    if player == "0":
        player = "X"
    else:
        player = "0"
    return player


def switch_turn(turn):
    if turn == "A":
        turn = "B"
    else:
        turn = "A"
    return turn


def get_move(board, player):
    while True:
        move = input("Please give valid cooridantes:\n- ")
        move = move.upper()
        if move == "QUIT" or move == "EXIT":
            print("\nRegistration failed.")
            sys.exit()
        else:
            if len(move) == 2 and move[0].isalpha() and move[1].isnumeric():
                row = ord(move[0]) - 65
                col = int(move[1]) - 1
                if row > len(board)-1 or col > len(board)-1 or col == -1:
                    print("\nOut of the board!\n")
                    clear(1)
                    print(f"{player}'s turn")
                    print_board(board)
                    continue
                return row, col
            else:
                print("\nNot valid!\n")
                clear(1)
                print(f"{player}'s turn")
                print_board(board)
                # continue


def get_ai_move(board, player):
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    while True:
        row = random.randint(0, len(board)-1)
        col = random.randint(0, len(board)-1)
        if board[row][col] != ".":
            continue
        else:
            print(f"AI's move: {abc[row]}{col+1}")
            return row, col


def mark(board, player, row, col, turn):
    if board[row][col] == "X" or board[row][col] == "0":
        print("\nReserved coordinate!\n")
    else:
        board[row][col] = player
        turn = switch_turn(turn)
        player = change_player(player)
    return player, turn


def has_won(board, player):
    rows = len(board)
    cols = len(board[0])
    end = True
    for i in range(rows):
        end = True
        for j in range(cols):
            if board[i][j] != player:
                end = False
                continue
        if end:
            return True
    for i in range(rows):
        end = True
        for j in range(cols):
            if board[j][i] != player:
                end = False
                continue
        if end:
            return True
    end = True
    list = []
    list2 = []
    for i in range(cols):
        if board[i][i] == player:
            list.append(0)
        if board[i][cols - 1 - i] == player:
            list2.append(0)
    if len(list) == len(board) or len(list2) == len(board):
        return True
    else:
        return False


def is_full(board):
    for row in board:
        for item in row:
            if item == ".":
                return False
    return True


def print_board(board):
    print()
    string = "  "
    for number in range(1, len(board)+1):
        string += str(number) + "   "
    list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    msg = ""
    for i, row in enumerate(board):
        element = row[0]
        element_str = f"{list[i]}" + '{:^{width}}'.format(element, width=3)
        msg = msg + element_str
        for element in row[1:]:
            element_str = '|{:^{width}}'.format(element, width=3)
            msg = msg + element_str
        msg = msg + '\n'
        if i is not len(board) - 1:
            element_str = " " + len(board) * "{:-^{width}}+" .format("", width=3)
            msg = msg + element_str[:-1]
            msg = msg + '\n'
    print(string + "\n" + msg)


def print_result(winner):
    if winner == 0:
        print("It's a tie!")
    else:
        print(f"{winner} has won!")


def tictactoe_game(mode="HUMAN-HUMAN"):
    board = init_board(board_size())
    player = "X"
    turn = "A"
    if mode == "HUMAN-HUMAN":
        while True:
            clear(1)
            print(f"{player}'s turn")
            print_board(board)
            row, col = get_move(board, player)
            player, turn = mark(board, player, row, col, turn)
            player = change_player(player)
            turn = switch_turn(turn)
            if has_won(board, player):
                clear(1)
                winner = player
                print_result(winner)
                print_board(board)
                break
            if is_full(board):
                clear(1)
                winner = 0
                print_result(winner)
                print_board(board)
                break
            player = change_player(player)
            turn = switch_turn(turn)
    elif mode == "HUMAN-AI":
        player = "0"
        while True:
            clear(1)
            print(f"{player}'s turn")
            print_board(board)
            if turn == "B":
                row, col = get_ai_move(board, player)
            elif turn == "A":
                row, col = get_move(board, player)
            player, turn = mark(board, player, row, col, turn)
            player = change_player(player)
            turn = switch_turn(turn)
            if has_won(board, player):
                clear(1)
                winner = player
                print_result(winner)
                print_board(board)
                break
            if is_full(board):
                clear(1)
                winner = 0
                print_result(winner)
                print_board(board)
                break
            player = change_player(player)
            turn = switch_turn(turn)
    elif mode == "AI-HUMAN":
        player = "0"
        while True:
            clear(1)
            print(f"{player}'s turn")
            print_board(board)
            if turn == "B":
                row, col = get_move(board, player)
            elif turn == "A":
                row, col = get_ai_move(board, player)
            player, turn = mark(board, player, row, col, turn)
            player = change_player(player)
            turn = switch_turn(turn)
            if has_won(board, player):
                clear(1)
                winner = player
                print_result(winner)
                print_board(board)
                break
            if is_full(board):
                clear(1)
                winner = 0
                print_result(winner)
                print_board(board)
                break
            player = change_player(player)
            turn = switch_turn(turn)
    else:
        while True:
            clear(1)
            print(f"{player}'s turn")
            print_board(board)
            row, col = get_ai_move(board, player)
            mark(board, player, row, col, turn="")
            if has_won(board, player):
                clear(1)
                winner = player
                print_result(winner)
                print_board(board)
                return
            if is_full(board):
                clear(1)
                winner = 0
                print_result(winner)
                print_board(board)
                return
            player = change_player(player)
            turn = switch_turn(turn)


def main_menu():
    clear(0)
    while True:
        mode = input("Game mode:\n\n1. HUMAN vs. HUMAN\n2. HUMAN vs. AI\n3. AI vs. HUMAN\n4. AI vs. AI\n\n- ")
        if mode == "1":
            tictactoe_game("HUMAN-HUMAN")
            return
        elif mode == "2":
            tictactoe_game("HUMAN-AI")
            return
        elif mode == "3":
            tictactoe_game("AI-HUMAN")
            return
        elif mode == "4":
            tictactoe_game("AI-AI")
            return
        else:
            print("\nNot valid mode.")
            clear(2)


if __name__ == '__main__':
    main_menu()
