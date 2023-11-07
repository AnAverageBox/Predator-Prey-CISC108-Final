'''
Instructions: copy the text below into a comment at the top of your Python file.
Put an X into the [ ] boxes for each milestone you believe you have finished.

## Simulator Features
# Milestone 1
[ ] Sheep exist
[ ] Wolves exist
[ ] Animals move
[ ] Animals live
[ ] Animals die
# Milestone 2
[ ] Smooth movement
[ ] Wolves eat
[ ] Animals reproduce
# Milestone 3
[ ] Grass exists
[ ] Grass lives
[ ] Sheep eat
[ ] Grass grows
[ ] Green grass
[ ] Show stats
# Extra Credit
[ ] Stable Settings
[ ] Fancy Stats
[ ] Plot Stats
[ ] Control Panel
[ ] Hunters
[ ] Evolution
'''
from designer import *
from random import randint
from dataclasses import dataclass

@dataclass
class World:
    sheep: list[DesignerObject]
    wolfs: list[DesignerObject]
    sheep_population: int
    wolf_population: int
    wolf_timer: int #for creating wolves
    sheep_timer: int #for creating sheep
    
def create_world() -> World:
    """Creates the World"""
    return World([], [], 1, 1, 0, 0)

def create_sheep() -> DesignerObject:
    """Creates sheep"""
    sheep = emoji('🐑')
    sheep.scale_x = 1
    sheep.scale_y = 1
    sheep.x = rand_int(0, get_width())
    sheep.y = rand_int(0, get_heigth())
    return sheep

def make_sheep(world: World):
    """Creates sheep on a random part of the screen when conditions are met,
    uses create_sheep() function"""
    
    
def grow_sheep_population():
    """increases the sheeps population
    make a coutner that when the sheep_pop increases by 50 (including the amount that may be subtracted), it adds another
    sheep object on screen and the counter resets to 0 and repeats the process"""
    
    world.sheep_population += 1

def create_wolf() -> DesignerObject:
    """Creates wolfs at a random part of the screen"""
    wolf = emoji('🐺')
    wolf.scale_x = 1
    wolf.scale_x = 1
    wolf.x = rand_int(0, get_width())
    wolf.y = rand_int(0, get_height())
    return wolf

def make_wolves(world: World):
    """Creates wolf if conditions are met, calls create_wolf() function"""
    


when('starting', create_world)
when('updating', grow_sheep_population)

start()
