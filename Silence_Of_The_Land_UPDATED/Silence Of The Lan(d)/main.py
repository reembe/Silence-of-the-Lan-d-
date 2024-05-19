import pygame
import time
from player import Player
from mini_bosses import Mini
from main_bosses import Main

# the portion above imports the modules/packages as well as the classes we created

# the following below initializes pygame modules that are used as well as the screen and text font
pygame.init()
pygame.font.init()
title_font = pygame.font.Font("joystix.ttf", 55)
pygame.display.set_caption("Silence of the Lan(d)")
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.mixer.init()


# backgrounds for each screen
bg_loading = pygame.image.load("loadingscreen.jpg")
bg_story = pygame.image.load("village.png")
bg_game = pygame.image.load("dark_sky.jpg")
bg_win = pygame.image.load('win.png')

# this sets up the music. whenever you see variable.play(), its starting a song. whenever you see pygame.mixer.fadeout(2), this is to end the song.
# the s in s1, s2, s3 stands for song.
welcome = pygame.mixer.Sound("welcome_screen_music.wav")
death = pygame.mixer.Sound("death_noise.wav")
s1 = pygame.mixer.Sound("song2.wav")
s2 = pygame.mixer.Sound("song3.wav")
s5 = pygame.mixer.Sound("song6.wav")

# fonts and messages for the instructions
loading_font = pygame.font.Font("joystix.ttf", 35)
instructions_font = pygame.font.Font("joystix.ttf", 45)
instructions_font2 = pygame.font.Font("joystix.ttf", 23)
game_msg_1 = instructions_font.render("WELCOME!!", True, (255, 255, 255))
game_msg_2 = instructions_font.render("Your goal is to eliminate all the monsters.", True, (255, 255, 255))

# timer
start_times = 0
timer_font = pygame.font.Font("joystix.ttf", 25)

# creates objects and sets up player and enemy health
enemy = Mini(2070, 870, 1)
big_enemy = Main(2030, 800, 1)
enemy1 = Mini(2030, 870, 2)
big_enemy1 = Main(2030, 800, 2)
enemy2 = Mini(2070, 870, 3)
big_enemy2 = Main(2030, 800, 3)
enemy3 = Mini(2030, 870, 4)
big_enemy3 = Main(2030, 800, 4)
enemy4 = Mini(2070, 870, 5)
big_enemy4 = Main(2030, 800, 5)

big_reset = True
small_reset = True
big1_reset = True
small1_reset = True
big2_reset = True
small2_reset = True
big3_reset = True
small3_reset = True
big4_reset = True
small4_reset = True

x = 300
y = 900
player = Player(x, y)
direction = "up"
player_health = 250

mini_enemy_health = 50
mini_enemy_health1 = 50
mini_enemy_health2 = 50
mini_enemy_health3 = 50
mini_enemy_health4 = 50
main_enemy_health = 75
main_enemy_health1 = 75
main_enemy_health2 = 75
main_enemy_health3 = 75
main_enemy_health4 = 75




# the variables for the typewriting effect on the loading screen
msgs = ["you were a young girl living peacefully in a village.",
        'until one day... monsters rose from the ground...',
        'and attacked it!',
        'now, the king has entrusted you with the task',
        'of saving your village... but can you do it?']

counter1 = 0    # counter represents each character in the message and checks if the message is completely written
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
speed = 16     # how long it takes for the next character to be written on the screen; bigger number = slower typing
done = False    # checks if the message is done

# the variables for the typewriting effect on the death/loss/win screens
other_counter = 0
other_speed = 16
other_done = False
death_msg = "you died... what a disappointment."
loss_msg = ["you didn't collect enough points...",
            'you were so close...']
won_msg = ["you won!! the king's army has arrived and",
           "congratulates you on your victory!"]

# screens
start_now = False
first_time = True
loading_screen = True
story_screen = False
game_screen = False
death_screen = False
loss_screen = False
win_screen = False
points = 0


# the loading screen at beginning of the game

while loading_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loading_screen = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            story_screen = True
            game_screen = False
            loading_screen = False  # start game screen
            pygame.mixer.fadeout(2)

    screen.blit(bg_loading, (0, 0))
    # pygame.mixer.Sound.play(welcome_music)
    welcome.play()
    title_msg = title_font.render("SILENCE OF THE LAN(D)", True, (32, 17, 66))
    screen.blit(title_msg, (500, 500))
    title_font2 = pygame.font.Font("joystix.ttf", 49)
    title_msg2 = title_font2.render("Click anywhere to start!", True, (32, 17, 66))
    screen.blit(title_msg2, (500, 250))

    pygame.display.update()

# the story screen which details the background of why the player is going on this monster eliminating journey

while story_screen:

    if start_times == 0:
        start = time.time()
        start_times += 1
    timer = round((time.time() - start), 1)
    s1.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loading_screen = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            story_screen = False
            game_screen = True
            timer = 0
            first_time = True
            start_times = 0  # start game screen
            pygame.mixer.fadeout(2)

    screen.blit(bg_story, (0, 0))

    # the code below checks if the whole message is on the screen or not; if not, 1 is added to the counter
    # there are multiple counters for each message

    if timer >= 0.5:
        if counter1 < speed * len(msgs[0]):
            counter1 += 1
        elif counter1 >= speed * len(msgs[0]):
            done = True
        new_msg1 = loading_font.render(msgs[0][0:counter1 // speed], True, 'white')
        screen.blit(new_msg1, (200, 130))
    if timer >= 4:
        if counter2 < speed * len(msgs[1]):
            counter2 += 1
        elif counter2 >= speed * len(msgs[1]):
            done = True
        new_msg2 = loading_font.render(msgs[1][0:counter2 // speed], True, 'white')
        screen.blit(new_msg2, (245, 200))
    if timer >= 8.5:
        if counter3 < speed * len(msgs[2]):
            counter3 += 1
        elif counter3 >= speed * len(msgs[2]):
            done = True
        new_msg3 = loading_font.render(msgs[2][0:counter3 // speed], True, 'red')
        screen.blit(new_msg3, (735, 270))
    if timer >= 11:
        screen.blit(bg_story, (0, 0))
    if timer >= 11.5:
        if counter4 < speed * len(msgs[3]):
            counter4 += 1
        elif counter4 >= speed * len(msgs[3]):
            done = True
        new_msg4 = loading_font.render(msgs[3][0:counter4 // speed], True, 'white')
        screen.blit(new_msg4, (250, 130))
    if timer >= 15.5:
        if counter5 < speed * len(msgs[4]):
            counter5 += 1
        elif counter5 >= speed * len(msgs[4]):
            done = True
        new_msg5 = loading_font.render(msgs[4][0:counter5 // speed], True, 'white')
        screen.blit(new_msg5, (255, 200))

    # the code above creates the typewriter effect for each message and begins typing at the specific second
    # mentioned in the if statement

# when this time appears or if the player clicks the screen, the game instructions will begin

    if timer >= 25.5:
        story_screen = False
        game_screen = True
        timer = 0
        first_time = True
        start_times = 0
        pygame.mixer.fadeout(2)

    pygame.display.update()

# below is the game screen where instructions print first and the battle is second

while game_screen:
    s5.play(loops=100)
    pygame.display.update()
    if start_times == 0:
        start = time.time()
        start_times += 1
    timer = round((time.time() - start), 1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loading_screen = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_screen = True

    if first_time == True:
        screen.blit(bg_game, (0, 0))

    # the code below blits instruction messages at every message's respective second

    if timer >= 0.5 and start_now == False:
        screen.blit(instructions_font.render("WELCOME!!", True, (255, 255, 255)), (810, 120))
    if timer >= 2 and start_now == False:
        screen.blit(instructions_font2.render("Your goal is to eliminate all the monsters without dying.", True,
                                              (255, 255, 255)), (405, 190))
    if timer >= 4 and start_now == False:
        screen.blit(instructions_font2.render("Small monsters are 5 points, big monsters are 10 points.", True,
                                              (255, 255, 255)),
                    (411, 260))
    if timer >= 6.5 and start_now == False:
        screen.blit(instructions_font2.render("Use WASD to move and click the monsters to eliminate them!", True,
                                              (255, 255, 255)),
                    (400, 330))
    if timer >= 8 and start_now == False:
        screen.blit(instructions_font2.render("Get 350 points for the king's validation!", True,
                                              (255, 255, 255)),
                    (540, 400))


    # when its this time the game starts

    if timer >= 11.5:
        start_now = True

# the game uses a combination of the timer, and a points system to end the game and score the player.
# The monsters spawn in based on timer and have a certain amount of time before they despawn.
# The player must click them before then.
# as the game progresses the monsters respawn faster. the monsters use the go_to_player function to always head to the direction of the player.
# the player moves using the keyboard event getpressed.()
# collide is used to detect if the enemies touch the player or if the players mouse touch the enemies.

    if start_now == True:
        if first_time == True:
            start_times = 0
            first_time = False
        if start_times == 0:
            start = time.time()
            start_times += 1
        timer = round((time.time() - start), 1)
        screen.blit(bg_game, (0, 0))
        pygame.draw.rect(screen, (255, 0, 0), (1600, 15, 250, 20))              # draws the green health bar
        pygame.draw.rect(screen, (0, 255, 0), (1600, 15, player_health, 20))    # draws the red health bar
        screen.blit(player.image, player.rect)
        screen.blit(timer_font.render("Timer: " + str(timer) + " seconds", True, (255, 255, 255)), (5, 15))
        screen.blit(timer_font.render("Points: " + str(points), True, (255, 255, 255)), (1600, 45))
        screen.blit(enemy.image, enemy.rect)
        enemy.go_to_player(player)


# spawns in the enemies at a certain time and makes them follow player. it also resets their health
        if timer >= 2 and timer <= 34:
            screen.blit(enemy2.image, enemy2.rect)
            enemy2.go_to_player(player)
        if timer >= 3 and timer <= 34:
            screen.blit(enemy1.image, enemy1.rect)
            enemy1.go_to_player(player)
        if timer >= 4 and timer <= 38:
            screen.blit(enemy3.image, enemy3.rect)
            enemy3.go_to_player(player)
        if timer >= 5 and timer <= 42:
            screen.blit(enemy4.image, enemy4.rect)
            enemy4.go_to_player(player)
        if timer >= 6 and timer <= 44:
            screen.blit(big_enemy1.image, big_enemy1.rect)
            big_enemy1.go_to_player(player)
        if timer >= 7 and timer <= 23:
            screen.blit(big_enemy3.image, big_enemy3.rect)
            big_enemy3.go_to_player(player)
        if timer >= 8 and timer <= 26:
            screen.blit(big_enemy4.image, big_enemy4.rect)
            big_enemy4.go_to_player(player)
        if timer >= 9 and timer <= 29:
            screen.blit(big_enemy.image, big_enemy.rect)
            big_enemy.go_to_player(player)
        if timer >= 11 and timer <= 54:
            if big3_reset:
                big_enemy3.reset_main(2060, 870)
                big3_reset = False
                main_enemy_health3 = 75
            screen.blit(big_enemy3.image, big_enemy3.rect)
            big_enemy3.go_to_player(player)
        if timer >= 12 and timer <= 57:
            if big4_reset:
                big_enemy4.reset_main(2090, 870)
                big4_reset = False
                main_enemy_health4 = 75
            screen.blit(big_enemy4.image, big_enemy4.rect)
            big_enemy4.go_to_player(player)
        if timer >= 13 and timer <= 52:
            if big_reset:
                big_enemy.reset_main(2050, 870)
                big_reset = False
                main_enemy_health = 75
            screen.blit(big_enemy.image, big_enemy.rect)
            big_enemy.go_to_player(player)
        if timer >= 32 and timer <= 54:
            if big2_reset:
                big_enemy2.reset_main(2040, 870)
                big2_reset = False
                main_enemy_health2 = 75
            screen.blit(big_enemy2.image, big_enemy2.rect)
            big_enemy2.go_to_player(player)
        if timer >= 34 and timer <= 40:
            if small1_reset:
                enemy1.reset_mini(2070, 870)
                small1_reset = False
                mini_enemy_health1 = 50
            screen.blit(enemy1.image, enemy1.rect)
            enemy1.go_to_player(player)
        if timer >= 38 and timer <= 44:
            if small3_reset:
                enemy3.reset_mini(2030, 870)
                small3_reset = False
                mini_enemy_health3 = 50
            screen.blit(enemy3.image, enemy3.rect)
            enemy3.go_to_player(player)
        if timer >= 42 and timer <= 48:
            if small4_reset:
                enemy4.reset_mini(2060, 870)
                small4_reset = False
                mini_enemy_health4 = 50
            screen.blit(enemy4.image, enemy4.rect)
            enemy4.go_to_player(player)
        if timer >= 44 and timer <= 52:
            if big1_reset:
                big_enemy1.reset_main(2080, 870)
                big1_reset = False
                main_enemy_health1 = 75
            screen.blit(big_enemy1.image, big_enemy1.rect)
            big_enemy1.go_to_player(player)
        if timer >= 48 and timer <= 54:
            if big3_reset:
                big_enemy3.reset_main(2090, 870)
                big3_reset = False
                main_enemy_health3 = 75
            screen.blit(big_enemy3.image, big_enemy3.rect)
            big_enemy3.go_to_player(player)
        if timer >= 50 and timer <= 56:
            if big4_reset:
                big_enemy4.reset_main(2030, 870)
                big4_reset = False
                main_enemy_health4 = 75
            screen.blit(big_enemy4.image, big_enemy4.rect)
            big_enemy4.go_to_player(player)
        if timer >= 52 and timer <= 58:
            if big_reset:
                big_enemy.reset_main(2070, 870)
                big_reset = False
                main_enemy_health = 75
            screen.blit(big_enemy.image, big_enemy.rect)
            big_enemy.go_to_player(player)
        if timer >= 54 and timer <= 60:
            if big2_reset:
                big_enemy2.reset_main(2050, 870)
                big2_reset = False
                main_enemy_health2 = 75
            screen.blit(big_enemy2.image, big_enemy2.rect)
            big_enemy2.go_to_player(player)
        if timer >= 57:
            if small1_reset:
                enemy1.reset_mini(2080, 870)
                small1_reset = False
                mini_enemy_health1 = 50
            screen.blit(enemy1.image, enemy1.rect)
            enemy1.go_to_player(player)
        if timer >= 59:
            if small3_reset:
                enemy3.reset_mini(2010, 870)
                small3_reset = False
                mini_enemy_health3 = 50
            screen.blit(enemy3.image, enemy3.rect)
            enemy3.go_to_player(player)
        if timer >= 62:
            if small4_reset:
                enemy4.reset_mini(2020, 870)
                small4_reset = False
                mini_enemy_health4 = 50
            screen.blit(enemy4.image, enemy4.rect)
            enemy4.go_to_player(player)
        if timer >= 64:
            if big1_reset:
                big_enemy1.reset_main(2050, 870)
                big1_reset = False
                main_enemy_health1 = 75
            screen.blit(big_enemy1.image, big_enemy1.rect)
            big_enemy1.go_to_player(player)
        if timer >= 66:
            if big3_reset:
                big_enemy3.reset_main(2060, 870)
                big3_reset = False
                main_enemy_health3 = 75
            screen.blit(big_enemy3.image, big_enemy3.rect)
            big_enemy3.go_to_player(player)
        if timer >= 69:
            if big4_reset:
                main_enemy_health4 = 75
                big_enemy4.reset_main(2090, 870)
                big4_reset = False
            screen.blit(big_enemy4.image, big_enemy4.rect)
            big_enemy4.go_to_player(player)
        if timer >= 72:
            if big_reset:
                main_enemy_health = 75
                big_enemy.reset_main(2030, 870)
                big_reset = False
            screen.blit(big_enemy.image, big_enemy.rect)
            big_enemy.go_to_player(player)
        if timer >= 74:
            if big2_reset:
                main_enemy_health2 = 75
                big_enemy2.reset_main(2070, 870)
                big2_reset = False
            screen.blit(big_enemy2.image, big_enemy2.rect)
            big_enemy2.go_to_player(player)

        if timer == 40 and points < 350:
            game_screen = False
            loss_screen = True
            pygame.mixer.fadeout(2)
        if timer == 40 and points >= 350:
            game_screen = False
            win_screen = True
            pygame.mixer.fadeout(2)


# detects if the player dealt damage to any enemies and if they were killed

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.player_attack(direction)
            if enemy.rect.collidepoint(event.pos):
                mini_enemy_health -= 50
                points += 5
                if mini_enemy_health == 0:
                    small_reset = True
                    enemy.reset_mini(-10000, -10000)
            if enemy1.rect.collidepoint(event.pos):
                mini_enemy_health1 -= 50
                points += 5
                if mini_enemy_health1 == 0:
                    small1_reset = True
                    enemy1.reset_mini(-10000, -10000)
            if enemy2.rect.collidepoint(event.pos):
                mini_enemy_health2 -= 50
                points += 5
                if mini_enemy_health2 == 0:
                    small2_reset = True
                    enemy2.reset_mini(-10000, -10000)
            if enemy3.rect.collidepoint(event.pos):
                mini_enemy_health3 -= 50
                points += 5
                if mini_enemy_health3 == 0:
                    small3_reset = True
                    enemy3.reset_mini(-10000, -10000)
            if enemy4.rect.collidepoint(event.pos):
                mini_enemy_health4 -= 50
                points += 5
                if mini_enemy_health4 == 0:
                    small4_reset = True
                    enemy4.reset_mini(-10000, -10000)

            if big_enemy.rect.collidepoint(event.pos):
                main_enemy_health -= 75
                points += 10
                if main_enemy_health == 0:
                    big_reset = True
                    big_enemy.reset_main(-10000, -10000)
            if big_enemy1.rect.collidepoint(event.pos):
                main_enemy_health1 -= 75
                points += 10
                if main_enemy_health1 == 0:
                    big1_reset = True
                    big_enemy1.reset_main(-10000, -10000)
            if big_enemy2.rect.collidepoint(event.pos):
                main_enemy_health2 -= 75
                points += 10
                if main_enemy_health2 == 0:
                    big2_reset = True
                    big_enemy2.reset_main(-10000, -10000)
            if big_enemy3.rect.collidepoint(event.pos):
                main_enemy_health3 -= 75
                points += 10
                if main_enemy_health3 == 0:
                    big3_reset = True
                    big_enemy3.reset_main(-10000, -10000)
            if big_enemy4.rect.collidepoint(event.pos):
                main_enemy_health4 -= 75
                points += 10
                if main_enemy_health4 == 0:
                    big4_reset = True
                    big_enemy4.reset_main(-10000, -10000)

# detects player movement through keyboard input

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        direction = "up"
        player.move_player(direction)
    if keys[pygame.K_s]:
        direction = "down"
        player.move_player(direction)
    if keys[pygame.K_a]:
        direction = "left"
        player.move_player(direction)
    if keys[pygame.K_d]:
        direction = "right"
        player.move_player(direction)




# detects if player has been hit by enemy. uses a timer to make sure player isn't killed too fast

    if timer % 2 == 0:
        if player.rect.colliderect(enemy.rect):
            player_health -= 1

        if player.rect.colliderect(enemy1.rect):
            player_health -= 1

        if player.rect.colliderect(enemy2.rect):
            player_health -= 1

        if player.rect.colliderect(enemy3.rect):
            player_health -= 1

        if player.rect.colliderect(enemy4.rect):
            player_health -= 1

        if player.rect.colliderect(big_enemy.rect):
            player_health -= 2

        if player.rect.colliderect(big_enemy1.rect):
            player_health -= 2

        if player.rect.colliderect(big_enemy2.rect):
            player_health -= 2

        if player.rect.colliderect(big_enemy3.rect):
            player_health -= 2

        if player.rect.colliderect(big_enemy4.rect):
            player_health -= 2





# detects if player health goes below 0 and sends them to the death screen

    if player_health <= 0:
        game_screen = False
        death_screen = True
        pygame.mixer.fadeout(2)

# death screen where player loses

while death_screen:
    death.play()


    if other_counter < other_speed * len(death_msg):
        other_counter += 1
    elif other_counter >= other_speed * len(death_msg):
        other_done = True
    new_death_msg = loading_font.render(death_msg[0:other_counter // other_speed], True, 'white')

    screen.fill((0, 0, 0))
    screen.blit(new_death_msg, (465, 400))

    pygame.display.update()

# winning screen where player survives and gets enough points

while win_screen:
    s1.play()

    if other_counter < other_speed * len(won_msg[0]):
        other_counter += 1
    elif other_counter >= other_speed * len(won_msg[0]):
        other_done = True
    new_won_msg1 = loading_font.render(won_msg[0][0:other_counter // other_speed], True, 'white')

    if other_counter < other_speed * len(won_msg[1]):
        other_counter += 1
    elif other_counter >= other_speed * len(won_msg[1]):
        other_done = True
    new_won_msg2 = loading_font.render(won_msg[1][0:other_counter // other_speed], True, 'white')

    screen.blit(bg_win, (0, 0))
    screen.blit(new_won_msg1, (350, 350))
    screen.blit(new_won_msg2, (350, 390))

    pygame.display.update()

# losing screen where player survives and doesn't get enough points

while loss_screen:
    s2.play()

    if other_counter < other_speed * len(loss_msg[0]):
        other_counter += 1
    elif other_counter >= other_speed * len(loss_msg[0]):
        other_done = True
    new_loss_msg1 = loading_font.render(loss_msg[0][0:other_counter // other_speed], True, 'white')

    if other_counter < other_speed * len(loss_msg[1]):
        other_counter += 1
    elif other_counter >= other_speed * len(loss_msg[1]):
        other_done = True
    new_loss_msg2 = loading_font.render(loss_msg[1][0:other_counter // other_speed], True, 'white')

    screen.blit(bg_win, (0, 0))
    screen.blit(new_loss_msg1, (350, 350))
    screen.blit(new_loss_msg2, (350, 390))

    pygame.display.update()
