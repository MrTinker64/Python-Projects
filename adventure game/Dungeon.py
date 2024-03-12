from enum import Flag
import random

class Contents(Flag):
    Gold = 1, 2
    Weapon = 3
    Armor = 4
    Magic_Item = 5
    Potion = 6
    Trap = 7, 8
    Monster = 9, 10
    Natural_Hazard = 11, 12
    Empty = 13, 14, 15, 16
    

class Dungeon:
    DUNGEON = [
        [0], [0], [0], [0], [0],
        [0], [0], [0], [0], [0],
        [0], [0], [0], [0], [0],
        [0], [0], [0], [0], [0],
        [0], [0], [0], [0], [0]
    ]
    
    def __init__(self) -> None:
        self.create_dungeon
    
    def create_dungeon(self):
        for i in range(len(self.DUNGEON)):
            contents = random.choice(list(Contents))
            self.DUNGEON[i][0] = contents
            print(contents)
            
    def __repr__(self):
        return f"{self.DUNGEON}"
            
if __name__ == "__main__":
    print(Contents(4))
    # dungeon = Dungeon()
    # Dungeon.create_dungeon(dungeon)