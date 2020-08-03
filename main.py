import pygame
import os

ing_path = os.path.join('player.png')

class character(object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    character.image = pygame.image.load ('player.png')
    self.image = character.image
    self.image = pygame.transform.scale(self.image(50,50)
    

     self.hitbox(self.x.self.y,55,55)
   def draw(self,surface):
     surface.blit(self.image,(self.image.x,self.y))

pygame.init()
while running:
    if event.type == pygame.QUIT
      pygame.quit()
      running = False
    screen.((255,255,255))
    Sprite.draw(screen)
    pygame.display.update()
  clock.tick(60)  
  if key[pygame.K_LEFT] and self.x > 0:

