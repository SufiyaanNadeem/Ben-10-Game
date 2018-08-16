"""
Loading Game Objects Sprites from specified spritesheets, resizing them, and adding them to variables.

The SpriteSheets Below were created by subvercetti - spriters-resource

Author: Sufiyaan Nadeem
"""

import pygame

WIN_WIDTH = 1040
WIN_HEIGHT = 576


class GameObject_Sprites:

    spritesheet = pygame.image.load(
        "Graphics/Watch_SpriteSheet.png")

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-4, -6))
    image = pygame.transform.scale(image, (81, 81))
    Watch_1 = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-89, -6))
    image = pygame.transform.scale(image, (81, 81))
    Watch_2 = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-177, -6))
    image = pygame.transform.scale(image, (81, 81))
    Watch_3 = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-265, -6))
    image = pygame.transform.scale(image, (81, 81))
    Watch_4 = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-352, -6))
    image = pygame.transform.scale(image, (81, 81))
    Watch_5 = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-507, -7))
    image = pygame.transform.scale(image, (81, 81))
    Wildmutt = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-596, -7))
    image = pygame.transform.scale(image, (81, 81))
    Fourarms = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-683, -7))
    image = pygame.transform.scale(image, (81, 81))
    Heatblast = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-771, -7))
    image = pygame.transform.scale(image, (81, 81))
    XLR8 = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-859, -7))
    image = pygame.transform.scale(image, (81, 81))
    Ghostfreak = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-507, -95))
    image = pygame.transform.scale(image, (81, 81))
    Ripjaws = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-596, -95))
    image = pygame.transform.scale(image, (81, 81))
    Stinkfly = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-683, -95))
    image = pygame.transform.scale(image, (81, 81))
    GreyMatter = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-771, -95))
    image = pygame.transform.scale(image, (81, 81))
    Diamondhead = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-859, -95))
    image = pygame.transform.scale(image, (81, 81))
    Upgrade = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-7, -95))
    image = pygame.transform.scale(image, (81, 81))
    Wildmutt_Ready = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-7, -174))
    image = pygame.transform.scale(image, (81, 81))
    Fourarms_Ready = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-7, -257))
    image = pygame.transform.scale(image, (81, 81))
    Heatblast_Ready = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-7, -418))
    image = pygame.transform.scale(image, (81, 81))
    Ghostfreak_Ready = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-7, -337))
    image = pygame.transform.scale(image, (81, 81))
    XLR8_Ready = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-255, -95))
    image = pygame.transform.scale(image, (81, 81))
    Ripjaws_Ready = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-255, -175))
    image = pygame.transform.scale(image, (81, 81))
    Stinkfly_Ready = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-255, -254))
    image = pygame.transform.scale(image, (81, 81))
    GreyMatter_Ready = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-258, -336))
    image = pygame.transform.scale(image, (81, 81))
    Diamondhead_Ready = image

    image = pygame.Surface((81, 81), pygame.SRCALPHA)
    image.blit(spritesheet, (-257, -419))
    image = pygame.transform.scale(image, (81, 81))
    Upgrade_Ready = image

    image = pygame.image.load("Graphics/DoorReady.png")
    image = pygame.transform.scale(image, (116, 192))
    Door_Ready = image

    image = pygame.image.load("Graphics/DoorOpen.png")
    image = pygame.transform.scale(image, (116, 192))
    Door_Open = image

    image = pygame.image.load("Graphics/GoldKey.png")
    image = pygame.transform.scale(image, (64, 49))
    Door_Key = image

    spritesheet = pygame.image.load(
        "Graphics\\Heart_SpriteSheet.png")
    image = pygame.Surface((194, 176), pygame.SRCALPHA)
    image.blit(spritesheet, (0, 0))
    image = pygame.transform.scale(image, (int(194 / 3), int(176 / 3)))
    Heart_1 = image

    image = pygame.Surface((195, 176), pygame.SRCALPHA)
    image.blit(spritesheet, (-221, 17))
    image = pygame.transform.scale(image, (int(195 / 3), int(176 / 3)))
    Heart_2 = image
    image = pygame.image.load("Graphics/Instructions.png")
    Instructions = image

    image = pygame.image.load("Graphics/Fourarms_Stats.png")
    Fourarms_Stats = image

    image = pygame.image.load("Graphics/Wildmutt_Stats.png")
    Wildmutt_Stats = image

    image = pygame.image.load("Graphics/Heatblast_Stats.png")
    Heatblast_Stats = image

    image = pygame.image.load("Graphics/XLR8_Stats.png")
    XLR8_Stats = image

    image = pygame.image.load("Graphics/Ghostfreak_Stats.png")
    Ghostfreak_Stats = image

    image = pygame.image.load("Graphics/Ripjaws_Stats.png")
    Ripjaws_Stats = image

    image = pygame.image.load("Graphics/Stinkfly_Stats.png")
    Stinkfly_Stats = image

    image = pygame.image.load("Graphics/Greymatter_Stats.png")
    Greymatter_Stats = image

    image = pygame.image.load("Graphics/Diamondhead_Stats.png")
    Diamondhead_Stats = image

    image = pygame.image.load("Graphics/Upgrade_Stats.png")
    Upgrade_Stats = image

    Home_Screen_temp = pygame.image.load("Graphics\\Home_Screen.png")
    Home_Screen_temp = pygame.transform.scale(
        Home_Screen_temp, (WIN_WIDTH, WIN_HEIGHT))
    Home_Screen_img = pygame.Surface(
        Home_Screen_temp.get_size(), pygame.HWSURFACE)
    Home_Screen_img.blit(Home_Screen_temp, (0, 0))
    del Home_Screen_temp

    Game_Over_temp = pygame.image.load("Graphics\\GameOver_1.png")
    Game_Over_temp = pygame.transform.scale(
        Game_Over_temp, (WIN_WIDTH, WIN_HEIGHT))
    Game_Over_img = pygame.Surface(Game_Over_temp.get_size(), pygame.HWSURFACE)
    Game_Over_img.blit(Game_Over_temp, (0, 0))
    del Game_Over_temp

    Background_temp = pygame.image.load("Graphics\\Background_1.jpg")
    Background_1 = pygame.Surface(
        Background_temp.get_size(), pygame.HWSURFACE)
    Background_1.blit(Background_temp, (0, 0))

    Background_temp = pygame.image.load("Graphics\\Background_2.jpg")
    Background_temp = pygame.transform.scale(
        Background_temp, (WIN_WIDTH, WIN_HEIGHT))
    Background_2 = pygame.Surface(
        Background_temp.get_size(), pygame.HWSURFACE)
    Background_2.blit(Background_temp, (0, 0))

    Background_temp = pygame.image.load("Graphics\\Background_3.jpg")
    Background_temp = pygame.transform.scale(
        Background_temp, (WIN_WIDTH, WIN_HEIGHT))
    Background_3 = pygame.Surface(
        Background_temp.get_size(), pygame.HWSURFACE)
    Background_3.blit(Background_temp, (0, 0))
