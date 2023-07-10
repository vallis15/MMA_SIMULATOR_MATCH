import random

import pygame

pygame.mixer.init()

def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

def generation_result(name1, name2):
    winner = random.choice([name1, name2])
    round = random.randint(1, 3)
    type_win = random.choice(["TKO", "Submise", "Body"])

    if type_win == "Body":
        round = 3

    result = f"Vítěz: {winner}\nVýhra: {type_win}\nKolo: {round}"
    return result