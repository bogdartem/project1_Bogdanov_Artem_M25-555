#!/usr/bin/env python3
from labyrinth_game.player_actions import show_inventory
from labyrinth_game.utils import describe_current_room
# import labyrinth_game.constants


def main():
    """Main function of the labyrinth game."""
    print('Добро пожаловать в Лабиринт сокровищ!')
    
    game_state = {
        'player_inventory': [],  # Инвентарь игрока
        'current_room': 'entrance',  # Текущая комната
        'game_over': False,  # Значения окончания игры
        'steps_taken': 0  # Количество шагов
    }
    describe_current_room(game_state)
    # show_inventory(game_state)
    # Создайте цикл while, который будет работать, пока игра не окончена.
    # Внутри цикла считывайте команду от пользователя.
    


if __name__ == "__main__":
    main()
