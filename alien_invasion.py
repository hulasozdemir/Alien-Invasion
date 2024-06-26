import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
    
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        # Main Loop
        while True:
            self._check_events()
            self._update_screen()    
            self.ship.update()
            self.bullets.update()
            self.clock.tick(60)

            # Destroy the out of screen bullets
            for bullet in self.bullets:
                if bullet.rect.bottom < 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))

            

    def _check_events(self) -> None:
        # Check for user input and respond
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
                
    
    def _update_screen(self) -> None:
        # Update the screen properties
        

        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.ship.blitme()
        pygame.display.flip()
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet(event)
        elif event.key == pygame.K_q:
            sys.exit()
        

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self, event):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
         

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()