'''
link to milestone 1 demo: https://drive.google.com/file/d/1iQFsoh4K1TU5lLgh_2xIyjmcAowIe2Jl/view?usp=sharing

link to milestone 2 demo: https://drive.google.com/file/d/1u96U_DzSRpxA95U6sS-xi7c0vwGMWgcO/view?usp=sharing

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
[X] Smooth movement
[X] Wolves eat
[X] Animals reproduce
# Milestone 3
[X] Grass exists
[X] Grass lives
[X] Sheep eat
[X] Grass grows
[X] Green grass
[X] Show stats
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

#screen width: 800
#screen height: 600
WOLF_SPEED = 2
SHEEP_SPEED = 1

#List of the grass squares to be used on screen
GRASS_ROW1 = [rectangle('green',get_width()/4, get_height()/3, 100, 100),
                rectangle('green',get_width()/4, get_height()/3, 300, 100),
                rectangle('green',get_width()/4, get_height()/3, 500, 100),
                rectangle('green',get_width()/4, get_height()/3, 700, 100)]

GRASS_ROW2 = [rectangle('green',get_width()/4, get_height()/3, 100, 300),
                rectangle('green',get_width()/4, get_height()/3, 300, 300),
                rectangle('green',get_width()/4, get_height()/3, 500, 300),
                rectangle('green',get_width()/4, get_height()/3, 700, 300)]

GRASS_ROW3 = [rectangle('green',get_width()/4, get_height()/3, 100, 500),
                rectangle('green',get_width()/4, get_height()/3, 300, 500),
                rectangle('green',get_width()/4, get_height()/3, 500, 500),
                rectangle('green',get_width()/4, get_height()/3, 700, 500)]

GRASS_RECTANGLES = [GRASS_ROW1, GRASS_ROW2, GRASS_ROW3] #2D array/list

GRASS_GROWTH_TIMERS = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]#for grass growing after being eaten

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
#Note for grader, I only used del because Wolf and Sheep were separate
#dataclasses from a DesignerObject, I was running into some bugs when I didn't

@dataclass
class World:
    grass_squares_grid: list[[DesignerObject]]#the grass on screen
    grass_growth_timers: list[[int]]#timer for each grass square to grow back
    
    
    sheep: list[Sheep]
    wolves: list[Wolf]
    
    sheep_population: float #WILL BE MADE INTO INTEGER WHEN ON SCREEN
    wolf_population: float #WILL BE MADE INTO INTEGER WHEN ON SCREEN
    
    sheep_timer: int #for creating wolves
    wolf_timer: int #for creating sheep
    world_timer: int #universal timer for both animals
    
    sheep_population_counter: DesignerObject
    wolf_population_counter: DesignerObject
    
    #population can affect on-screen animals
    sheep_population_spawn: float #population can affect on-screen animals
    wolf_population_spawn: float
    
def create_world() -> World:
    """Creates the World"""
    return World(GRASS_RECTANGLES,GRASS_GROWTH_TIMERS,
                [create_sheep(),create_sheep()],[create_wolf(),create_wolf()],
                 800, 400,
                 0, 0, 0,
                 text("black", 'Wolf population: ' + str(500), 25, 200, 130),
                 text("black", 'Sheep population: ' + str(1000), 25, 200, 170),
                 1000,500,)
    #using the other way to make dataclass instance

def increase_timers(world: World):
    """increases timers in the world dataclass"""
    world.wolf_timer = world.wolf_timer + 1
    world.sheep_timer = world.sheep_timer + 1
    world.world_timer += 1
    
    
    row = 0
    for time_row in world.grass_growth_timers:
        row +=1
        #grass will grow back after 1000 updates
        if time_row[0] > 0 and time_row[0] < 1000:
            time_row[0] += 1
        else:
            time_row[0] = 0
            world.grass_squares_grid[row-1][0].color = 'green'
        
        if time_row[1] > 0 and time_row[0] < 1000:
            time_row[1] += 1
        else:
            time_row[1] = 0
            world.grass_squares_grid[row-1][1].color = 'green'
        
        if time_row[2] > 0 and time_row[0] < 1000:
            time_row[2] += 1
        else:
            time_row[2] = 0
            world.grass_squares_grid[row-1][2].color = 'green'
        
        if time_row[3] > 0 and time_row[0] < 1000:
            time_row[3] += 1
        else:
            time_row[3] = 0
            world.grass_squares_grid[row-1][3].color = 'green'
      
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
        #once sheep's current location matches the new location, it makes gives it another one
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
    """will move the wolves to the new locations"""
    for wolf in world.wolves:
        direction_x = 1
        direction_y = 1
        #variables above dictate what direction wolf needs to move in
        if wolf.emoji.x > wolf.new_x:
            direction_x = -1
        if wolf.emoji.y > wolf.new_y:
            direction_y = -1
            
        x_close_enough = close_enough_to(wolf.emoji.x, wolf.new_x)
        y_close_enough = close_enough_to(wolf.emoji.y, wolf.new_y)
        if not x_close_enough: 
            wolf.emoji.x += WOLF_SPEED * direction_x
        
        if not y_close_enough:
            wolf.emoji.y += WOLF_SPEED * direction_y
        
        if x_close_enough and y_close_enough:
            #new location on screen is assigned
            new_location = new_animal_location(wolf.emoji.x, wolf.emoji.y)
            wolf.new_x = new_location[0]
            wolf.new_y = new_location[1]
            
def close_enough_to(current_value: int, new_value) -> bool:
    """returns whether value (usually x or y coordinate) is close enough to new 
    location/coordinates as a boolean (in this case if it's within 1 unit/pixel)"""
    if abs(abs(current_value) - abs(new_value)) <= 1:
        return True
    else:
        return False

def make_wolf(world: World):
    """Creates wolf if conditions are met, calls create_wolf() function"""
    if world.wolf_timer / 300 >= 1:
        #every 150 updates a new wolf spawns on screen
        world.wolves.append(create_wolf())
        world.wolf_timer = 0
        
def wolf_eats_sheep(world:World):
    destroyed_sheep = []
    for wolf in world.wolves:
        for shep in world.sheep:
            if colliding(wolf.emoji, shep.emoji):
                destroyed_sheep.append(shep)
                
    if len(destroyed_sheep) > 0:
        world.sheep_population -= 200
        world.wolf_population += 300
    world.sheep = filter_from_sheep(world.sheep, destroyed_sheep, world)
    
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
    """each sheep and wolf dies after a certain amount of time (likely to get changed after adding population)"""
    if world.world_timer % 600 == 0:
        destroy(world.wolves[0].emoji)
        del world.wolves[0]#deletes oldest wolf in list of wolves
        world.wolf_population -= 200
    if world.world_timer % 350 == 0:
        destroy(world.sheep[0].emoji)
        del world.sheep[0]#deletes oldest sheep in list of wolves
        world.sheep_population -= 400
        
def wolves_starve(world: World):
    if world.wolf_population < 1000:
        world.wolf_population -= .3
    if world.wolf_population > 1000 and world.wolf_population < 2000:
        world.wolf_population -= .9
    if world.wolf_population >= 2000:
        world.wolf_population -= 1.5
        
        
def animals_reproduce(world: World):
    """animals' populations goes up and down, dependeing on the number of
    emojis that exist on screen"""
    num_of_wolves = len(world.wolves)#can be done with for loop
    num_of_sheep = len(world.sheep)#can be done with for loop
    
    current_wolf_population = world.wolf_population
    current_sheep_population = world.sheep_population
    
    sheep_born = current_sheep_population * 0.0005
    world.sheep_population = sheep_born + current_sheep_population
    #five hundredths of a percent
    
    wolves_born = current_wolf_population * 0.0003
    world.wolf_population = wolves_born + current_wolf_population
    #three hundreths of a percent per update
    
def update_population_text(world:World):
    """Updates the population text on screen to be match the population"""
    updated_sheep_text = 'Sheep population: ' + str(int(world.sheep_population))
    world.sheep_population_counter.text = updated_sheep_text
    
    updated_wolf_text = 'Wolf population: ' + str(int(world.wolf_population))
    world.wolf_population_counter.text = updated_wolf_text   
            
def filter_from_sheep(old_list: list[Sheep], elements_to_not_keep: list[Sheep]) -> list[Sheep]:
    """filters out sheep that have been 'killed' by the wolf and deletes them from the world"""
    sheep_left = []
    for sheep in old_list:
        if sheep in elements_to_not_keep:
            destroy(sheep.emoji)
            del sheep
        else:
            sheep_left.append(sheep)
    return sheep_left

def population_increase_animals(world: World):
    """adds or removes sheep/wolves from the screen depending on how much their
    population goes up or down"""
    destroyed_sheep = []
    if world.sheep_population - world.sheep_population_spawn >= 400:
        world.sheep.append(create_sheep())
        world.sheep_population_spawn = world.sheep_population
    elif world.sheep_population - world.sheep_population_spawn <= -400:
        destroyed_sheep.append(world.sheep[0])
        world.sheep_population_spawn = world.sheep_population
        
    world.sheep = filter_from_sheep(world.sheep, destroyed_sheep, world)
    destroyed_sheep = []
    
    destroyed_wolves = []
    if world.wolf_population - world.wolf_population_spawn >= 200:
        world.wolves.append(create_wolf())
        world.wolf_population_spawn = world.wolf_population
    elif world.wolf_population - world.wolf_population_spawn <= -200:
        print(world.wolves)
        destroyed_wolves.append(world.wolves[0])
        world.wolf_population_spawn = world.wolf_population
        
    world.wolves = filter_from_wolves(world.wolves, destroyed_wolves, world)
    destroyed_wolves = []
    
def filter_from_wolves(old_list: list[Wolf], elements_to_not_keep: list[Wolf], world: World) -> list[Wolf]:
    """deletes wolves from list of wolves that have died"""
    wolves_left = []
    for wolf in old_list:
        if wolf in elements_to_not_keep:
            destroy(wolf.emoji)
            del wolf
            world.wolf_population -= 200
        else:
            wolves_left.append(wolf)
    return wolves_left

def filter_from_sheep(old_list: list[Sheep], elements_to_not_keep: list[Sheep], world: World) -> list[Sheep]:
    """filters out sheep that have been 'killed' by the wolf and deletes them from the world"""
    sheep_left = []
    for sheep in old_list:
        if sheep in elements_to_not_keep:
            destroy(sheep.emoji)
            del sheep
            world.sheep_population - 400
        else:
            sheep_left.append(sheep)
    return sheep_left
    
def grass_dies(world: World):
    """When a sheep touches green grass, it 'eats' the grass
    and the grass turn brown for a period of time"""
    grass_timers_grid = world.grass_growth_timers
    start_timer_x = 0
    start_timer_y = 0
    
    for shep in world.sheep:
        start_timer_x = 0
        for grass_square_row in world.grass_squares_grid:
            start_timer_x += 1
            start_timer_y = 0
            for grass_square in grass_square_row:
                start_timer_y += 1
                if grass_square.color == 'green' and colliding(grass_square, shep.emoji):
                    grass_square.color = 'saddlebrown'
                    grass_timers_grid[start_timer_x-1][start_timer_y-1] += 1
                    if grass_timers_grid[start_timer_x-1][start_timer_y-1] == 1:
                        world.sheep_population += 100

def grass_grows(world: World):
    """Grass grows back after being 'eating'"""
    

def simulation_over(world: World): #THIS WILL BE THE LAST FUNCTION
    if world.wolf_population <= 0:
        pass
    if world.sheep_population <= 0:
        pass


#100 updates is around 6 seconds
when('starting', create_world)
when('updating', increase_timers)
when('updating', make_wolf)
when('updating', make_sheep)
when('updating', move_wolves)
when('updating', move_sheep)
when('updating', animals_die)
when('updating', animals_reproduce)
when('updating', wolves_starve)
when('updating', update_population_text)
when('updating', wolf_eats_sheep)
when('updating', population_increase_animals)
when('updating', grass_dies)
#there's a bug here, if you put 'updatin' it doesn't give an error

start()

