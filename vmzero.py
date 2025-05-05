import pgzrun, pygame, random, os

os.environ ['SDL_VIDEO_CENTERED'] = '1'

TITLE = "Veltramon Zero"
ICON = "vmzero.ico"

WIDTH = 800
HEIGHT = 600

center_x = float (WIDTH / 2)
center_y = float (HEIGHT / 2)

frame_left = int (60)
frame_right = int (WIDTH - 60)
frame_top = int (-30)
frame_bottom = int (HEIGHT + 60)

player_position = int (HEIGHT - 100)

hud_top_y = int (50)
hud_bottom_y = int (HEIGHT - 50)
hud_size = int (17)

ship = ["player_ship1", "player_ship2", "player_explosion_1", "player_explosion_2", "player_explosion_3", "player_explosion_4", "player_explosion_5", "player_explosion_6", "player_explosion_7", "player_explosion_8", "player_explosion_9", "player_explosion_10", "player_explosion_11"]

player = Actor (ship [0])
player.x = center_x
player.y = frame_bottom
player.spawned = False
player.frame = 0
player.delay = 0
player.health = 100
player.died = False
player.lives = 5
score = 0

game_paused = False

transition_one = Actor ("transition_0")
transition_one.x = center_x
transition_one.y = int (HEIGHT + 300)
transition_two = Actor ("transition_1")
transition_two.x = center_x
transition_two.y = center_y
transition_three = Actor ("transition_2")
transition_three.x = center_x
transition_three.y = int (HEIGHT + 300)

transition_step = 3

black_enemies = []
blue_enemies = []
green_enemies = []
red_enemies = []

enemies_defeated = 0
enemies_required = 1
current_level = 0
level_completed = False
new_level = True
level_countdown = 100
level_timer = 0
level_timer_delay = 0
time_limit = 30

enemy_black = ["enemy_black1", "enemy_black2", "enemy_explosion_1", "enemy_explosion_2", "enemy_explosion_3", "enemy_explosion_4", "enemy_explosion_5", "enemy_explosion_6", "enemy_explosion_7", "enemy_explosion_8", "enemy_explosion_9", "enemy_explosion_10"]
enemy_blue = ["enemy_blue1", "enemy_blue2", "enemy_explosion_1", "enemy_explosion_2", "enemy_explosion_3", "enemy_explosion_4", "enemy_explosion_5", "enemy_explosion_6", "enemy_explosion_7", "enemy_explosion_8", "enemy_explosion_9", "enemy_explosion_10"]
enemy_green = ["enemy_green1", "enemy_green2", "enemy_explosion_1", "enemy_explosion_2", "enemy_explosion_3", "enemy_explosion_4", "enemy_explosion_5", "enemy_explosion_6", "enemy_explosion_7", "enemy_explosion_8", "enemy_explosion_9", "enemy_explosion_10"]
enemy_red = ["enemy_red1", "enemy_red2", "enemy_explosion_1", "enemy_explosion_2", "enemy_explosion_3", "enemy_explosion_4", "enemy_explosion_5", "enemy_explosion_6", "enemy_explosion_7", "enemy_explosion_8", "enemy_explosion_9", "enemy_explosion_10"]

stars = ['1', '2', '3', '4', '5', '6']

planets = ['planet00', 'planet01', 'planet02', 'planet03', 'planet04', 'planet05', 'planet06', 'planet07', 'planet08', 'planet09']

planet = Actor (random.choice (planets))
planet.x = random.randint (frame_left, frame_right)
planet.y = -center_y

next_planet = ""

player_blue_lasers = ["laser_blue", "laser_blue_hit"]
player_lasers = []
player_laser_delay = 0

enemy_red_lasers = ["laser_red", "laser_red_hit"]

black_enemy_lasers = []

blue_enemy_lasers = []

green_enemy_lasers = []

red_enemy_lasers = []

background = Actor (stars [0])
background_next = Actor (stars [0])

background.x = center_x
background.y = center_y

background_next.x = center_x
background_next.y = (background.y - 600)

background.frame = 0
background.delay = 0

def on_key_down (key):
    global game_paused

    if (key == keys.P) and (game_paused == True):
        game_paused = False
    elif (key == keys.P) and (game_paused == False):
        game_paused = True


def update ():
    global enemies_defeated, enemies_required, level_completed, current_level, score, new_level, transition_step, level_countdown, level_timer, level_timer_delay, time_limit, player_laser_delay
    
    if (current_level == 0) or (current_level == 5):
        if keyboard.space:
            new_level = True
            
    if game_paused == False:        
        if player.spawned == True:
            level_timer_delay += 1

            if level_timer_delay == 60:
                level_timer -= 1
                level_timer_delay = 0
                if level_timer == 0:
                    player.health = 0

        if current_level <= 0:
            background.y += 1
            background_next.y += 1
            planet.y += 0.5
            time_limit = 30
            enemies_required = 1
        elif current_level == 1:
            background.y += 1
            background_next.y += 1
            planet.y += 0.5
            time_limit = 30
            enemies_required = 10
        elif current_level == 2:
            background.y += 2
            background_next.y += 2
            planet.y += 1
            time_limit = 40
            enemies_required = 15
        elif current_level == 3:
            background.y += 3
            background_next.y += 3
            planet.y += 1.5
            time_limit = 50
            enemies_required = 20
        elif current_level == 4:
            background.y += 4
            background_next.y += 4
            planet.y += 2
            time_limit = 60
            enemies_required = 25
        elif current_level > 4:
            background.y += 4
            background_next.y += 4
            planet.y += 2
            time_limit = 30
            enemies_required = 1

        if enemies_defeated == enemies_required:
            level_completed = True

        background.delay += 1

        if background.delay == 5:
            background.frame += 1
            background.delay = 0
            
        if background.frame == 1:
            background.image = stars [1]
            background_next.image = stars [1]
        elif background.frame == 2:
            background.image = stars [2]
            background_next.image = stars [2]
        elif background.frame == 3:
            background.image = stars [3]
            background_next.image = stars [3]
        elif background.frame == 4:
            background.image = stars [4]
            background_next.image = stars [4]
        elif background.frame == 5:
            background.image = stars [5]
            background_next.image = stars [5]
        elif background.frame == 6:
            background.frame = 0
            background.image = stars [0]
            background_next.image = stars [0]

        player.delay += 1

        if player.delay == 2:
            player.frame += 1
            player.delay = 0
            
        if player.health > 0:
            if player.frame == 1:
                player.image = ship [1]
            elif player.frame == 2:
                player.frame = 0
                player.image = ship [0]
        elif player.health <= 0:
            player.died = True
            player.spawned = False
            if (player.frame == 1) or (player.frame == 2):
                player.image = ship [2]
            elif player.frame == 3:
                player.image = ship [3]
            elif player.frame == 4:
                player.image = ship [4]
            elif player.frame == 5:
                player.image = ship [5]
            elif player.frame == 6:
                player.image = ship [6]
            elif player.frame == 7:
                player.image = ship [7]
            elif player.frame == 8:
                player.image = ship [8]
            elif player.frame == 9:
                player.image = ship [9]
            elif player.frame == 10:
                player.image = ship [10]
            elif player.frame == 11:
                player.image = ship [11]
            elif player.frame == 12:
                player.image = ship [12]
            elif player.frame == 13:
                new_level = True

        if player.health > 100:
            player.health = 100
                
        if (keyboard.left) and (player.spawned == True):
            player.x -= 5
        if (keyboard.right) and (player.spawned == True):
            player.x += 5

        if player.x < frame_left:
            player.x = frame_left
        if player.x > frame_right:
            player.x = frame_right
        
        if (player.spawned == False) and (level_completed == False) and (new_level == False) and (current_level > 0) and (current_level < 5):
            if player.y > player_position:
                player.y -= 2
            else:
                player.spawned = True
                player.y = player_position

        if (keyboard.space or keyboard.up) and (player_laser_delay == 0) and (player.spawned == True):
            player_laser = Actor (player_blue_lasers [0])
            player_laser.x = player.x
            player_laser.y = player.y - 40
            player_laser.hit = False
            player_laser.hit_delay = 0
            player_lasers.append (player_laser)

        player_laser_delay += 1

        if player_laser_delay == 8:
            player_laser_delay = 0

        for player_laser in player_lasers:
            
            for black_enemy in black_enemies:
                if (black_enemy.colliderect (player_laser) == True) and (black_enemy.health > 0):
                    player_laser.image = player_blue_lasers [1]
                    player_laser.y = (black_enemy.y + 50)
                    player_laser.hit_delay += 1
                    if player_laser.hit_delay == 4:
                        player_laser.hit = True
                        black_enemy.health -= 1
                        if black_enemy.health <= 0:
                            enemies_defeated += 1
                            score += 100

            for blue_enemy in blue_enemies:
                if (blue_enemy.colliderect (player_laser) == True) and (blue_enemy.health > 0):
                    player_laser.image = player_blue_lasers [1]
                    player_laser.y = (blue_enemy.y + 50)
                    player_laser.hit_delay += 1
                    if player_laser.hit_delay == 4:
                        player_laser.hit = True
                        blue_enemy.health -= 1
                        if blue_enemy.health <= 0:
                            enemies_defeated += 1
                            score += 100

            for green_enemy in green_enemies:
                if (green_enemy.colliderect (player_laser) == True) and (green_enemy.health > 0):
                    player_laser.image = player_blue_lasers [1]
                    player_laser.y = (green_enemy.y + 50)
                    player_laser.hit_delay += 1
                    if player_laser.hit_delay == 4:
                        player_laser.hit = True
                        green_enemy.health -= 1
                        if green_enemy.health <= 0:
                            enemies_defeated += 1
                            score += 100

            for red_enemy in red_enemies:
                if (red_enemy.colliderect (player_laser) == True) and (red_enemy.health > 0):
                    player_laser.image = player_blue_lasers [1]
                    player_laser.y = (red_enemy.y + 50)
                    player_laser.hit_delay += 1
                    if player_laser.hit_delay == 4:
                        player_laser.hit = True
                        red_enemy.health -= 1
                        if red_enemy.health <= 0:
                            enemies_defeated += 1
                            score += 100
                            player.health += 20
                        
            player_laser.y -= 15

            if (player_laser.y < frame_top) or (player_laser.hit == True):
                player_lasers.remove (player_laser)
                
        for black_enemy in black_enemies:
            if (random.randint (0, 100) > 99) and (player.spawned == True):
                black_enemy_laser = Actor (enemy_red_lasers [0])
                black_enemy_laser.x = black_enemy.x
                black_enemy_laser.y = black_enemy.y + 40
                black_enemy_laser.hit = False
                black_enemy_laser.hit_delay = 0
                black_enemy_lasers.append (black_enemy_laser)

            black_enemy.delay += 1

            if black_enemy.delay == 2:
                black_enemy.frame += 1
                black_enemy.delay = 0
            
            if black_enemy.health > 0:
                if black_enemy.frame == 1:
                    black_enemy.image = enemy_black [1]
                elif black_enemy.frame == 2:
                    black_enemy.frame = 0
                    black_enemy.image = enemy_black [0]
            elif black_enemy.health <= 0:
                if (black_enemy.frame == 1) or (black_enemy.frame == 2):
                    black_enemy.image = enemy_black [2]
                elif black_enemy.frame == 3:
                    black_enemy.image = enemy_black [3]
                elif black_enemy.frame == 4:
                    black_enemy.image = enemy_black [4]
                elif black_enemy.frame == 5:
                    black_enemy.image = enemy_black [5]
                elif black_enemy.frame == 6:
                    black_enemy.image = enemy_black [6]
                elif black_enemy.frame == 7:
                    black_enemy.image = enemy_black [7]
                elif black_enemy.frame == 8:
                    black_enemy.image = enemy_black [8]
                elif black_enemy.frame == 9:
                    black_enemy.image = enemy_black [9]
                elif black_enemy.frame == 10:
                    black_enemy.image = enemy_black [10]
                elif black_enemy.frame == 11:
                    black_enemy.image = enemy_black [11]
                
            black_enemy.y += 1.5
                
            if (black_enemy.y > frame_bottom) or (black_enemy.frame == 12):
                black_enemies.remove (black_enemy)

        for blue_enemy in blue_enemies:
            if (random.randint (0, 100) > 98) and (player.spawned == True):
                blue_enemy_laser = Actor (enemy_red_lasers [0])
                blue_enemy_laser.x = blue_enemy.x
                blue_enemy_laser.y = blue_enemy.y + 40
                blue_enemy_laser.hit = False
                blue_enemy_laser.hit_delay = 0
                blue_enemy_lasers.append (blue_enemy_laser)

            blue_enemy.delay += 1

            if blue_enemy.delay == 2:
                blue_enemy.frame += 1
                blue_enemy.delay = 0
            
            if blue_enemy.health > 0:
                if blue_enemy.frame == 1:
                    blue_enemy.image = enemy_blue [1]
                elif blue_enemy.frame == 2:
                    blue_enemy.frame = 0
                    blue_enemy.image = enemy_blue [0]
            elif blue_enemy.health <= 0:
                if (blue_enemy.frame == 1) or (blue_enemy.frame == 2):
                    blue_enemy.image = enemy_blue [2]
                elif blue_enemy.frame == 3:
                    blue_enemy.image = enemy_blue [3]
                elif blue_enemy.frame == 4:
                    blue_enemy.image = enemy_blue [4]
                elif blue_enemy.frame == 5:
                    blue_enemy.image = enemy_blue [5]
                elif blue_enemy.frame == 6:
                    blue_enemy.image = enemy_blue [6]
                elif blue_enemy.frame == 7:
                    blue_enemy.image = enemy_blue [7]
                elif blue_enemy.frame == 8:
                    blue_enemy.image = enemy_blue [8]
                elif blue_enemy.frame == 9:
                    blue_enemy.image = enemy_blue [9]
                elif blue_enemy.frame == 10:
                    blue_enemy.image = enemy_blue [10]
                elif blue_enemy.frame == 11:
                    blue_enemy.image = enemy_blue [11]
                
            blue_enemy.y += 1.5
            if (blue_enemy.y > frame_bottom) or (blue_enemy.frame == 12):
                blue_enemies.remove (blue_enemy)

        for green_enemy in green_enemies:
            if (random.randint (0, 100) > 97) and (player.spawned == True):
                green_enemy_laser = Actor (enemy_red_lasers [0])
                green_enemy_laser.x = green_enemy.x
                green_enemy_laser.y = green_enemy.y + 40
                green_enemy_laser.hit = False
                green_enemy_laser.hit_delay = 0
                green_enemy_lasers.append (green_enemy_laser)

            green_enemy.delay += 1

            if green_enemy.delay == 2:
                green_enemy.frame += 1
                green_enemy.delay = 0
            
            if green_enemy.health > 0:
                if green_enemy.frame == 1:
                    green_enemy.image = enemy_green [1]
                elif green_enemy.frame == 2:
                    green_enemy.frame = 0
                    green_enemy.image = enemy_green [0]
            elif green_enemy.health <= 0:
                if (green_enemy.frame == 1) or (green_enemy.frame == 2):
                    green_enemy.image = enemy_green [2]
                elif green_enemy.frame == 3:
                    green_enemy.image = enemy_green [3]
                elif green_enemy.frame == 4:
                    green_enemy.image = enemy_green [4]
                elif green_enemy.frame == 5:
                    green_enemy.image = enemy_green [5]
                elif green_enemy.frame == 6:
                    green_enemy.image = enemy_green [6]
                elif green_enemy.frame == 7:
                    green_enemy.image = enemy_green [7]
                elif green_enemy.frame == 8:
                    green_enemy.image = enemy_green [8]
                elif green_enemy.frame == 9:
                    green_enemy.image = enemy_green [9]
                elif green_enemy.frame == 10:
                    green_enemy.image = enemy_green [10]
                elif green_enemy.frame == 11:
                    green_enemy.image = enemy_green [11]
                
            green_enemy.y += 1.5
            if (green_enemy.y > frame_bottom) or (green_enemy.frame == 12):
                green_enemies.remove (green_enemy)

        for red_enemy in red_enemies:
            if (random.randint (0, 100) > 96) and (player.spawned == True):
                red_enemy_laser = Actor (enemy_red_lasers [0])
                red_enemy_laser.x = red_enemy.x
                red_enemy_laser.y = red_enemy.y + 40
                red_enemy_laser.hit = False
                red_enemy_laser.hit_delay = 0
                red_enemy_lasers.append (red_enemy_laser)

            red_enemy.delay += 1

            if red_enemy.delay == 2:
                red_enemy.frame += 1
                red_enemy.delay = 0
            
            if red_enemy.health > 0:
                if red_enemy.frame == 1:
                    red_enemy.image = enemy_red [1]
                elif red_enemy.frame == 2:
                    red_enemy.frame = 0
                    red_enemy.image = enemy_red [0]
            elif red_enemy.health <= 0:
                if (red_enemy.frame == 1) or (red_enemy.frame == 2):
                    red_enemy.image = enemy_red [2]
                elif red_enemy.frame == 3:
                    red_enemy.image = enemy_red [3]
                elif red_enemy.frame == 4:
                    red_enemy.image = enemy_red [4]
                elif red_enemy.frame == 5:
                    red_enemy.image = enemy_red [5]
                elif red_enemy.frame == 6:
                    red_enemy.image = enemy_red [6]
                elif red_enemy.frame == 7:
                    red_enemy.image = enemy_red [7]
                elif red_enemy.frame == 8:
                    red_enemy.image = enemy_red [8]
                elif red_enemy.frame == 9:
                    red_enemy.image = enemy_red [9]
                elif red_enemy.frame == 10:
                    red_enemy.image = enemy_red [10]
                elif red_enemy.frame == 11:
                    red_enemy.image = enemy_red [11]
                
            red_enemy.y += 1.5
            if (red_enemy.y > frame_bottom) or (red_enemy.frame == 12):
                red_enemies.remove (red_enemy)

        for black_enemy_laser in black_enemy_lasers:

            black_enemy_laser.y += 15

            if (player.colliderect (black_enemy_laser) == True) and (player.health > 0):
                    black_enemy_laser.image = enemy_red_lasers [1]
                    black_enemy_laser.y = (player.y - 20)
                    black_enemy_laser.hit_delay += 1
                    if black_enemy_laser.hit_delay == 4:
                        black_enemy_laser.hit = True
                        player.health -= 1

            if (black_enemy_laser.y > frame_bottom) or (black_enemy_laser.hit == True):
                black_enemy_lasers.remove (black_enemy_laser)

        for blue_enemy_laser in blue_enemy_lasers:

            blue_enemy_laser.y += 15

            if (player.colliderect (blue_enemy_laser) == True) and (player.health > 0):
                    blue_enemy_laser.image = enemy_red_lasers [1]
                    blue_enemy_laser.y = (player.y - 20)
                    blue_enemy_laser.hit_delay += 1
                    if blue_enemy_laser.hit_delay == 4:
                        blue_enemy_laser.hit = True
                        player.health -= 1

            if (blue_enemy_laser.y > frame_bottom) or (blue_enemy_laser.hit == True):
                blue_enemy_lasers.remove (blue_enemy_laser)

        for green_enemy_laser in green_enemy_lasers:

            green_enemy_laser.y += 15

            if (player.colliderect (green_enemy_laser) == True) and (player.health > 0):
                    green_enemy_laser.image = enemy_red_lasers [1]
                    green_enemy_laser.y = (player.y - 20)
                    green_enemy_laser.hit_delay += 1
                    if green_enemy_laser.hit_delay == 4:
                        green_enemy_laser.hit = True
                        player.health -= 1

            if (green_enemy_laser.y > frame_bottom) or (green_enemy_laser.hit == True):
                green_enemy_lasers.remove (green_enemy_laser)

        for red_enemy_laser in red_enemy_lasers:

            red_enemy_laser.y += 15

            if (player.colliderect (red_enemy_laser) == True) and (player.health > 0):
                    red_enemy_laser.image = enemy_red_lasers [1]
                    red_enemy_laser.y = (player.y - 20)
                    red_enemy_laser.hit_delay += 1
                    if red_enemy_laser.hit_delay == 4:
                        red_enemy_laser.hit = True
                        player.health -= 1

            if (red_enemy_laser.y > frame_bottom) or (red_enemy_laser.hit == True):
                red_enemy_lasers.remove (red_enemy_laser)

        if (random.randint (0, 1000) > 980) and (player.spawned == True):
            if random.randint (0, 3) == 0:
                blue_enemy = Actor (enemy_blue [0])
                blue_enemy.y = frame_top
                blue_enemy.x = random.randint (frame_left, frame_right)
                blue_enemy.health = 3
                blue_enemy.frame = 0
                blue_enemy.delay = 0
                blue_enemies.append (blue_enemy)
            elif random.randint (0, 3) == 1:
                black_enemy = Actor (enemy_black [0])
                black_enemy.y = frame_top
                black_enemy.x = random.randint (frame_left, frame_right)
                black_enemy.health = 3
                black_enemy.frame = 0
                black_enemy.delay = 0
                black_enemies.append (black_enemy)
            elif random.randint (0, 3) == 2:
                green_enemy = Actor (enemy_green [0])
                green_enemy.y = frame_top
                green_enemy.x = random.randint (frame_left, frame_right)
                green_enemy.health = 3
                green_enemy.frame = 0
                green_enemy.delay = 0
                green_enemies.append (green_enemy)
            elif random.randint (0, 3) == 3:
                red_enemy = Actor (enemy_red [0])
                red_enemy.y = frame_top
                red_enemy.x = random.randint (frame_left, frame_right)
                red_enemy.health = 3
                red_enemy.frame = 0
                red_enemy.delay = 0
                red_enemies.append (red_enemy)

        if planet.y == 900:
            next_planet = random.choice (planets)

            while True:
                if next_planet == planet.image:
                    next_planet = random.choice (planets)
                else:
                    break
            
            planet.image = next_planet
            planet.x = random.randint (frame_left, frame_right)
            planet.y = -center_y

        if level_completed == True:
            player.spawned = False
            
            if player.y > frame_top:
                player.y -= 5
            else:
                if keyboard.space:
                    new_level = True

        if new_level == True:
            if transition_step == 0:
                transition_one.y = int (HEIGHT + 300)
                transition_two.y = int (HEIGHT + 900)
                transition_three.y = int (HEIGHT + 1500)
                transition_step = 1
            if transition_step == 1:
                transition_one.y -= 10
                transition_two.y -= 10
                transition_three.y -= 10
                if transition_one.y < -center_y:
                    transition_step = 2
            if transition_step == 2:
                if (player.died == False) and (current_level < 6):
                    current_level += 1
                if (player.died == True) and (player.lives > 0):
                    player.lives -= 1
                    player.died = False
                if ((player.died == True) and (player.lives == 0)) or (current_level == 6):
                    current_level = 0
                    score = 0
                    player.lives = 5
                    player.died = False

                next_planet = random.choice (planets)

                while True:
                    if next_planet == planet.image:
                        next_planet = random.choice (planets)
                    else:
                        break
            
                planet.image = next_planet
                planet.x = random.randint (frame_left, frame_right)
                planet.y = -center_y

                background.y = center_y
                background_next.y = (background.y - 600)
                transition_one.y = int (HEIGHT + 300)
                transition_step = 3
            if transition_step == 3:
                level_completed = False
                enemies_defeated = 0
                player.frame = 0
                player.health = 100
                player.x = center_x
                player.y = frame_bottom
                level_timer = time_limit
                transition_two.y -= 10
                transition_three.y -= 10
                if transition_three.y < -center_y:
                    transition_step = 4
            if transition_step == 4:
                transition_two.y = int (HEIGHT + 900)
                transition_three.y = int (HEIGHT + 1500)

                if (current_level > 0) and (current_level < 5):
                    level_countdown -= 1
                    if level_countdown == 0:
                        level_countdown = 100
                        transition_step = 5
                else:
                    level_countdown = 100
                    transition_step = 5
                    
            if transition_step == 5:
                transition_step = 0
                new_level = False

    if background_next.y == center_y:
        background.y = center_y
        background_next.y = (background.y - 600)

def draw ():
    screen.clear ()
    background.draw ()
    background_next.draw ()
    planet.draw ()

    player.draw ()
    
    if transition_step < 2:
        for black_enemy in black_enemies:
            black_enemy.draw ()

        for blue_enemy in blue_enemies:
            blue_enemy.draw ()

        for green_enemy in green_enemies:
            green_enemy.draw ()

        for red_enemy in red_enemies:
            red_enemy.draw ()
            
        for black_enemy_laser in black_enemy_lasers:
            black_enemy_laser.draw ()

        for blue_enemy_laser in blue_enemy_lasers:
            blue_enemy_laser.draw ()

        for green_enemy_laser in green_enemy_lasers:
            green_enemy_laser.draw ()

        for red_enemy_laser in red_enemy_lasers:
            red_enemy_laser.draw ()
        
        for player_laser in player_lasers:
            player_laser.draw ()

    if current_level == 0:
        screen.draw.text ("VELTRAMON ZERO", fontname = "press_start", fontsize = (hud_size * 2.5), centerx = center_x, centery = (center_y - 130), color = (255, 255, 255), align = "center", owidth = 8, ocolor = "blue")
        screen.draw.text ("PRESS SPACE TO BEGIN", fontname = "press_start", fontsize = hud_size, centerx = center_x, centery = center_y, color = (255, 255, 255), align = "center", owidth = 4, ocolor = "blue")
        screen.draw.text ("LEFT/RIGHT = MOVE" + "\nUP/SPACE = FIRE" + "\nP = PAUSE", fontname = "press_start", fontsize = hud_size, centerx = center_x, centery = (center_y + 130), color = (255, 255, 255), align = "center", owidth = 4, ocolor = "blue")
        screen.draw.text ("POWERED BY" + "\nPYGAME ZERO", fontname = "press_start", align = "left", left = frame_left, centery = hud_top_y, color = (255, 255, 255), fontsize = hud_size, owidth = 4, ocolor = "blue")
        screen.draw.text ("PRE-ALPHA VERSION" + "\nBUILD 0.15", fontname = "press_start", align = "right", right = frame_right, centery = hud_top_y, color = (255, 255, 255), fontsize = hud_size, owidth = 4, ocolor = "blue")
        screen.draw.text ("NICHOLAS R. TRAPANI, 2023-2025" + "\nART BY JETREL AND KENNEY" + "\nFONT BY CODEMAN98", fontname = "press_start", fontsize = hud_size, centerx = center_x, centery = (center_y + 200), color = (255, 255, 255), align = "center", owidth = 4, ocolor = "blue")
        screen.draw.text ("THIS BUILD WILL NOT REPRESENT THE FULL RELEASE", fontname = "press_start", fontsize = (hud_size * 0.75), centerx = center_x, centery = hud_bottom_y, color = (255, 255, 255), align = "center", owidth = 4, ocolor = "blue")

    if (current_level > 0) and (current_level < 5):
        screen.draw.text ("SCORE\n" + str (score), fontname = "press_start", align = "left", left = frame_left, centery = hud_top_y, color = (255, 255, 255), fontsize = hud_size, owidth = 4, ocolor = "blue")
        screen.draw.text ("TIME\n" + str (level_timer), fontname = "press_start", centerx = center_x, centery = hud_top_y, color = (255, 255, 255), fontsize = hud_size, owidth = 4, ocolor = "blue")
        screen.draw.text ("LIVES\n" + str (player.lives), fontname = "press_start", align = "right", right = frame_right, centery = hud_top_y, color = (255, 255, 255), fontsize = hud_size, owidth = 4, ocolor = "blue")
        screen.draw.text ("HEALTH\n" + str (player.health), fontname = "press_start", align = "left", left = frame_left, centery = hud_bottom_y, color = (255, 255, 255), fontsize = hud_size, owidth = 4, ocolor = "blue")

    if current_level == 5:
        screen.draw.text ("THANK YOU FOR PLAYING" + "\nTHE VELTRAMON ZERO DEMO", fontname = "press_start", fontsize = (hud_size * 1.5), centerx = center_x, centery = (center_y - 100), color = (255, 255, 255), align = "center", owidth = 8, ocolor = "darkgreen")
        screen.draw.text ("PRESS SPACE TO CONTINUE", fontname = "press_start", fontsize = hud_size, centerx = center_x, centery = (center_y + 100), color = (255, 255, 255), align = "center", owidth = 8, ocolor = "blue")

    if (level_completed == True) and (player.y == frame_top) and (transition_step < 2):
        screen.draw.text ("LEVEL " + str (current_level) + "\nSCORE: " + str (score) + "\nPRESS SPACE TO CONTINUE", fontname = "press_start", center = (center_x, center_y), color = (255, 255, 255), fontsize = hud_size, owidth = 4, ocolor = "blue")

    if (transition_step > 2) and (transition_step < 5) and (current_level > 0) and (current_level < 5):
        screen.draw.text ("LEVEL " + str (current_level) + "\nDESTROY " + str (enemies_required) + " SHIPS" + "\nGET READY!", fontname = "press_start", center = (center_x, center_y), color = (255, 255, 255), fontsize = hud_size, owidth = 4, ocolor = "blue")

    transition_one.draw ()
    transition_two.draw ()
    transition_three.draw ()

    if game_paused == True:
        screen.draw.text ("GAME PAUSED", fontname = "press_start", centerx = center_x, centery = (center_y - 50), color = (255, 255, 255), fontsize = hud_size, owidth = 4, ocolor = "red4")

pgzrun.go ()
