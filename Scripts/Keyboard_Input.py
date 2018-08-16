"""
Key Input Handler that decides what variables to set true depending on what keys are pressed.

Author: Sufiyaan Nadeem
"""

import pygame
from Globals import *


def KeyInput_Handler(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            Globals.isRunning = False
        if event.key == pygame.K_UP:
            Globals.up = True
        if event.key == pygame.K_DOWN:
            Globals.down = True
        if event.key == pygame.K_LEFT:
            Globals.left = True
        if event.key == pygame.K_RIGHT:
            Globals.right = True
        if event.key == pygame.K_z:
            Globals.attack = True
        if event.key == pygame.K_p and Globals.scene == "Game":
            Globals.scene = "Pause"
        if event.key == pygame.K_p and Globals.scene == "Pause":
            if Globals.pause_counter >= 10:
                Globals.scene = "Game"
        if event.key == pygame.K_q and Globals.scene == "Game":
            Globals.scene = "Menu"
        if event.key == pygame.K_q and Globals.scene == "Menu":
            if Globals.menu_counter >= 10:
                Globals.scene = "Game"
        if event.key == pygame.K_SPACE:
            Globals.scene = "Game"

    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            Globals.up = False
        if event.key == pygame.K_DOWN:
            Globals.down = False
        if event.key == pygame.K_RIGHT:
            Globals.right = False
        if event.key == pygame.K_LEFT:
            Globals.left = False
        if event.key == pygame.K_z:
            Globals.attack = False
        if event.key == pygame.K_p:
            Globals.pause_counter = 0
        if event.key == pygame.K_q:
            Globals.menu_counter = 0
