"""
Loading Enemy Sprites from specified spritesheets, resizing them, and adding them to variables.
This file also loads in the Boss's projectile.

The SpriteSheets Below were created by dragonrod342 - DeviantArt

Author: Sufiyaan Nadeem
"""

import pygame


class Enemy_Sprites:
    spritesheet = pygame.image.load(
        "Graphics/Megawatt_SpriteSheet.png")

    character = pygame.Surface((14, 20), pygame.SRCALPHA)
    character.blit(spritesheet, (-10, -18))
    character = pygame.transform.scale(character, (14 * 4, 20 * 4))
    Megawatt_Idle1 = character

    character = pygame.Surface((14, 20), pygame.SRCALPHA)
    character.blit(spritesheet, (-26, -18))
    character = pygame.transform.scale(character, (14 * 4, 20 * 4))
    Megawatt_Idle2 = character

    character = pygame.Surface((14, 20), pygame.SRCALPHA)
    character.blit(spritesheet, (-42, -18))
    character = pygame.transform.scale(character, (14 * 4, 20 * 4))
    Megawatt_Idle3 = character

    character = pygame.Surface((14, 20), pygame.SRCALPHA)
    character.blit(spritesheet, (-57, -18))
    character = pygame.transform.scale(character, (14 * 4, 20 * 4))
    Megawatt_Idle4 = character

    character = pygame.Surface((17, 18), pygame.SRCALPHA)
    character.blit(spritesheet, (-12, -58))
    character = pygame.transform.scale(character, (17 * 4, 18 * 4))
    Megawatt_Fly1 = character

    character = pygame.Surface((17, 18), pygame.SRCALPHA)
    character.blit(spritesheet, (-31, -58))
    character = pygame.transform.scale(character, (17 * 4, 18 * 4))
    Megawatt_Fly2 = character

    character = pygame.Surface((17, 18), pygame.SRCALPHA)
    character.blit(spritesheet, (-50, -58))
    character = pygame.transform.scale(character, (17 * 4, 18 * 4))
    Megawatt_Fly3 = character

    character = pygame.Surface((17, 18), pygame.SRCALPHA)
    character.blit(spritesheet, (-70, -58))
    character = pygame.transform.scale(character, (17 * 4, 18 * 4))
    Megawatt_Fly4 = character

    character = pygame.Surface((18, 18), pygame.SRCALPHA)
    character.blit(spritesheet, (-185, -223))
    character = pygame.transform.scale(character, (18 * 4, 18 * 4))
    Megawatt_Fall = character

    character = pygame.Surface((18, 20), pygame.SRCALPHA)
    character.blit(spritesheet, (-15, -281))
    character = pygame.transform.scale(character, (18 * 4, 20 * 4))
    Megawatt_Dead1 = character

    character = pygame.Surface((18, 20), pygame.SRCALPHA)
    character.blit(spritesheet, (-45, -281))
    character = pygame.transform.scale(character, (18 * 4, 20 * 4))
    Megawatt_Dead2 = character

    character = pygame.Surface((18, 20), pygame.SRCALPHA)
    character.blit(spritesheet, (-73, -281))
    character = pygame.transform.scale(character, (18 * 4, 20 * 4))
    Megawatt_Dead3 = character

    spritesheet = pygame.image.load(
        "Graphics/Wolf_SpriteSheet.png")

    character = pygame.Surface((56, 58), pygame.SRCALPHA)
    character.blit(spritesheet, (-7, -20))
    character = pygame.transform.scale(character, (56 * 3, 58 * 3))
    Wolf_Idle1 = character

    character = pygame.Surface((54, 58), pygame.SRCALPHA)
    character.blit(spritesheet, (-68, -20))
    character = pygame.transform.scale(character, (54 * 3, 58 * 3))
    Wolf_Idle2 = character

    character = pygame.Surface((60, 58), pygame.SRCALPHA)
    character.blit(spritesheet, (-133, -20))
    character = pygame.transform.scale(character, (60 * 3, 58 * 3))
    Wolf_Idle3 = character

    character = pygame.Surface((63, 58), pygame.SRCALPHA)
    character.blit(spritesheet, (-204, -20))
    character = pygame.transform.scale(character, (63 * 3, 58 * 3))
    Wolf_Idle4 = character

    character = pygame.Surface((82, 58), pygame.SRCALPHA)
    character.blit(spritesheet, (-7, -88))
    character = pygame.transform.scale(character, (82 * 3, 58 * 3))
    Wolf_Walk1 = character

    character = pygame.Surface((90, 58), pygame.SRCALPHA)
    character.blit(spritesheet, (-94, -88))
    character = pygame.transform.scale(character, (90 * 3, 58 * 3))
    Wolf_Walk2 = character

    character = pygame.Surface((75, 58), pygame.SRCALPHA)
    character.blit(spritesheet, (-189, -88))
    character = pygame.transform.scale(character, (75 * 3, 58 * 3))
    Wolf_Walk3 = character

    character = pygame.Surface((71, 58), pygame.SRCALPHA)
    character.blit(spritesheet, (-269, -88))
    character = pygame.transform.scale(character, (71 * 3, 58 * 3))
    Wolf_Walk4 = character

    character = pygame.Surface((54, 62), pygame.SRCALPHA)
    character.blit(spritesheet, (-9, -178))
    character = pygame.transform.scale(character, (54 * 3, 62 * 3))
    Wolf_Jump = character

    character = pygame.Surface((35, 58), pygame.SRCALPHA)
    character.blit(spritesheet, (-78, -182))
    character = pygame.transform.scale(character, (35 * 3, 58 * 3))
    Wolf_Fall = character

    character = pygame.Surface((55, 58), pygame.SRCALPHA)
    character.blit(spritesheet, (-6, -276))
    character = pygame.transform.scale(character, (55 * 3, 58 * 3))
    Wolf_Attack1 = character

    character = pygame.Surface((58, 58), pygame.SRCALPHA)
    character.blit(spritesheet, (-71, -276))
    character = pygame.transform.scale(character, (58 * 3, 58 * 3))
    Wolf_Attack2 = character

    character = pygame.Surface((63, 58), pygame.SRCALPHA)
    character.blit(spritesheet, (-143, -276))
    character = pygame.transform.scale(character, (63 * 3, 58 * 3))
    Wolf_Attack3 = character

    character = pygame.Surface((64, 58), pygame.SRCALPHA)
    character.blit(spritesheet, (-218, -276))
    character = pygame.transform.scale(character, (64 * 3, 58 * 3))
    Wolf_Attack4 = character

    character = pygame.Surface((57, 67), pygame.SRCALPHA)
    character.blit(spritesheet, (-15, -362))
    character = pygame.transform.scale(character, (57 * 3, 67 * 3))
    Wolf_Scratch1 = character

    character = pygame.Surface((67, 67), pygame.SRCALPHA)
    character.blit(spritesheet, (-84, -362))
    character = pygame.transform.scale(character, (67 * 3, 67 * 3))
    Wolf_Scratch2 = character

    character = pygame.Surface((59, 67), pygame.SRCALPHA)
    character.blit(spritesheet, (-173, -362))
    character = pygame.transform.scale(character, (59 * 3, 67 * 3))
    Wolf_Scratch3 = character

    character = pygame.Surface((58, 67), pygame.SRCALPHA)
    character.blit(spritesheet, (-258, -362))
    character = pygame.transform.scale(character, (58 * 3, 67 * 3))
    Wolf_Scratch4 = character

    character = pygame.Surface((56, 58), pygame.SRCALPHA)
    character.blit(spritesheet, (-283, -20))
    character = pygame.transform.scale(character, (56 * 3, 58 * 3))
    Wolf_Dead = character

    character = pygame.Surface((61, 39), pygame.SRCALPHA)
    character.blit(spritesheet, (-260, -548))
    character = pygame.transform.scale(character, (61 * 3, 39 * 3))
    Wave_Shoot = character
