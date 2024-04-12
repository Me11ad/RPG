import random

class Character:
    def __init__(self, cell, name, symbol):
        self.name = name
        self.symbol = symbol 
        self.cell = cell

    def move(self, movement):
        x, y = self.pos
        game_map = self.cell.gamemap
        
        if movement == 'up':
            if game_map.is_valid_move(x,y-1):
                game_map.move_character(self, (x,y-1))
        if movement == 'down':
            if game_map.is_valid_move(x, y+1):
                game_map.move_character(self, (x,y+1))
        elif movement == 'left':
            if game_map.is_valid_move(x-1, y):
                game_map.move_character(self, (x-1,y))
        elif movement == 'right':
            if game_map.is_valid_move(x+1, y):
                game_map.move_character(self, (x+1,y))      
    

class Item:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class Cell:
    def __init__(self, pos, map, has_wall=False):
        self.character = None
        self.item = None
        self.has_wall = has_wall
        self.pos = pos
        self.gamemap = map
    

    


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
    
    def get_cell_at(self, x, y):
        return self.map[y][x]
    
    def move_character(self, character, new_pos):
        new_x, new_y = new_pos
        self.map[new_y][new_x].character = character
        character.cell.character = None
        character.cell = self.map[new_y][new_x]

                

    # def move_character(self, character, new_x, new_y):
    #     current_cell = self.map[new_y][new_x]
    #     if self.is_valid_move(new_x, new_y) and not current_cell.character:
    #         old_x, old_y = self.find_character(character)
    #         self.map[old_y][old_x].character = None
    #         self.map[new_y][new_x].character = character

    # def find_character(self, character):
    #     for y, row in enumerate(self.map):
    #         for x, cell in enumerate(row):
    #             if cell.character == character:
    #                 return x, y
    #     return None, None

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
                    print('.', end=' ')
            print()  # Перенос строки для новой строки карты
            




# Создание персонажей
self = Character(10, "Hero", "H", 5)
monster = Character(4,"Monster", "M", 7)

# Создание предметов
sword = Item("Sword", "S")
potion = Item("Potion", "P")

# Создание игровой карты
game_map = GameMap(10)

# Размещение персонажей и предметов на карте
# game_map.place_character(hero, 5, 5)
game_map.place_character(monster, 4, 4)
game_map.place_item(sword, 1, 3)
game_map.place_item(potion, 3, 1)

# Вывод карты в консоль
game_map.print_map()

# Добавление стен на карту
game_map.map[1][1].has_wall = True
game_map.map[3][3].has_wall = True

# Изменения в коде для передвижения персонажей с учётом стен
# game_map.move_character(hero, 0, 1)  # Перемещение героя вправо
# game_map.move_character(monster, 4, 3)  # Перемещение монстра вниз