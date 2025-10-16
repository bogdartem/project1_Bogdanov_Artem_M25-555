from labyrinth_game.constants import ROOMS, room_data_message


def describe_current_room(game_state):
    """Описание текущей комнаты."""
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]
    
    print(f"== {current_room.upper()} ==")
    print(room_data['description'])
    # print(room_data.keys())  # ['description', 'exits', 'items', 'puzzle']
    if room_data['items']:
        # print('Заметные предметы: ', (', ').join())
        pass

    # for key in room_data.keys():
    #     if room_data[key] is not None:
    #         print(f'{room_data_message[key]} {room_data[key]}')


"""
Функция описания комнаты. 
В utils.py создайте функцию describe_current_room(game_state).
Она должна принимать один аргумент — словарь game_state.
Используя game_state['current_room'], получите из константы ROOMS данные о текущей комнате.
Последовательно выведите на экран:
Название комнаты в верхнем регистре (например, == ENTRANCE ==).
Описание комнаты.
Список видимых предметов. Если они есть, то вывести сообщение "Заметные предметы:" с перечисленными предметами
Доступные выходы("Выходы:").
Сообщение о наличии загадки, если она есть("Кажется, здесь есть загадка (используйте команду solve).")
"""