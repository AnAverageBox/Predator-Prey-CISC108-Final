'''
link to milestone 1 demo: https://drive.google.com/file/d/1iQFsoh4K1TU5lLgh_2xIyjmcAowIe2Jl/view?usp=sharing

Instructions: copy the text below into a comment at the top of your Python file.
Put an X into the [ ] boxes for each milestone you believe you have finished.

## Simulator Features
# Milestone 1
[X] Sheep exist
[X] Wolves exist
[X] Animals move
[X] Animals live
[X] Animals die
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

WOLF_SPEED = 2
SHEEP_SPEED = 1


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
    world_timer: int #universal timer for both animals
    
def create_world() -> World:
    """Creates the World"""
    return World([create_sheep()], [create_wolf()], 1, 1, 0, 0, 0)

def increase_timers(world: World):
    world.wolf_timer = world.wolf_timer + 1
    world.sheep_timer = world.sheep_timer + 1
    world.world_timer += 1

def create_sheep() -> Sheep:
    """Creates sheep"""
    sheep_x = randint(0, get_width()-20)
    sheep_y = randint(0, get_height()-20)
    
    new_location = new_animal_location(sheep_x, sheep_y)
    new_x = new_location[0]
    new_y = new_location[1]
    
    sheep = Sheep(emoji('🐑', sheep_x, sheep_y), new_x, new_y, True)
    return sheep

def move_sheep(world: World):
    """will move sheep to the new location"""
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
            shep.emoji.x += SHEEP_SPEED * direction_x
        if shep.emoji.y != shep.new_y:
            shep.emoji.y += SHEEP_SPEED * direction_y
            
        make_new_location = shep.emoji.x == shep.new_x and shep.emoji.y == shep.new_y
        #once sheep's current location matches the new location, it makes another new one
        if make_new_location:
            new_location = new_animal_location(shep.emoji.x, shep.emoji.y)
            shep.new_x = new_location[0]
            shep.new_y = new_location[1]

def make_sheep(world: World):
    """Creates sheep on a random part of the screen when conditions are met,
    uses create_sheep() function"""
    if world.sheep_timer / 100 >= 1:
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
    
    new_location = new_animal_location(wolf_x, wolf_y)
    new_x = new_location[0]
    new_y = new_location[1]

    wolf = Wolf(emoji('🐺', wolf_x, wolf_y), new_x, new_y, True)
    return wolf

def move_wolves(world: World):
    """will move the wolf to the new coordinate"""
    for wolf in world.wolves:
        direction_x = 1
        direction_y = 1
        #variables above dictate what direction wolf needs to move in
        if wolf.emoji.x > wolf.new_x:
            direction_x = -1
        if wolf.emoji.y > wolf.new_y:
            direction_y = -1
            
        if abs(abs(wolf.emoji.x) - abs(wolf.new_x)) > 1:
            #if the new x coordinate current x coordinate or within 1 unit
            #of each other, it stops moving the wolf (this prevents wolf from vibrating)
            wolf.emoji.x += WOLF_SPEED * direction_x
        if abs(abs(wolf.emoji.y) - abs(wolf.new_y)) > 1:
            wolf.emoji.y += WOLF_SPEED * direction_y
            
        make_new_location = abs(abs(wolf.emoji.x) - abs(wolf.new_x)) <= 1 and abs(abs(wolf.emoji.y) - abs(wolf.new_y)) <= 1
        #once wolf's current location matches the new location, it makes another new one
        if make_new_location:
            new_location = new_animal_location(wolf.emoji.x, wolf.emoji.y)
            wolf.new_x = new_location[0]
            wolf.new_y = new_location[1]
            

def make_wolf(world: World):
    """Creates wolf if conditions are met, calls create_wolf() function"""
    if world.wolf_timer / 300 >= 1:
        #every 150 updates a new wolf spawns on screen
        world.wolves.append(create_wolf())
        world.wolf_timer = 0

def grow_wolf_population(world: World):
    """increases the wolf population make a counter that when the sheep_pop increases
    by 50 (including the amount that may be subtracted), it adds another sheep object
    on screen and the counter resets to 0 and repeats the process"""
    world.wolf_population += 1
    
def new_animal_location(x: int, y: int) -> list[int]:
    """takes coordinate x and y, and return new coordinate that is
    within 200 units of said coordinates
    
    Ex:
    (300,300) -> (500, 100)
    """
    left_right = randint(0, 1)#0 is left, 1 is right
    up_down = randint(0, 1)# 0 is down, 1 is up
    move_x = randint(0, 200)
    move_y = randint(0, 200)
    if left_right == 0:
        move_x = -move_x
    if up_down == 1:
        move_y = -move_y #y getting smaller actually is higher up on the screen
        
    #prevents going off screen
    new_x = x + move_x
    new_y = y + move_y
    if new_x < 0:
        new_x = 0
    elif new_x > get_width():
        new_x = get_width()
    
    if new_y < 0:
        new_y = 0
    elif new_y > get_height():
        new_y = get_height()
    return [new_x, new_y]

def animals_die(world: World):
    """each sheep and wolf dies after a certain amount of time"""
    if world.world_timer % 500 == 0:
        destroy(world.wolves[0].emoji)
        del world.wolves[0]#deletes oldest wolf in list of wolves
    if world.world_timer % 350 == 0:
        destroy(world.sheep[0].emoji)
        del world.sheep[0]#deletes oldest sheep in list of wolves
    

when('starting', create_world)
when('updating', grow_sheep_population)
when('updating', increase_timers)
when('updating', make_wolf)
when('updating', make_sheep)
when('updating', move_wolves)
when('updating', move_sheep)
when('updating', animals_die)

start()
