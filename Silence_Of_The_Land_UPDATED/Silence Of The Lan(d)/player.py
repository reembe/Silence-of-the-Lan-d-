import pygame

# this class is for the player's character

class Player:
   def __init__(self, x, y):
       self.x = x
       self.y = y
       self.image = pygame.image.load("idle_down.png")
       self.rescale_image(self.image)
       self.image_size = self.image.get_size()
       self.rect = pygame.Rect(self.x, self.y, self.image_size[0] * 5, self.image_size[1] * 5)
       self.delta = 4

   # the code below rescales the image of the object

   def rescale_image(self, image):
       self.image_size = self.image.get_size()
       scale_size = (self.image_size[0] * .7, self.image_size[1] * .7)
       self.image = pygame.transform.scale(self.image, scale_size)

# the code below uses userinput to move the player in a certain direction and change the sprite according to the direction
   
   def move_player(self, d):
       if d == "down" and self.y < 900:
           self.y = self.y + self.delta
           self.image = pygame.image.load("down_0.png")
           self.rescale_image(self.image)
           self.image_size = self.image.get_size()
           self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
       elif d == "up" and self.y > 900:
           self.y = self.y - self.delta
           self.image = pygame.image.load("up_0.png")
           self.rescale_image(self.image)
           self.image_size = self.image.get_size()
           self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
       elif d == "left" and self.x > 0:
           self.x = self.x - self.delta
           self.image = pygame.image.load("left_0.png")
           self.rescale_image(self.image)
           self.image_size = self.image.get_size()
           self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
       elif d == "right" and self.x < 1900:
           self.x = self.x + self.delta
           self.image = pygame.image.load("right_0.png")
           self.rescale_image(self.image)
           self.image_size = self.image.get_size()
           self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

   # the code below uses userinput when the player chooses to attack to change the sprite into one of the player attacking based on the direction

   def player_attack(self, d):
      if d == "down" and self.y < 1000:
          self.image = pygame.image.load("attack_down.png")
          self.rescale_image(self.image)
          self.image_size = self.image.get_size()
          self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
      elif d == "up" and self.y > 0:
          self.image = pygame.image.load("attack_up.png")
          self.rescale_image(self.image)
          self.image_size = self.image.get_size()
          self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
      elif d == "left" and self.x > 0:
          self.image = pygame.image.load("attack_left.png")
          self.rescale_image(self.image)
          self.image_size = self.image.get_size()
          self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
      elif d == "right" and self.x < 1000:
          self.image = pygame.image.load("attack_right.png")
          self.rescale_image(self.image)
          self.image_size = self.image.get_size()
          self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])




