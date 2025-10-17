from labyrinth_game.constants import ROOMS  # , room_data_message


def describe_current_room(game_state):
    """Описание текущей комнаты."""
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]
    # print(room_data.keys())  # ['description', 'exits', 'items', 'puzzle']
    print(f"== {current_room.upper()} ==")
    print(room_data['description'])
    if room_data['items']:
        print('Заметные предметы: ', ', '.join(room_data['items']))
    if room_data['exits']:
        print('Выходы: ', ', '.join(room_data['exits'].keys()))
    if room_data['puzzle'] is not None:
        print('Кажется, здесь есть загадка (используйте команду solve).')

    # for key in room_data.keys():
    #     if room_data[key] is not None:
    #         print(f'{room_data_message[key]} {room_data[key]}')


def show_help():
    """Показать доступные команды."""
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение")
