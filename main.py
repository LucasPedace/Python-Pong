import pygame, sys, random


def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        player_score += 1
        ball_restart()

    if ball.right >= screen_width:
        opponent_score += 1
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai():
    opponent.y += opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_restart():
    global  ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))


# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1020
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color(10, 10, 10)
green_color = (0, 125, 0)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 0

# Text Variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Player on the right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

        # Player on the left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                opponent_speed += 7
            if event.key == pygame.K_w:
                opponent_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                opponent_speed -= 7
            if event.key == pygame.K_w:
                opponent_speed += 7

    # Game logic
    ball_animation()
    player_animation()
    opponent_ai()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, green_color, player)
    pygame.draw.rect(screen, green_color, opponent)
    pygame.draw.ellipse(screen, green_color, ball)
    pygame.draw.aaline(screen, green_color, (screen_width / 2, 0), (screen_width / 2, screen_height))

    player_text = game_font.render(f"{player_score}", False, green_color)
    screen.blit(player_text, ((screen_width/2 + 30), 340))

    opponent_text = game_font.render(f"{opponent_score}", False, green_color)
    screen.blit(opponent_text, ((screen_width/2 - 50), 340))

    # Updating the window
    pygame.display.flip()
    clock.tick(60)

