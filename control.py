import pygame

def refreshEscape():
    done = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    return done

def waitClick():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                done = True
