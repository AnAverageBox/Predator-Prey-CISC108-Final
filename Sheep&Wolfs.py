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
class Sheep:
    emoji: DesignerObject
    new_x: int
    new_y: int
    alive: bool

@dataclass
class Wolf:
    emoji: DesignerObject
    new_x: int
    new_y: int
    alive: bool

@dataclass
class World:
    sheep: list[Sheep]
    wolves: list[Wolf]
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

def create_sheep() -> Sheep:
    """Creates sheep"""
    sheep_x = randint(0, get_width()-20)
    sheep_y = randint(0, get_height()-20)
    
    sheep = Sheep(emoji('🐑', sheep_x, sheep_y), 0, 0, True)
    return sheep

def move_sheep(world: World):
    for shep in world.sheep:
        #singular and plural for sheep are the same
        direction_x = 1
        direction_y = 1
        #variables above dictate what direction sheep needs to move in
        if shep.emoji.x > shep.new_x:
            direction_x = -1
        if shep.emoji.y > shep.new_y:
            direction_y = -1
            
        if shep.emoji.x != shep.new_x:
            shep.emoji.x += 1 * direction_x
        if shep.emoji.y != shep.new_y:
            shep.emoji.y += 1 * direction_y

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

def create_wolf() -> Wolf:
    """Creates wolfs at a random part of the screen"""
    wolf_x = randint(0, get_width()-20)
    wolf_y = randint(0, get_height()-20)
    wolf = Wolf(emoji('🐺', wolf_x, wolf_y), 0, 0, True)
    return wolf

def move_wolf(world: World):
    """will move the wolf to the new coordinate"""
    for wolf in world.wolves:
        direction_x = 1
        direction_y = 1
        #variables above dictate what direction wolf needs to move in
        if wolf.emoji.x > wolf.new_x:
            direction_x = -1
        if wolf.emoji.y > wolf.new_y:
            direction_y = -1
            
        if wolf.emoji.x != wolf.new_x:
            wolf.emoji.x += 1 * direction_x
        if wolf.emoji.y != wolf.new_y:
            wolf.emoji.y += 1 * direction_y

def make_wolves(world: World):
    """Creates wolf if conditions are met, calls create_wolf() function"""
    if world.wolf_timer / 150 >= 1:
        #every 150 updates a new wolf spawns on screen
        world.wolves.append(create_wolf())
        world.wolf_timer = 0

def grow_wolf_population(world: World):
    """increases the wolf population make a counter that when the sheep_pop increases
    by 50 (including the amount that may be subtracted), it adds another sheep object
    on screen and the counter resets to 0 and repeats the process"""
    world.wolf_population += 1
    
def new_animal_location(animal: DesignerObject) -> list[int]:
    """generates a new coordinate that a the animal will move to"""
    left_right = randint(0, 1)#0 is left, 1 is right
    up_down = randint(0, 1)# 0 is down, 1 is up
    move_x = randint(0, 30)
    move_y = randint(0, 30)
    if left_right == 0:
        move_x = -move_x
    if up_down == 1:
        move_y = -move_y #y getting smaller actually is higher up on the screen
    return [animal.emoji.x + move_x, animal.emoji.y + move_y]

when('starting', create_world)
when('updating', grow_sheep_population)
when('updating', increase_timers)
when('updating', make_wolves)
when('updating', make_sheep)

start()
