import random
class Character:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
class Item:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class Cell:
    def __init__(self, has_wall=False):
        self.character = None
        self.item = None
        self.has_wall = has_wall


class GameMap:
    def __init__(self, size):
        self.size = size
        self.map = [[Cell() for _ in range(size)] for _ in range(size)]

    def place_character(self, character, x, y):
        self.map[y][x].character = character

    def place_item(self, item, x, y):
        self.map[y][x].item = item

    def is_valid_move(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size and not self.map[y][x].has_wall

    def move_character(self, character, new_x, new_y):
        current_cell = self.map[new_y][new_x]
        if self.is_valid_move(new_x, new_y) and not current_cell.character:
            old_x, old_y = self.find_character(character)
            self.map[old_y][old_x].character = None
            self.map[new_y][new_x].character = character

    def find_character(self, character):
        for y, row in enumerate(self.map):
            for x, cell in enumerate(row):
                if cell.character == character:
                    return x, y
        return None, None

    def print_map(self):
        for row in self.map:
            for cell in row:
                if cell.character:
                    print(cell.character.symbol, end=' ')
                elif cell.item:
                    print(cell.item.symbol, end=' ')
                elif cell.has_wall:
                    print('#', end=' ')  # Символ стены
                else:
                    print('-', end=' ')
            print()  # Перенос строки для новой строки карты




# Создание персонажей
hero = Character("Hero", "H")
monster = Character("Monster", "M")

# Создание предметов
sword = Item("Sword", "S")
potion = Item("Potion", "P")

# Создание игровой карты
game_map = GameMap(5)

# Размещение персонажей и предметов на карте
game_map.place_character(hero, 2, 2)
game_map.place_character(monster, 4, 4)
game_map.place_item(sword, 1, 3)
game_map.place_item(potion, 3, 1)

# Вывод карты в консоль
game_map.print_map()

# Добавление стен на карту
game_map.map[1][1].has_wall = True
game_map.map[3][3].has_wall = True

# Изменения в коде для передвижения персонажей с учётом стен
game_map.move_character(hero, 3, 2)  # Перемещение героя вправо
game_map.move_character(monster, 4, 3)  # Перемещение монстра вниз