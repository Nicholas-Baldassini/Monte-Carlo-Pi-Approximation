import pygame
import random

pygame.init()
size = 500
screen = pygame.display.set_mode((size, size))

circle_points = 0
total_points = 1


def draw_circle() -> None:
    """
    Draw the circle outline on the screen
    """
    pygame.draw.circle(screen, (255, 255, 255), (int(size/2), int(size/2)),
                       int(size/2), width=1)


def generate_points() -> None:
    """
    Generate the random points on the screen, approximate pi and print it
    """
    global circle_points
    global total_points
    while True:
        x = random.uniform(0, size)
        y = random.uniform(0, size)
        if ((x-(size/2))**2) + ((y - (size/2))**2) <= (size/2)**2:
            pygame.draw.circle(screen, (0, 255, 0), (int(x), int(y)), 1)
            circle_points += 1
        else:
            pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), 1)

        total_points += 1

        # Print every 100 points
        if circle_points % 100 == 0:
            print(4*(circle_points/total_points))
        pygame.display.update()


if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill((0, 0, 0))
        draw_circle()
        generate_points()
