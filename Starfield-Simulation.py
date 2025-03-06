import pygame
import random

# Window setting
Width, Height = 800, 800
NUM_Stars = 2500

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((Width, Height))

class Star:
    def __init__(self):
        self.x = random.uniform(-Width // 2, Width // 2)
        self.y = random.uniform(-Height // 2, Height // 2)
        self.z = random.uniform(1, Width // 2)  # Depth 
        self.pz = self.z  # Store the initial depth (Motion effect)

    def update(self):
        self.z -= 2.5  # Speed of the star
        # Reset star's position  
        if self.z < 1:
            self.x = random.uniform(-Width // 2, Width // 2)
            self.y = random.uniform(-Height // 2, Height // 2)
            self.z = Width // 2
            self.pz = self.z  # Reset depth

    def show(self, screen):
        # Convert 3D to 2D position
        sx = int((self.x / self.z) * Width) + Width // 2
        sy = int((self.y / self.z) * Height) + Height // 2

        # Speed trail effect
        px = int((self.x / self.pz) * Width) + Width // 2
        py = int((self.y / self.pz) * Height) + Height // 2

        self.pz = self.z  # Update depth

        # Draw Motion effect
        pygame.draw.line(screen, (255,255,255), (px, py), (sx, sy))

# List of stars
stars = [Star() for _ in range(NUM_Stars)]

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and render each star
    for star in stars:
        star.update()
        star.show(screen)

    pygame.display.flip()

pygame.quit()
