"""
Creating Buttons and assigning functions for each button. 

Author: Sufiyaan Nadeem
"""

import pygame
from Globals import *
from Scripts.GUI import *


class Buttons():
    def Play():
        Globals.scene = "Game"

    def Exit():
        pygame.mixer.music.stop()
        Globals.isRunning = False

    def Pause():
        Globals.scene = "Pause"

    def Home():
        pygame.mixer.music.unpause()
        Globals.scene = "Menu"


WIN_WIDTH = 1040
WIN_HEIGHT = 576
# Play Button
btnPlay = Menu.Button(text="Play", rect=(0, 0, 160, 60),
                      bg=UltraColor.Gray, fg=UltraColor.White, bgr=UltraColor.Green, tag=("Menu", None))
btnPlay.Left = WIN_WIDTH / 2 - (btnPlay.Width * 2 + 40) / 2
btnPlay.Top = WIN_HEIGHT - 80
btnPlay.Command = Buttons.Play


# Resume Button
btnResume = Menu.Button(text="Resume", rect=(0, 0, 160, 60),
                        bg=UltraColor.Gray, fg=UltraColor.White, bgr=UltraColor.Green, tag=("Pause", None))
btnResume.Left = WIN_WIDTH / 2 - btnResume.Width / 2 - 170
btnResume.Top = WIN_HEIGHT - 80
btnResume.Command = Buttons.Play


#   Could be simpligied by doing parameters in other class
btnExit = Menu.Button(text="Exit", rect=(0, 0, 160, 60), bg=UltraColor.Gray,
                      fg=UltraColor.White, bgr=UltraColor.Green, tag=("Menu", None))
btnExit.Left = btnPlay.Left + 200
btnExit.Top = btnPlay.Top
btnExit.Command = Buttons.Exit

#   Could be simpligied by doing parameters in other class
btnExit2 = Menu.Button(text="Exit", rect=(0, 0, 160, 60), bg=UltraColor.Gray,
                       fg=UltraColor.White, bgr=UltraColor.Green, tag=("Pause", None))
btnExit2.Left = btnResume.Left + 200
btnExit2.Top = btnResume.Top
btnExit2.Command = Buttons.Exit

#   Could be simpligied by doing parameters in other class
btnExit3 = Menu.Button(text="Exit", rect=(0, 0, 160, 60), bg=UltraColor.Gray,
                       fg=UltraColor.White, bgr=UltraColor.Green, tag=("GameOver", None))
btnExit3.Left = WIN_WIDTH - 600 + 200
btnExit3.Top = WIN_HEIGHT - 300 + 30
btnExit3.Command = Buttons.Exit


# Pause Button
btnPause = Menu.Button(text="Pause", rect=(0, 0, 160, 60),
                       bg=UltraColor.Gray, fg=UltraColor.White, bgr=UltraColor.DarkBlue, tag=("Game", None))
btnPause.Left = WIN_WIDTH - (10 + btnPause.Width)
btnPause.Top = WIN_HEIGHT - 80
btnPause.Command = Buttons.Pause


# Home Button
btnHome = Menu.Button(text="Main Menu", rect=(0, 0, 160, 60),
                      bg=UltraColor.Gray, fg=UltraColor.White, bgr=UltraColor.Green, tag=("Pause", None))
btnHome.Left = btnExit2.Left + 200
btnHome.Top = btnExit2.Top
btnHome.Command = Buttons.Home
