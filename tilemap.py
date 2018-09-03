import pygame as PY


class map:
    def __init__(self, filename):
        self.map_data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.map_data.append(line)
    self.tilewidth
