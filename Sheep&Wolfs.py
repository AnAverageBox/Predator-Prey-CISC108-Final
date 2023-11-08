'''
Instructions: copy the text below into a comment at the top of your Python file.
Put an X into the [ ] boxes for each milestone you believe you have finished.

## Simulator Features
# Milestone 1
[X] Sheep exist
[X] Wolves exist
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
    wolves: list[DesignerObject]
    sheep_population: int
    wolf_population: int
    wolf_timer: int #for creating wolves
    sheep_timer: int #for creating sheep
    
def create_world() -> World:
    """Creates the World"""
    return World([create_sheep()], [create_wolf()], 1, 1, 0, 0)

def increase_timers(world: World):
    world.wolf_timer = world.wolf_timer + 1
    world.sheep_timer = world.sheep_timer + 1

def create_sheep() -> DesignerObject:
    """Creates sheep"""
    sheep = emoji('🐑')
    sheep.scale_x = 1
    sheep.scale_y = 1
    sheep.x = randint(0, get_width())
    sheep.y = randint(0, get_height())
    return sheep

def new_sheep_location(current_location: list[int]) -> list[int]:
    """generates a new coordinate that a sheep will move to"""
    left_right = randint(0, 1)#0 is left, 1 is right
    up_down = randint(0, 1)# 0 is down, 1 is up
    move_x = rand_int(0, 30)
    move_y = rand_int(0, 30)
    if left_right == 0:
        move_x = -move_x
    if up_down == 1:
        move_y = -move_y #y getting smaller actually is higher up on the screen
    return [current_location + move_x, current_location + move_y]

def move_sheep(world: World):
    pass

def make_sheep(world: World):
    """Creates sheep on a random part of the screen when conditions are met,
    uses create_sheep() function"""
    if world.sheep_timer / 50 >= 1:
        #every 50 updates another sheep will spawn on screen
        world.sheep.append(create_sheep())
        world.sheep_timer = 0
    
def grow_sheep_population(world: World):
    """increases the sheeps population make a counter that when the sheep_pop increases
    by 50(including the amount that may be subtracted), it adds anothersheep object on
    screen and the counter resets to 0 and repeats the process"""
    world.sheep_population += 1

def create_wolf() -> DesignerObject:
    """Creates wolfs at a random part of the screen"""
    wolf = emoji('🐺')
    wolf.scale_x = 1
    wolf.scale_x = 1
    wolf.x = randint(0, get_width())
    wolf.y = randint(0, get_height())
    return wolf

def new_wolf_location(current_location: list[int]) -> list[int]:
    """generates a new coordinate that a wolf will move to"""
    left_right = randint(0, 1) #0 for left 1 for right
    up_down = randint(0, 1)#0 for down 1 for up
    move_x = rand_int(0, 40)
    move_y = rand_int(0, 40)
    if left_right == 0:
        move_x = -move_x
    if up_down == 1:
        move_y = -move_y #y getting smaller actually is higher up on the screen
    return [current_location[0] + move_x, current_location[1] + move_y]

def move_wolf(world: World):
    """will move the wolf to the new coordinate"""
    pass

def make_wolves(world: World):
    """Creates wolf if conditions are met, calls create_wolf() function"""
    if world.wolf_timer / 150 >= 1:
        #every 150 updates a new wolf spawns on screen
        world.wolfs.append(create_wolf())
        world.wolf_timer = 0

def grow_wolf_population(world: World):
    """increases the wolf population make a counter that when the sheep_pop increases
    by 50 (including the amount that may be subtracted), it adds another sheep object
    on screen and the counter resets to 0 and repeats the process"""
    world.wolf_population += 1

when('starting', create_world)
when('updating', grow_sheep_population)
when('updating', increase_timers)
when('updating', make_wolves)
when('updating', make_sheep)

start()
