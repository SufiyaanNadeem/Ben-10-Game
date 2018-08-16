"""
Loading Projectile Object Sprites from specified spritesheets, resizing them, and adding them to variables.

The SpriteSheets Below were created by subvercetti - spriters-resource and dragonrod342 - DeviantArt

Author: Sufiyaan Nadeem
"""
import pygame


class Projectile_Sprites:
    spritesheet = pygame.image.load(
        "Graphics\\Upgrade_SpriteSheet.png")
    character = pygame.Surface((63, 13), pygame.SRCALPHA)
    character.blit(spritesheet, (-593, -236))
    character = pygame.transform.scale(character, (63 * 2, 13 * 2))
    Beam_Shot = character

    spritesheet = pygame.image.load(
        "Graphics\\Diamondhead_SpriteSheet.png")
    character = pygame.Surface((14, 10), pygame.SRCALPHA)
    character.blit(spritesheet, (-336, -502))
    character = pygame.transform.scale(character, (14 * 3, 10 * 3))
    Diamond1 = character

    character = pygame.Surface((25, 35), pygame.SRCALPHA)
    character.blit(spritesheet, (-360, -477))
    character = pygame.transform.scale(character, (25 * 3, 35 * 3))
    Diamond2 = character

    character = pygame.Surface((41, 65), pygame.SRCALPHA)
    character.blit(spritesheet, (-392, -447))
    character = pygame.transform.scale(character, (41 * 3, 65 * 3))
    Diamond3 = character

    character = pygame.Surface((60, 108), pygame.SRCALPHA)
    character.blit(spritesheet, (-440, -404))
    character = pygame.transform.scale(character, (60 * 3, 108 * 3))
    Diamond4 = character

    spritesheet = pygame.image.load(
        "Graphics\\Heatblast_SpriteSheet.png")
    character = pygame.Surface((14, 14), pygame.SRCALPHA)
    character.blit(spritesheet, (-255, -318))
    character = pygame.transform.scale(character, (14 * 3, 14 * 3))
    Fireball_Spin1 = character

    character = pygame.Surface((14, 14), pygame.SRCALPHA)
    character.blit(spritesheet, (-272, -318))
    character = pygame.transform.scale(character, (14 * 3, 14 * 3))
    Fireball_Spin2 = character

    character = pygame.Surface((14, 14), pygame.SRCALPHA)
    character.blit(spritesheet, (-289, -318))
    character = pygame.transform.scale(character, (14 * 3, 14 * 3))
    Fireball_Spin3 = character

    character = pygame.Surface((14, 14), pygame.SRCALPHA)
    character.blit(spritesheet, (-306, -318))
    character = pygame.transform.scale(character, (14 * 3, 14 * 3))
    Fireball_Spin4 = character

    spritesheet = pygame.image.load(
        "Graphics\\Stinkfly_SpriteSheet.png")
    character = pygame.Surface((36, 12), pygame.SRCALPHA)
    character.blit(spritesheet, (-657, -237))
    character = pygame.transform.scale(character, (36 * 2, 12 * 2))
    Stink_Shoot = character

    spritesheet = pygame.image.load(
        "Graphics\\Ghostfreak_SpriteSheet.png")
    character = pygame.Surface((36, 78), pygame.SRCALPHA)
    character.blit(spritesheet, (-110, -237))
    character = pygame.transform.scale(character, (36 * 2, 78 * 2))
    Wind_Blow1 = character

    character = pygame.Surface((61, 78), pygame.SRCALPHA)
    character.blit(spritesheet, (-172, -233))
    character = pygame.transform.scale(character, (61 * 2, 78 * 2))
    Wind_Blow2 = character

    character = pygame.Surface((63, 78), pygame.SRCALPHA)
    character.blit(spritesheet, (-254, -234))
    character = pygame.transform.scale(character, (63 * 2, 78 * 2))
    Wind_Blow3 = character

    character = pygame.Surface((68, 78), pygame.SRCALPHA)
    character.blit(spritesheet, (-337, -232))
    character = pygame.transform.scale(character, (68 * 2, 78 * 2))
    Wind_Blow4 = character

    character = pygame.Surface((69, 78), pygame.SRCALPHA)
    character.blit(spritesheet, (-429, -233))
    character = pygame.transform.scale(character, (69 * 2, 78 * 2))
    Wind_Blow5 = character

    character = pygame.Surface((68, 78), pygame.SRCALPHA)
    character.blit(spritesheet, (-519, -233))
    character = pygame.transform.scale(character, (68 * 2, 78 * 2))
    Wind_Blow6 = character
