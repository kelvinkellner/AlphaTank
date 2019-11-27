# tutorial link: https://repl.it/talk/learn/Game-in-Python/21409
import pygame

# initialise pygame
pygame.init()

# Create our screen with a width and height
screen = pygame.display.set_mode((32*8, 32*8))
# Make our pygame clock
clock = pygame.time.Clock()

# Let's predefine some colors for clarity, these are easy on the eyes, and look good
DARK = (50, 50, 50)
LIGHT = (210, 210, 210)

# Let's make a rectangle, with x and y and width an height
rect = pygame.Rect((0, 0), (32, 32))
# Then make a surface with a width and height
surface = pygame.Surface((32, 32))
# And fill the surface with a color
surface.fill(LIGHT)

# Start our game loop
# YES, WE REALLY BE ON THAT 'while True' GANG HAHA
while True:
  # Let's set the clock's FPS to 60
  clock.tick(60)

# Now we can start the event loop
for event in pygame.event.get():
  # If the event type is QUIT
  if event.type == pygame.QUIT:
    # Then we end pygame
    pygame.quit()
    # And quit the program
    quit()

  # Otherwise, if a key is down
  elif event.type == pygame.KEYDOWN:
    # And that key is w
    if event.key == pygame.K_w:
      # Move the rectangle up
      rect.move_ip(0, -32)

    # And that key is s
    elif event.key == pygame.K_s:
      # Move the rectangle down
      rect.move_ip(0, 32)

    # And that key is a
    elif event.key == pygame.K_a:
      # Move the rectangle left
      rect.move_ip(-32, 0)

    # And that key is d
    elif event.key == pygame.K_d:
      # Move the rectangle right
      rect.move_ip(32, 0)

# Clear the screen by filling it
screen.fill(DARK)
# Then blit (add to the buffer) our surface with our rectangle on
screen.blit(surface, rect)
# Then update the display to show the buffer
pygame.display.update()