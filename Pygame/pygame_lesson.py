import pygame
from blob import Blob

STARTING_BLUE_BLOBS = 50
STARTING_RED_BLOBS = 10
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (138, 43, 226)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()


class PurpleBlob(Blob):
    """docstring for GreenBlob"""
    def __init__(self, color, x_boundary, y_boundary, movement_range):
        super().__init__(color, x_boundary, y_boundary, movement_range)
        self.color = PURPLE


class RedBlob(Blob):
    """docstring for GreenBlob"""
    def __init__(self, color, x_boundary, y_boundary, movement_range):
        super().__init__(color, x_boundary, y_boundary, movement_range)
        self.color = RED


class GreenBlob(Blob):
    """docstring for GreenBlob"""
    def __init__(self, color, x_boundary, y_boundary, movement_range):
        super().__init__(color, x_boundary, y_boundary, movement_range)
        self.color = GREEN


def draw_env(blob_list):
    game_display.fill(WHITE)
    for blobs in blob_list:
        for blob_id, blob in blobs.items():
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
            blob.check_bounds()
    pygame.display.update()


def main():
    blue_blobs = dict(enumerate([PurpleBlob(BLUE, WIDTH, HEIGHT, (-1, 2)) for _ in
                                range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([RedBlob(RED, WIDTH, HEIGHT, (-1, 2)) for _ in
                                range(STARTING_RED_BLOBS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_env([blue_blobs, red_blobs])
        clock.tick(60)


if __name__ == "__main__":
    main()
