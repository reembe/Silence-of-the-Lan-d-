import pygame
import math

# this class is for the small enemies in the game


# the code below initializes the object in the Mini class. It uses the number variable to determine what image the monster will have.

class Mini:
   def __init__(self, x, y, number):
       self.x = x
       self.y = y
       if number == 1:
           self.image_list = ["small1.gif"]
       if number == 2:
           self.image_list = ["small2.gif"]
       if number == 3:
           self.image_list = ["small3.gif"]
       if number == 4:
           self.image_list = ["small4.gif"]
       if number == 5:
        self.image_list = ["small5.gif"]
       self.image = pygame.image.load(self.image_list[0])
       self.rescale_image(self.image)
       self.image_size = self.image.get_size()
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
       self.delta = 1
       self.image_idx = 0
       self.mask = pygame.mask.from_surface(self.image)

# the code below rescales the image of the object

   def rescale_image(self, image):
       self.image_size = self.image.get_size()
       scale_size = (self.image_size[0] * .7, self.image_size[1] * .7)
       self.image = pygame.transform.scale(self.image, scale_size)

# the code below resets the object to any location

   def reset_mini(self, x, y):
       self.x = x
       self.y = y
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

# the code below has the enemy follow the player by taking the players coordinates and figuring out the distance between the two and
   # having the enemies x and ys increase by the ammount needed to bring them together

   def go_to_player(self, player):
       if self.x == -10000 and self.y == -10000:
           dir_x = -1000
           dir_y = -1000
       else:
           dir_x, dir_y = player.rect.x - self.rect.x, player.rect.y - self.rect.y
           dist = math.hypot(dir_x, dir_y)
           if dist != 0:
               dir_x, dir_y = dir_x / dist, dir_y / dist
           self.rect.x += dir_x * self.delta
           self.rect.y += dir_y * self.delta

