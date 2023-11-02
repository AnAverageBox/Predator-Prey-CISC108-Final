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
    sheep_pop: int
    wolf_pop: int
    timer: int
    
def create_world() -> World:
    """Creates the World"""
    return World(create_sheep(), create_wolf(), 1, 1)

def create_sheep() -> DesignerObject:
    """Creates sheep"""
    sheep = emoji('🐑')
    
    
def grow_sheep_population():
    """increases the sheeps population
    make a coutner that when the sheep_pop increases by 50 (including the amount that may be subtracted), it adds another
    sheep object on screen and the counter resets to 0 and repeats the process"""
    
    world.sheep_pop += 1

def create_wolf() -> designerObject:
    """Creates wolfs"""
    wolf = emoji('🐺')


when('starting', create_world())
when('updating', )

start()

