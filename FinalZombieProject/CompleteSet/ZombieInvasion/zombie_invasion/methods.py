import sys
from time import sleep
import pygame
import bullet as Bul
import zombie as Zomb
import random

def UpdateScreen(background, bullets, play, display, settings, stats, shooter, zombies):
    # Requirement ID: 2.0.0
    """Refreshes items on the screen."""

    settings.screen.blit(background, background.get_rect())
    # This method draws the bullets on the screen for each bullet in the bullet list.
    for bullet in bullets.sprites():
        bullet.Draw()

    zombies.draw(settings.screen)
    shooter.blitme()
    display.Display()

    # If the game is not active display play button.
    if not stats.game_active:
        play.PlayButton()

    pygame.display.flip()


def EventCheck(bullets, play, display, settings, stats, shooter, zombies):
    # Requirement ID: 2.0.1
    """Check for Key events. This method checks if a key was pressed on the keyboard
    of if a mouse button was clicked."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYUP:
            KeyUpCheck(event, shooter)
        elif event.type == pygame.KEYDOWN:
            KeyDownCheck(bullets, event, settings, shooter, stats)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            Play(bullets, display, mouse_x, mouse_y, play, settings, stats, shooter, zombies)


def KeyDownCheck(bullets, event, settings, shooter, stats):
    # Requirement ID: 2.0.2
    """Check for Key Down Event. This method checks if a key was pressed on the keyboard and if so, moves the
     shooter, rotates the shooter, or shoots a bullet."""

    if event.key == pygame.K_RIGHT: shooter.moving_right = True
    elif event.key == pygame.K_LEFT: shooter.moving_left = True
    elif event.key == pygame.K_UP: shooter.moving_up = True
    elif event.key == pygame.K_DOWN: shooter.moving_down = True
    elif event.key == pygame.K_b:
        ShootMegaBullets(stats, settings, shooter, bullets)
    elif event.key == pygame.K_SPACE:
        ShootBullet(settings, shooter, bullets)
    elif event.key == pygame.K_KP1 or event.key == pygame.K_x: shooter.Rotate(45.0)
    elif event.key == pygame.K_KP3 or event.key == pygame.K_c: shooter.Rotate(315.0)
    elif event.key == pygame.K_KP2 or event.key == pygame.K_z: shooter.Rotate(90.0)
    elif event.key == pygame.K_KP4 or event.key == pygame.K_v: shooter.Rotate(270.0)
    elif event.key == pygame.K_q: sys.exit()


def ShootMegaBullets(stats, settings, shooter, bullets):
    # Requirement ID: 2.0.3
    """Shoot the mega bullets."""

    settings.IsMegaBullet = True
    if(stats.shot_bullets <= settings.number_of_mega_bullets and stats.level>0):
        new_bullet = Bul.Bullet(settings, shooter)
        bullets.add(new_bullet)
        stats.remaining_bullets = settings.number_of_mega_bullets - stats.shot_bullets
        stats.shot_bullets += 1


def ShootBullet(settings, shooter, bullets):
    # Requirement ID: 2.0.4
    """Shoot ordinary bullets."""

    settings.bullet_size = 7
    settings.bullet_color = settings.black
    new_bullet = Bul.Bullet(settings, shooter)
    bullets.add(new_bullet)


def KeyUpCheck(event, shooter):
    # Requirement ID: 2.0.5
    """Check key up events. This method checks if a key was lifted. """

    keys = pygame.key.get_pressed()

    if event.key == pygame.K_RIGHT: shooter.moving_right = False

    elif event.key == pygame.K_LEFT: shooter.moving_left = False

    elif event.key == pygame.K_UP: shooter.moving_up = False

    elif event.key == pygame.K_DOWN: shooter.moving_down = False

    elif event.key == pygame.K_KP1 or event.key == pygame.K_x:
        shooter.Rotate(315.0) if (keys[pygame.K_KP3] or keys[pygame.K_c]) else shooter.Rotate(0.0)
        shooter.Rotate(90.0) if (keys[pygame.K_KP2] or keys[pygame.K_z]) else shooter.Rotate(0.0)
        shooter.Rotate(270.0) if (keys[pygame.K_KP4] or keys[pygame.K_v]) else shooter.Rotate(0.0)

    elif event.key == pygame.K_KP2 or event.key == pygame.K_z:
        shooter.Rotate(315.0) if (keys[pygame.K_KP3] or keys[pygame.K_c]) else shooter.Rotate(0.0)
        shooter.Rotate(45.0) if (keys[pygame.K_KP1] or keys[pygame.K_x]) else shooter.Rotate(0.0)
        shooter.Rotate(270.0) if (keys[pygame.K_KP4] or keys[pygame.K_v]) else shooter.Rotate(0.0)

    elif event.key == pygame.K_KP3 or event.key == pygame.K_c:
        shooter.Rotate(45.0) if (keys[pygame.K_KP1] or keys[pygame.K_x]) else shooter.Rotate(0.0)
        shooter.Rotate(90.0) if (keys[pygame.K_KP2] or keys[pygame.K_z]) else shooter.Rotate(0.0)
        shooter.Rotate(270.0) if (keys[pygame.K_KP4] or keys[pygame.K_v]) else shooter.Rotate(0.0)

    elif event.key == pygame.K_KP4 or event.key == pygame.K_v:
        shooter.Rotate(315.0) if (keys[pygame.K_KP3] or keys[pygame.K_c]) else shooter.Rotate(0.0)
        shooter.Rotate(90.0) if (keys[pygame.K_KP2] or keys[pygame.K_z]) else shooter.Rotate(0.0)
        shooter.Rotate(45.0) if (keys[pygame.K_KP1] or keys[pygame.K_x]) else shooter.Rotate(0.0)


def UpdateObjects(bullets, display, settings, stats, shooter, zombies):
    # Requirement ID: 2.0.6
    "This method initializes the bullet settings, calls the UpdateBullets and UpdateZombies methods."

    InitializeBulletSettings(stats, settings)
    UpdateBullets(bullets, display, settings, stats, shooter, zombies)
    UpdateZombies(bullets, display, settings, stats, shooter, zombies)


def UpdateZombies(bullets, display, settings, stats, shooter, zombies):
    # Requirement ID: 2.0.7
    """This method updates the zombies on the screen, checks if a zombie has collided with a shooter, and
     ensures that the zombies do not go off the screen.
      """

    ZombiesOnScreen(settings, zombies)

    zombies.update()

    if pygame.sprite.spritecollideany(shooter, zombies):
        ShooterDown(bullets, display, settings, stats, shooter, zombies)

    ZombiesOffTheScreen(bullets, display, settings, stats, shooter, zombies)


def RemoveBullets(bullets):
    # Requirement ID: 2.0.8
    "This method removes bullets that have gone off the screen."

    for bullet in bullets.copy():
        bullet.rect = bullet.circle
        # print(bullet.rect.bottom)
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        if bullet.rect.right <= 0:
            bullets.remove(bullet)
        if bullet.rect.left <= 0:
            bullets.remove(bullet)


def IncrementScore(collisions, stats, display=None):
    # Requirement ID: 2.0.9
    """If a zombie is killed, increment the score by 1."""

    if collisions:
        stats.score += 1
        if display != None:
            display.InitScore()


def UpdateBullets(bullets, display, settings, stats, shooter, zombies):
    # Requirement ID: 2.1.0
    """This method updates bullets on the screen and checks if they have hit a zombie. If the bullets have
    hit a zombie, increment the score. If all of the zombies have been killed, reset the board and increment the
    level. """

    bullets.update()
    display.Bullets()

    RemoveBullets(bullets)
    crashed = {}
    SC = pygame.sprite.spritecollide

    #Modification to the sprints collision method. Only removes non mega bullets on collision.
    for bullet in bullets.sprites():
        bang = SC(bullet, zombies, True, None)
        if bang:
            crashed[bullet] = bang
            if(settings.IsMegaBullet == False):
                bullet.kill()
    collisions = crashed

    IncrementScore(collisions,stats,display)

    #New level when all of the zombies are gone
    if len(zombies) == 0:
        bullets.empty()
        settings.ResizeZombies()
        stats.level += 1
        settings.IsMegaBullet = False
        stats.shot_bullets = 0
        display.Level()
        display.Bullets()
        ZombieCollection(settings, shooter, zombies)
        stats.remaining_bullets = settings.number_of_mega_bullets - stats.shot_bullets

        InitializeBulletSettings(stats, settings)


def InitializeBulletSettings(stats, settings):
    # Requirement ID: 2.1.1
    """Initialize bullet settings. Each level will give the shooter more mega bullets.
    be given a special mega bullet that will be a random size larger than the first mega bullet."""

    if (stats.level < settings.mega_bullet_level[0]):
        MegaBulletSettings(settings, 0, settings.red)
    elif (stats.level < settings.mega_bullet_level[1]):
        MegaBulletSettings(settings, 1, settings.fireball)
    elif (stats.level < settings.mega_bullet_level[2]):
        MegaBulletSettings(settings, 2, settings.megafireball)
    else:
        settings.bullet_color = settings.supernova
        rn = (random.randint(10, 50))
        settings.bullet_size = rn
        settings.number_of_mega_bullets = settings.cnt_mega_bullets[3]


def MegaBulletSettings(settings, level, color):
    # Requirement ID: 2.1.2
    """This method sets the size and color of the mega bullet"""

    settings.bullet_color = color
    settings.bullet_size = settings.size_of_mega_bullet[level]
    settings.number_of_mega_bullets = settings.cnt_mega_bullets[level]


def CheckForWin(stats, settings, button, zombies, bullets, shooter):
    # Requirement ID: 2.1.3
    """This method checks if the level is a winning level and if so prints a win message."""

    if (stats.level == settings.number_of_levels):
        play = button.PlayButton(settings)
        stats.game_active = False
        ResetGame(zombies, bullets, settings, shooter, stats)
        return play


def ShooterDown(bullets, display, settings, stats, shooter, zombies):
    # Requirement ID: 2.1.4
    """Checks if a shooter was hit by a zombie and if so decrements the lives."""

    if stats.lives > 0:
        stats.lives -= 1
        display.Shooters()
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

    ResetGame(zombies, bullets, settings, shooter, stats)


def ZombiesOnScreen(settings, zombies):
    # Requirement ID: 2.1.5
    """Zombies change direction when hit the edge of the screen"""

    for zombie in zombies.sprites():
        if zombie.ZombiesOnTheScreen():
            settings.fleet_direction *= -1
            break


def ZombiesOffTheScreen(bullets, display, settings, stats, shooter, zombies):
    # Requirement ID: 2.1.6
    """This method checks if the zombie hits the bottom of the screen. If the zombie hits the bottom of the
    screen the shooter dies. """

    screen_rect = settings.screen.get_rect()
    for zombie in zombies.sprites():
        if zombie.rect.bottom >= screen_rect.bottom:
            ShooterDown(bullets, display, settings, stats, shooter, zombies)
            break


def ZombieCollection(settings, shooter, zombies):
    # Requirement ID: 2.1.7
    """Zombie Collection. This method determines how many zombies to put on the screen.
    With each level the zombies get smaller and more zombies fit on the screen. """

    zomb = Zomb.Zombie(settings)
    available_space_x = settings.screen_width - zomb.rect.width

    if zomb.rect.width < 5: zomb.rect.width = 5
    number_zombies_x = int(available_space_x / (zomb.rect.width))

    #this method determines the space available to fit zombies.
    available_space_y = (settings.screen_height - (3 * zomb.rect.height) - shooter.rect.height)

    if zomb.rect.height <5: zomb.rect.height = 5
    number_rows = int(available_space_y / (2 * zomb.rect.height))

    for row_number in range(number_rows):
        for zombie_number in range(number_zombies_x):
            zomb = Zomb.Zombie(settings)
            zombie_width = zomb.rect.width
            zomb.x = zombie_width + zombie_width * zombie_number
            zomb.rect.x = zomb.x
            zomb.rect.y = zomb.rect.height + 2 * zomb.rect.height * row_number
            zomb.CenterZombie()
            zomb.x = float(zomb.rect.x)
            zomb.y = float(zomb.rect.y)
            zombies.add(zomb)


def ResetGame(zombies, bullets, settings, shooter, stats):
    # Requirement ID: 2.1.8
    """Reset items on the board. This method is called for each new level. """

    zombies.empty()
    bullets.empty()
    ZombieCollection(settings, shooter, zombies)
    shooter.CenterShooter()
    InitializeBulletSettings(stats, settings)
    sleep(0.5)


def Play(bullets, display, mouse_x, mouse_y, play, settings, stats, shooter, zombies):
    # Requirement ID: 2.1.9
    """What to do when play button is pressed."""

    button_clicked = play.rect.collidepoint(mouse_x, mouse_y)

    # This calls all methods needed for the game.
    if button_clicked and not stats.game_active:
        stats.game_active = True
        settings.SetSpeed()
        stats.ResetScore()
        display.InitScore()
        display.Level()
        display.Shooters()
        display.Bullets()
        zombies.empty()
        bullets.empty()
        ZombieCollection(settings, shooter, zombies)
        shooter.CenterShooter()
