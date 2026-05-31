import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from constants import PLAYER_SHOOT_COOLDOWN_SECONDS
from logger import log_state
from logger import log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main() -> None:
    pygame.init()
    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0

    STATE_PLAYING = 0
    STATE_GAMEOVER = 1
    current_state = STATE_PLAYING
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)

    asteroid_field = AsteroidField()
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, "--godmode" in sys.argv)

    dt = 0.0
    font = pygame.font.SysFont("Arial", 48)
    # ... previous setup code ...

    while running:
        log_state()
        dt = clock.tick(60) / 1000

        # 1. HANDLE INPUT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if current_state == STATE_GAMEOVER:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # Reset everything before playing again
                        for a in asteroids:
                            a.kill()
                        for s in shots:
                            s.kill()
                        score = 0
                        player.reset(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                        print("RESTARTING")
                        current_state = STATE_PLAYING

        # 2. UPDATE GAME STATE (Only if playing)
        if current_state == STATE_PLAYING:
            updatable.update(dt)

            for asteroid in asteroids:
                if player.collides_with(asteroid):
                    log_event("player_hit")
                    current_state = STATE_GAMEOVER

            for obj in asteroids:
                for inner_obj in shots:
                    if obj.collides_with(inner_obj):
                        log_event("asteroid_shot")
                        score += 1
                        obj.split()

        # 3. DRAW EVERYTHING
        screen.fill("black")
        
        if current_state == STATE_PLAYING:
            for obj in drawable:
                obj.draw(screen)
        
        elif current_state == STATE_GAMEOVER:
            msg_surface = font.render("YOU DIED", True, "red")
            score_surface = font.render(f"Score: {score}", True, "white")
            retry_surface = font.render("Press 'R' to Retry", True, "gray")
            screen.blit(msg_surface, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 50))
            screen.blit(score_surface, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 10))
            screen.blit(retry_surface, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 70))

        pygame.display.flip()

        # limit the framerate to 60 FPS


if __name__ == "__main__":
    main()
import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from constants import PLAYER_SHOOT_COOLDOWN_SECONDS
from logger import log_state
from logger import log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main() -> None:
    pygame.init()
    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0

    STATE_PLAYING = 0
    STATE_GAMEOVER = 1
    current_state = STATE_PLAYING
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)

    asteroid_field = AsteroidField()
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, "--godmode" in sys.argv)

    dt = 0.0
    font = pygame.font.SysFont("Arial", 48)
    # ... previous setup code ...

    while running:
        log_state()
        dt = clock.tick(60) / 1000

        # 1. HANDLE INPUT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if current_state == STATE_GAMEOVER:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # Reset everything before playing again
                        for a in asteroids:
                            a.kill()
                        for s in shots:
                            s.kill()
                        score = 0
                        player.reset(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                        print("RESTARTING")
                        current_state = STATE_PLAYING

        # 2. UPDATE GAME STATE (Only if playing)
        if current_state == STATE_PLAYING:
            updatable.update(dt)

            for asteroid in asteroids:
                if player.collides_with(asteroid):
                    log_event("player_hit")
                    current_state = STATE_GAMEOVER

            for obj in asteroids:
                for inner_obj in shots:
                    if obj.collides_with(inner_obj):
                        log_event("asteroid_shot")
                        score += 1
                        obj.split()

        # 3. DRAW EVERYTHING
        screen.fill("black")
        
        if current_state == STATE_PLAYING:
            for obj in drawable:
                obj.draw(screen)
        
        elif current_state == STATE_GAMEOVER:
            msg_surface = font.render("YOU DIED", True, "red")
            score_surface = font.render(f"Score: {score}", True, "white")
            retry_surface = font.render("Press 'R' to Retry", True, "gray")
            screen.blit(msg_surface, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 50))
            screen.blit(score_surface, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 10))
            screen.blit(retry_surface, (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 70))

        pygame.display.flip()

        # limit the framerate to 60 FPS


if __name__ == "__main__":
    main()
