"""
Loading Player Sprites from specified spritesheets, resizing them, and adding them to variables.

The SpriteSheets Below were created by subvercetti - spriters-resource and dragonrod342 - DeviantArt

Author: Sufiyaan Nadeem
"""

import pygame


class Player_Sprites:
    spritesheet = pygame.image.load(
        "Graphics\\Ben_SpriteSheet2.png")

    character = pygame.Surface((31, 53), pygame.SRCALPHA)
    character.blit(spritesheet, (-394, -14))
    character = pygame.transform.scale(character, (28 * 3, 48 * 3))
    Ben_Idle1 = character

    character = pygame.Surface((31, 53), pygame.SRCALPHA)
    character.blit(spritesheet, (-440, -12))
    character = pygame.transform.scale(character, (28 * 3, 48 * 3))
    Ben_Idle2 = character

    character = pygame.Surface((32, 53), pygame.SRCALPHA)
    character.blit(spritesheet, (-484, -12))
    character = pygame.transform.scale(character, (29 * 3, 48 * 3))
    Ben_Idle3 = character

    character = pygame.Surface((32, 53), pygame.SRCALPHA)
    character.blit(spritesheet, (-524, -11))
    character = pygame.transform.scale(character, (29 * 3, 48 * 3))
    Ben_Idle4 = character

    character = pygame.Surface((31, 48), pygame.SRCALPHA)
    character.blit(spritesheet, (-386, -83))
    character = pygame.transform.scale(character, (31 * 3, 48 * 3))
    Ben_Walk1 = character

    character = pygame.Surface((41, 48), pygame.SRCALPHA)
    character.blit(spritesheet, (-426, -83))
    character = pygame.transform.scale(character, (41 * 3, 48 * 3))
    Ben_Walk2 = character

    character = pygame.Surface((40, 48), pygame.SRCALPHA)
    character.blit(spritesheet, (-470, -83))
    character = pygame.transform.scale(character, (40 * 3, 48 * 3))
    Ben_Walk3 = character

    character = pygame.Surface((32, 48), pygame.SRCALPHA)
    character.blit(spritesheet, (-518, -83))
    character = pygame.transform.scale(character, (32 * 3, 48 * 3))
    Ben_Walk4 = character

    character = pygame.Surface((33, 48), pygame.SRCALPHA)
    character.blit(spritesheet, (-556, -83))
    character = pygame.transform.scale(character, (33 * 3, 48 * 3))
    Ben_Walk5 = character

    character = pygame.Surface((39, 48), pygame.SRCALPHA)
    character.blit(spritesheet, (-596, -83))
    character = pygame.transform.scale(character, (39 * 3, 48 * 3))
    Ben_Walk6 = character

    character = pygame.Surface((38, 48), pygame.SRCALPHA)
    character.blit(spritesheet, (-641, -83))
    character = pygame.transform.scale(character, (38 * 3, 48 * 3))
    Ben_Walk7 = character

    character = pygame.Surface((30, 48), pygame.SRCALPHA)
    character.blit(spritesheet, (-689, -83))
    character = pygame.transform.scale(character, (30 * 3, 48 * 3))
    Ben_Walk8 = character

    character = pygame.Surface((34, 34), pygame.SRCALPHA)
    character.blit(spritesheet, (-384, -170))
    character = pygame.transform.scale(character, (34 * 3, 34 * 3))
    Ben_Jump1 = character

    character = pygame.Surface((39, 50), pygame.SRCALPHA)
    character.blit(spritesheet, (-440, -154))
    character = pygame.transform.scale(character, (39 * 3, 50 * 3))
    Ben_Jump2 = character

    character = pygame.Surface((34, 47), pygame.SRCALPHA)
    character.blit(spritesheet, (-503, -159))
    character = pygame.transform.scale(character, (34 * 3, 47 * 3))
    Ben_Jump3 = character

    character = pygame.Surface((31, 52), pygame.SRCALPHA)
    character.blit(spritesheet, (-387, -218))
    character = pygame.transform.scale(character, (29 * 3, 48 * 3))
    Ben_Punch1 = character

    character = pygame.Surface((41, 52), pygame.SRCALPHA)
    character.blit(spritesheet, (-432, -217))
    character = pygame.transform.scale(character, (38 * 3, 48 * 3))
    Ben_Punch2 = character

    character = pygame.Surface((47, 52), pygame.SRCALPHA)
    character.blit(spritesheet, (-481, -216))
    character = pygame.transform.scale(character, (43 * 3, 48 * 3))
    Ben_Punch3 = character

    character = pygame.Surface((31, 51), pygame.SRCALPHA)
    character.blit(spritesheet, (-308, -16))
    character = pygame.transform.scale(character, (28 * 3, 48 * 3))
    Ben_Dead = character

    character = pygame.Surface((31, 51), pygame.SRCALPHA)
    character.blit(spritesheet, (-350, -16))
    character = pygame.transform.scale(character, (28 * 3, 48 * 3))
    Ben_Transform = character


    spritesheet = pygame.image.load(
        "Graphics\\Wildmutt_SpriteSheet2.png")



    character = pygame.Surface((55,43),pygame.SRCALPHA)
    character.blit(spritesheet,(-45,-15))
    character = pygame.transform.scale(character, (49*3,38*3))
    Wildmutt_Idle1 = character

    character = pygame.Surface((55,43),pygame.SRCALPHA)
    character.blit(spritesheet,(-121,-15))
    character = pygame.transform.scale(character, (49*3,38*3))
    Wildmutt_Idle2 = character

    character = pygame.Surface((48,38),pygame.SRCALPHA)
    character.blit(spritesheet,(-16,-427))
    character = pygame.transform.scale(character, (48*3,38*3))
    Wildmutt_Walk1 = character

    character = pygame.Surface((56,38),pygame.SRCALPHA)
    character.blit(spritesheet,(-70,-426))
    character = pygame.transform.scale(character, (56*3,38*3))
    Wildmutt_Walk2 = character

    character = pygame.Surface((65,38),pygame.SRCALPHA)
    character.blit(spritesheet,(-135,-424))
    character = pygame.transform.scale(character, (65*3,38*3))
    Wildmutt_Walk3 = character

    character = pygame.Surface((62,38),pygame.SRCALPHA)
    character.blit(spritesheet,(-367,-429))
    character = pygame.transform.scale(character, (62*3,38*3))
    Wildmutt_Walk4 = character

    character = pygame.Surface((48,38),pygame.SRCALPHA)
    character.blit(spritesheet,(-437,-430))
    character = pygame.transform.scale(character, (48*3,38*3))
    Wildmutt_Walk5 = character

    character = pygame.Surface((64,40),pygame.SRCALPHA)
    character.blit(spritesheet,(-23,-367))
    character = pygame.transform.scale(character, (64*3,40*3))
    Wildmutt_Jump1 = character

    character = pygame.Surface((63,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-132,-367))
    character = pygame.transform.scale(character, (63*3,42*3))
    Wildmutt_Jump2 = character



    character = pygame.Surface((48,39),pygame.SRCALPHA)
    character.blit(spritesheet,(-228,-375))
    character = pygame.transform.scale(character, (47*3,38*3))
    Wildmutt_Jump3 = character

    character = pygame.Surface((56,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-192,-17))
    character = pygame.transform.scale(character, (49*3,38*3))
    Wildmutt_Transform = character

    character = pygame.Surface((55,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-259,-18))
    character = pygame.transform.scale(character, (49*3,38*3))
    Wildmutt_Dead = character


    character = pygame.Surface((64,40),pygame.SRCALPHA)
    character.blit(spritesheet,(-72,-489))
    character = pygame.transform.scale(character, (61*3,38*3))
    Wildmutt_Roll1 = character

    character = pygame.Surface((45,45),pygame.SRCALPHA)
    character.blit(spritesheet,(-145,-486))
    character = pygame.transform.scale(character, (38*3,38*3))
    Wildmutt_Roll2 = character

    character = pygame.Surface((38,45),pygame.SRCALPHA)
    character.blit(spritesheet,(-202,-486))
    character = pygame.transform.scale(character, (32*3,38*3))
    Wildmutt_Roll3 = character

    character = pygame.Surface((40,45),pygame.SRCALPHA)
    character.blit(spritesheet,(-252,-486))
    character = pygame.transform.scale(character, (34*3,38*3))
    Wildmutt_Roll4 = character

    character = pygame.Surface((44,45),pygame.SRCALPHA)
    character.blit(spritesheet,(-308,-486))
    character = pygame.transform.scale(character, (37*3,38*3))
    Wildmutt_Roll5 = character

    character = pygame.Surface((44,45),pygame.SRCALPHA)
    character.blit(spritesheet,(-362,-486))
    character = pygame.transform.scale(character, (37*3,38*3))
    Wildmutt_Roll6 = character

    character = pygame.Surface((38,45),pygame.SRCALPHA)
    character.blit(spritesheet,(-420,-486))
    character = pygame.transform.scale(character, (32*3,38*3))
    Wildmutt_Roll7 = character

    character = pygame.Surface((40,45),pygame.SRCALPHA)
    character.blit(spritesheet,(-469,-486))
    character = pygame.transform.scale(character, (34*3,38*3))
    Wildmutt_Roll8 = character

    character = pygame.Surface((44,45),pygame.SRCALPHA)
    character.blit(spritesheet,(-525,-486))
    character = pygame.transform.scale(character, (37*3,38*3))
    Wildmutt_Roll9 = character





    spritesheet = pygame.image.load("Graphics\\Fourarms_SpriteSheet2.png")
    character = pygame.Surface((45, 54), pygame.SRCALPHA)
    character.blit(spritesheet, (-40, -43))
    character = pygame.transform.scale(character, (45 * 3, 54 * 3))
    Fourarms_Idle1 = character

    character = pygame.Surface((45, 54), pygame.SRCALPHA)
    character.blit(spritesheet, (-99, -43))
    character = pygame.transform.scale(character, (45 * 3, 54 * 3))
    Fourarms_Idle2 = character

    character = pygame.Surface((45, 54), pygame.SRCALPHA)
    character.blit(spritesheet, (-155, -43))
    character = pygame.transform.scale(character, (45 * 3, 54 * 3))
    Fourarms_Idle3 = character

    character = pygame.Surface((45, 54), pygame.SRCALPHA)
    character.blit(spritesheet, (-213, -44))
    character = pygame.transform.scale(character, (45 * 3, 54 * 3))
    Fourarms_Idle4 = character

    character = pygame.Surface((43, 54), pygame.SRCALPHA)
    character.blit(spritesheet, (-58, -194))
    character = pygame.transform.scale(character, (43 * 3, 54 * 3))
    Fourarms_Walk1 = character

    character = pygame.Surface((52, 54), pygame.SRCALPHA)
    character.blit(spritesheet, (-115, -194))
    character = pygame.transform.scale(character, (52 * 3, 54 * 3))
    Fourarms_Walk2 = character

    character = pygame.Surface((35, 54), pygame.SRCALPHA)
    character.blit(spritesheet, (-182, -194))
    character = pygame.transform.scale(character, (35 * 3, 54 * 3))
    Fourarms_Walk3 = character

    character = pygame.Surface((41, 54), pygame.SRCALPHA)
    character.blit(spritesheet, (-231, -194))
    character = pygame.transform.scale(character, (41 * 3, 54 * 3))
    Fourarms_Walk4 = character

    character = pygame.Surface((51, 54), pygame.SRCALPHA)
    character.blit(spritesheet, (-288, -195))
    character = pygame.transform.scale(character, (51 * 3, 54 * 3))
    Fourarms_Walk5 = character

    character = pygame.Surface((35, 54), pygame.SRCALPHA)
    character.blit(spritesheet, (-355, -193))
    character = pygame.transform.scale(character, (35 * 3, 54 * 3))
    Fourarms_Walk6 = character

    character = pygame.Surface((44, 56), pygame.SRCALPHA)
    character.blit(spritesheet, (-42, -348))
    character = pygame.transform.scale(character, (42 * 3, 54 * 3))
    Fourarms_Punch1 = character

    character = pygame.Surface((44, 56), pygame.SRCALPHA)
    character.blit(spritesheet, (-96, -347))
    character = pygame.transform.scale(character, (42 * 3, 54 * 3))
    Fourarms_Punch2 = character

    character = pygame.Surface((61, 56), pygame.SRCALPHA)
    character.blit(spritesheet, (-154, -346))
    character = pygame.transform.scale(character, (59 * 3, 54 * 3))
    Fourarms_Punch3 = character

    character = pygame.Surface((61, 56), pygame.SRCALPHA)
    character.blit(spritesheet, (-223, -346))
    character = pygame.transform.scale(character, (59 * 3, 54 * 3))
    Fourarms_Punch4 = character

    character = pygame.Surface((49, 57), pygame.SRCALPHA)
    character.blit(spritesheet, (-297, -45))
    character = pygame.transform.scale(character, (49 * 3, 57 * 3))
    Fourarms_Jump1 = character

    character = pygame.Surface((45, 61), pygame.SRCALPHA)
    character.blit(spritesheet, (-464, -40))
    character = pygame.transform.scale(character, (40*3,54*3))
    Fourarms_Jump2 = character

    character = pygame.Surface((45,53),pygame.SRCALPHA)
    character.blit(spritesheet,(-456,-129))
    character = pygame.transform.scale(character, (45*3,54*3))
    Fourarms_Dead = character

    character = pygame.Surface((45,53),pygame.SRCALPHA)
    character.blit(spritesheet,(-455,-189))
    character = pygame.transform.scale(character, (46*3,54*3))
    Fourarms_Transform = character

    spritesheet = pygame.image.load("Graphics\\Heatblast_SpriteSheet.png")

    character = pygame.Surface((30,44),pygame.SRCALPHA)
    character.blit(spritesheet,(-15,-38))
    character = pygame.transform.scale(character, (30*3,44*3))
    Heatblast_Idle1 = character

    character = pygame.Surface((31,44),pygame.SRCALPHA)
    character.blit(spritesheet,(-53,-38))
    character = pygame.transform.scale(character, (31*3,44*3))
    Heatblast_Idle2 = character

    character = pygame.Surface((30,44),pygame.SRCALPHA)
    character.blit(spritesheet,(-98,-38))
    character = pygame.transform.scale(character, (30*3,44*3))
    Heatblast_Idle3 = character

    character = pygame.Surface((30,44),pygame.SRCALPHA)
    character.blit(spritesheet,(-138,-38))
    character = pygame.transform.scale(character, (30*3,44*3))
    Heatblast_Idle4 = character

    character = pygame.Surface((38,45),pygame.SRCALPHA)
    character.blit(spritesheet,(-220,-44))
    character = pygame.transform.scale(character, (38*3,45*3))
    Heatblast_Jump1 = character

    character = pygame.Surface((38,45),pygame.SRCALPHA)
    character.blit(spritesheet,(-267,-43))
    character = pygame.transform.scale(character, (38*3,45*3))
    Heatblast_Jump2 = character

    character = pygame.Surface((38,45),pygame.SRCALPHA)
    character.blit(spritesheet,(-316,-42))
    character = pygame.transform.scale(character, (38*3,45*3))
    Heatblast_Jump3 = character

    character = pygame.Surface((38,45),pygame.SRCALPHA)
    character.blit(spritesheet,(-359,-42))
    character = pygame.transform.scale(character, (38*3,45*3))
    Heatblast_Jump4 = character

    character = pygame.Surface((36,40),pygame.SRCALPHA)
    character.blit(spritesheet,(-431,-51))
    character = pygame.transform.scale(character, (36*3,40*3))
    Heatblast_Fall1 = character

    character = pygame.Surface((36,40),pygame.SRCALPHA)
    character.blit(spritesheet,(-470,-50))
    character = pygame.transform.scale(character, (36*3,40*3))
    Heatblast_Fall2 = character

    character = pygame.Surface((36,40),pygame.SRCALPHA)
    character.blit(spritesheet,(-509,-50))
    character = pygame.transform.scale(character, (36*3,40*3))
    Heatblast_Fall3 = character

    character = pygame.Surface((36,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-548,-47))
    character = pygame.transform.scale(character, (38*3,44*3))
    Heatblast_Fall4 = character

    character = pygame.Surface((31,40),pygame.SRCALPHA)
    character.blit(spritesheet,(-4,-201))
    character = pygame.transform.scale(character, (34*3,44*3))
    Heatblast_Walk1 = character

    character = pygame.Surface((36,40),pygame.SRCALPHA)
    character.blit(spritesheet,(-57,-198))
    character = pygame.transform.scale(character, (40*3,44*3))
    Heatblast_Walk2 = character

    character = pygame.Surface((21,40),pygame.SRCALPHA)
    character.blit(spritesheet,(-110,-201))
    character = pygame.transform.scale(character, (23*3,44*3))
    Heatblast_Walk3 = character

    character = pygame.Surface((30,40),pygame.SRCALPHA)
    character.blit(spritesheet,(-146,-199))
    character = pygame.transform.scale(character, (33*3,44*3))
    Heatblast_Walk4 = character

    character = pygame.Surface((36,40),pygame.SRCALPHA)
    character.blit(spritesheet,(-191,-200))
    character = pygame.transform.scale(character, (40*3,44*3))
    Heatblast_Walk5 = character

    character = pygame.Surface((21,40),pygame.SRCALPHA)
    character.blit(spritesheet,(-247,-200))
    character = pygame.transform.scale(character, (23*3,44*3))
    Heatblast_Walk6 = character

    character = pygame.Surface((31,43),pygame.SRCALPHA)
    character.blit(spritesheet,(-19,-274))
    character = pygame.transform.scale(character, (32*3,44*3))
    Heatblast_Punch1 = character

    character = pygame.Surface((53,43),pygame.SRCALPHA)
    character.blit(spritesheet,(-62,-272))
    character = pygame.transform.scale(character, (54*3,44*3))
    Heatblast_Punch2 = character

    character = pygame.Surface((55,43),pygame.SRCALPHA)
    character.blit(spritesheet,(-117,-274))
    character = pygame.transform.scale(character, (56*3,44*3))
    Heatblast_Punch3 = character

    character = pygame.Surface((52,43),pygame.SRCALPHA)
    character.blit(spritesheet,(-182,-276))
    character = pygame.transform.scale(character, (53*3,44*3))
    Heatblast_Punch4 = character

    character = pygame.Surface((30,44),pygame.SRCALPHA)
    character.blit(spritesheet,(-173,-39))
    character = pygame.transform.scale(character, (30*3,44*3))
    Heatblast_Dead = character

    character = pygame.Surface((30,44),pygame.SRCALPHA)
    character.blit(spritesheet,(-171,-93))
    character = pygame.transform.scale(character, (30*3,44*3))
    Heatblast_Transform = character

    
    spritesheet = pygame.image.load("Graphics\\XLR8_SpriteSheet.png")

    character = pygame.Surface((45,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-3,-27))
    character = pygame.transform.scale(character, (45*3,42*3))
    XLR8_Idle1 = character

    character = pygame.Surface((45,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-57,-27))
    character = pygame.transform.scale(character, (45*3,42*3))
    XLR8_Idle2 = character

    character = pygame.Surface((45,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-111,-27))
    character = pygame.transform.scale(character, (45*3,42*3))
    XLR8_Idle3 = character

    character = pygame.Surface((45,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-169,-26))
    character = pygame.transform.scale(character, (45*3,42*3))
    XLR8_Idle4 = character

    character = pygame.Surface((32,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-262,-94))
    character = pygame.transform.scale(character, (32*3,42*3))
    asda = character

    character = pygame.Surface((32,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-262,-94))
    character = pygame.transform.scale(character, (32*3,42*3))
    XLR8_Jump = character

    character = pygame.Surface((34,44),pygame.SRCALPHA)
    character.blit(spritesheet,(-324,-91))
    character = pygame.transform.scale(character, (32*3,42*3))
    XLR8_Fall = character


    character = pygame.Surface((44,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-5,-359))
    character = pygame.transform.scale(character, (44*3,42*3))
    XLR8_Kick1 = character

    character = pygame.Surface((37,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-62,-359))
    character = pygame.transform.scale(character, (37*3,42*3))
    XLR8_Kick2 = character

    character = pygame.Surface((31,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-107,-359))
    character = pygame.transform.scale(character, (31*3,42*3))
    XLR8_Kick3 = character

    character = pygame.Surface((49,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-162,-359))
    character = pygame.transform.scale(character, (49*3,42*3))
    XLR8_Kick4 = character

    character = pygame.Surface((33,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-216,-359))
    character = pygame.transform.scale(character, (33*3,42*3))
    XLR8_Kick5 = character

    character = pygame.Surface((33,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-264,-359))
    character = pygame.transform.scale(character, (33*3,42*3))
    XLR8_Kick6 = character

    character = pygame.Surface((52,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-1,-95))
    character = pygame.transform.scale(character, (52*3,42*3))
    XLR8_Walk1 = character

    character = pygame.Surface((52,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-61,-95))
    character = pygame.transform.scale(character, (52*3,42*3))
    XLR8_Walk2 = character

    character = pygame.Surface((52,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-121,-95))
    character = pygame.transform.scale(character, (52*3,42*3))
    XLR8_Walk3 = character

    character = pygame.Surface((52,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-183,-95))
    character = pygame.transform.scale(character, (52*3,42*3))
    XLR8_Walk4 = character

    character = pygame.Surface((45,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-307,-359))
    character = pygame.transform.scale(character, (45*3,42*3))
    XLR8_Dead = character

    character = pygame.Surface((45,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-299,-291))
    character = pygame.transform.scale(character, (45*3,42*3))
    XLR8_Transform = character

    character = pygame.Surface((45,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-10,-227))
    character = pygame.transform.scale(character, (45*3,42*3))
    XLR8_Run1 = character

    character = pygame.Surface((52,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-77,-227))
    character = pygame.transform.scale(character, (52*3,42*3))
    XLR8_Run2 = character

    character = pygame.Surface((53,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-149,-227))
    character = pygame.transform.scale(character, (53*3,42*3))
    XLR8_Run3 = character

    character = pygame.Surface((67,42),pygame.SRCALPHA)
    character.blit(spritesheet,(-273,-227))
    character = pygame.transform.scale(character, (67*3,42*3))
    XLR8_Run4 = character

    spritesheet = pygame.image.load("Graphics\\Ghostfreak_SpriteSheet.png")
    character = pygame.Surface((39,83),pygame.SRCALPHA)
    character.blit(spritesheet,(-272,-16))
    character = pygame.transform.scale(character, (39*2,83*2))
    Ghostfreak_Idle1 = character

    character = pygame.Surface((41,83),pygame.SRCALPHA)
    character.blit(spritesheet,(-330,-20))
    character = pygame.transform.scale(character, (41*2,83*2))
    Ghostfreak_Idle2 = character

    character = pygame.Surface((44,83),pygame.SRCALPHA)
    character.blit(spritesheet,(-392,-18))
    character = pygame.transform.scale(character, (44*2,83*2))
    Ghostfreak_Idle3 = character

    character = pygame.Surface((49,83),pygame.SRCALPHA)
    character.blit(spritesheet,(-450,-17))
    character = pygame.transform.scale(character, (49*2,83*2))
    Ghostfreak_Idle4 = character

    character = pygame.Surface((42,83),pygame.SRCALPHA)
    character.blit(spritesheet,(-514,-15))
    character = pygame.transform.scale(character, (42*2,83*2))
    Ghostfreak_Idle5 = character


    character = pygame.Surface((51,83),pygame.SRCALPHA)
    character.blit(spritesheet,(-266,-120))
    character = pygame.transform.scale(character, (51*2,83*2))
    Ghostfreak_Walk1 = character

    character = pygame.Surface((51,83),pygame.SRCALPHA)
    character.blit(spritesheet,(-326,-122))
    character = pygame.transform.scale(character, (51*2,83*2))
    Ghostfreak_Walk2 = character

    character = pygame.Surface((55,83),pygame.SRCALPHA)
    character.blit(spritesheet,(-384,-120))
    character = pygame.transform.scale(character, (55*2,83*2))
    Ghostfreak_Walk3 = character

    character = pygame.Surface((60,83),pygame.SRCALPHA)
    character.blit(spritesheet,(-439,-123))
    character = pygame.transform.scale(character, (60*2,83*2))
    Ghostfreak_Walk4 = character

    character = pygame.Surface((53,83),pygame.SRCALPHA)
    character.blit(spritesheet,(-518,-120))
    character = pygame.transform.scale(character, (53*2,83*2))
    Ghostfreak_Walk5 = character

    character = pygame.Surface((57,83),pygame.SRCALPHA)
    character.blit(spritesheet,(-17,-18))
    character = pygame.transform.scale(character, (57*2,83*2))
    Ghostfreak_Transform = character

    character = pygame.Surface((51,83),pygame.SRCALPHA)
    character.blit(spritesheet,(-266,-120))
    character = pygame.transform.scale(character, (51*2,83*2))
    Ghostfreak_Jump = character

    character = pygame.Surface((60,83),pygame.SRCALPHA)
    character.blit(spritesheet,(-439,-123))
    character = pygame.transform.scale(character, (60*2,83*2))
    Ghostfreak_Fall = character

    character = pygame.Surface((44,88),pygame.SRCALPHA)
    character.blit(spritesheet,(-10,-126))
    character = pygame.transform.scale(character, (44*2,88*2))
    Ghostfreak_Dead1 = character

    character = pygame.Surface((44,88),pygame.SRCALPHA)
    character.blit(spritesheet,(-75,-125))
    character = pygame.transform.scale(character, (44*2,88*2))
    Ghostfreak_Dead2 = character

    character = pygame.Surface((87,83),pygame.SRCALPHA)
    character.blit(spritesheet,(-10,-237))
    character = pygame.transform.scale(character, (87*2,83*2))
    Ghostfreak_Attack1 = character

    spritesheet = pygame.image.load("Graphics\\Ripjaws_SpriteSheet.png")
    character = pygame.Surface((52,63),pygame.SRCALPHA)
    character.blit(spritesheet,(-20,-64))
    character = pygame.transform.scale(character, (int(52*2.5),int(63*2.5)))
    Ripjaws_Idle1 = character

    character = pygame.Surface((50,63),pygame.SRCALPHA)
    character.blit(spritesheet,(-81,-63))
    character = pygame.transform.scale(character, (int(50*2.5),int(63*2.5)))
    Ripjaws_Idle2 = character

    character = pygame.Surface((52,63),pygame.SRCALPHA)
    character.blit(spritesheet,(-141,-62))
    character = pygame.transform.scale(character, (int(52*2.5),int(63*2.5)))
    Ripjaws_Idle3 = character

    character = pygame.Surface((53,63),pygame.SRCALPHA)
    character.blit(spritesheet,(-199,-62))
    character = pygame.transform.scale(character, (int(53*2.5),int(63*2.5)))
    Ripjaws_Idle4 = character

    character = pygame.Surface((66,63),pygame.SRCALPHA)
    character.blit(spritesheet,(-15,-143))
    character = pygame.transform.scale(character, (int(66*2.5),int(63*2.5)))
    Ripjaws_Walk1 = character

    character = pygame.Surface((66,63),pygame.SRCALPHA)
    character.blit(spritesheet,(-93,-146))
    character = pygame.transform.scale(character, (int(66*2.5),int(63*2.5)))
    Ripjaws_Walk2 = character

    character = pygame.Surface((66,63),pygame.SRCALPHA)
    character.blit(spritesheet,(-167,-144))
    character = pygame.transform.scale(character, (int(66*2.5),int(63*2.5)))
    Ripjaws_Walk3 = character

    character = pygame.Surface((66,63),pygame.SRCALPHA)
    character.blit(spritesheet,(-239,-143))
    character = pygame.transform.scale(character, (int(66*2.5),int(63*2.5)))
    Ripjaws_Walk4 = character

    character = pygame.Surface((66,63),pygame.SRCALPHA)
    character.blit(spritesheet,(-310,-146))
    character = pygame.transform.scale(character, (int(66*2.5),int(63*2.5)))
    Ripjaws_Walk5 = character

    character = pygame.Surface((66,63),pygame.SRCALPHA)
    character.blit(spritesheet,(-387,-150))
    character = pygame.transform.scale(character, (int(66*2.5),int(63*2.5)))
    Ripjaws_Walk6 = character

    character = pygame.Surface((49,63),pygame.SRCALPHA)
    character.blit(spritesheet,(-22,-536))
    character = pygame.transform.scale(character, (int(49*2.5),int(63*2.5)))
    Ripjaws_Attack1 = character

    character = pygame.Surface((84,63),pygame.SRCALPHA)
    character.blit(spritesheet,(-92,-536))
    character = pygame.transform.scale(character, (int(84*2.5),int(63*2.5)))
    Ripjaws_Attack2 = character

    character = pygame.Surface((68,63),pygame.SRCALPHA)
    character.blit(spritesheet,(-191,-537))
    character = pygame.transform.scale(character, (int(68*2.5),int(63*2.5)))
    Ripjaws_Attack3 = character

    character = pygame.Surface((45,62),pygame.SRCALPHA)
    character.blit(spritesheet,(-560,-193))
    character = pygame.transform.scale(character, (int(45*2.5),int(62*2.5)))
    Ripjaws_Jump = character

    character = pygame.Surface((32,63),pygame.SRCALPHA)
    character.blit(spritesheet,(-666,-200))
    character = pygame.transform.scale(character, (int(32*2.5),int(63*2.5)))
    Ripjaws_Fall = character

    character = pygame.Surface((53,63),pygame.SRCALPHA)
    character.blit(spritesheet,(-537,-59))
    character = pygame.transform.scale(character, (int(53*2.5),int(63*2.5)))
    Ripjaws_Transform = character

    character = pygame.Surface((53,63),pygame.SRCALPHA)
    character.blit(spritesheet,(-620,-59))
    character = pygame.transform.scale(character, (int(53*2.5),int(63*2.5)))
    Ripjaws_Dead = character


    spritesheet = pygame.image.load("Graphics\\Stinkfly_SpriteSheet.png")
    character = pygame.Surface((84,112),pygame.SRCALPHA)
    character.blit(spritesheet,(-13,-52))
    character = pygame.transform.scale(character, (84*2,112*2))
    Stinkfly_Transform = character

    character = pygame.Surface((78,112),pygame.SRCALPHA)
    character.blit(spritesheet,(-249,-44))
    character = pygame.transform.scale(character, (78*2,112*2))
    Stinkly_Idle1 = character

    character = pygame.Surface((86,112),pygame.SRCALPHA)
    character.blit(spritesheet,(-22,-196))
    character = pygame.transform.scale(character, (86*2,112*2))
    Stinkly_Walk1 = character

    character = pygame.Surface((94,112),pygame.SRCALPHA)
    character.blit(spritesheet,(-129,-196))
    character = pygame.transform.scale(character, (94*2,112*2))
    Stinkfly_Walk2= character

    character = pygame.Surface((74,112),pygame.SRCALPHA)
    character.blit(spritesheet,(-251,-195))
    character = pygame.transform.scale(character, (74*2,112*2))
    Stinkfly_Walk3 = character

    character = pygame.Surface((84,112),pygame.SRCALPHA)
    character.blit(spritesheet,(-344,-197))
    character = pygame.transform.scale(character, (84*2,112*2))
    Stinkfly_Attack1 = character

    character = pygame.Surface((84,112),pygame.SRCALPHA)
    character.blit(spritesheet,(-466,-195))
    character = pygame.transform.scale(character, (84*2,112*2))
    Stinkfly_Attack2 = character

    character = pygame.Surface((82,112),pygame.SRCALPHA)
    character.blit(spritesheet,(-568,-194))
    character = pygame.transform.scale(character, (82*2,112*2))
    Stinkfly_Attack3 = character

    character = pygame.Surface((73,69),pygame.SRCALPHA)
    character.blit(spritesheet,(-621,-72))
    character = pygame.transform.scale(character, (73*2,69*2))
    Stinkfly_Dead1 = character

    character = pygame.Surface((73,69),pygame.SRCALPHA)
    character.blit(spritesheet,(-721,-69))
    character = pygame.transform.scale(character, (73*2,69*2))
    Stinkfly_Dead2 = character    

    character = pygame.Surface((76,112),pygame.SRCALPHA)
    character.blit(spritesheet,(-386,-46))
    character = pygame.transform.scale(character, (76*2,112*2))
    Stinkfly_Fly1 = character

    character = pygame.Surface((82,112),pygame.SRCALPHA)
    character.blit(spritesheet,(-488,-49))
    character = pygame.transform.scale(character, (82*2,112*2))
    Stinkfly_Fly2 = character

    spritesheet = pygame.image.load("Graphics\\GreyMatter_SpriteSheet.png")

    character = pygame.Surface((73,64),pygame.SRCALPHA)
    character.blit(spritesheet,(-14,-124))
    character = pygame.transform.scale(character, (int(73/2),int(64/2)))
    Greymatter_Walk1 = character

    character = pygame.Surface((39,64),pygame.SRCALPHA)
    character.blit(spritesheet,(-124,-138))
    character = pygame.transform.scale(character, (int(39/2),int(64/2)))
    Greymatter_Walk2 = character

    character = pygame.Surface((71,64),pygame.SRCALPHA)
    character.blit(spritesheet,(-206,-122))
    character = pygame.transform.scale(character, (int(71/2),int(64/2)))
    Greymatter_Walk3 = character

    character = pygame.Surface((36,64),pygame.SRCALPHA)
    character.blit(spritesheet,(-315,-135))
    character = pygame.transform.scale(character, (int(36/2),int(64/2)))
    Greymatter_Walk4 = character

    character = pygame.Surface((38,64),pygame.SRCALPHA)
    character.blit(spritesheet,(-142,-30))
    character = pygame.transform.scale(character, (int(38/2),int(64/2)))
    Greymatter_Idle = character

    character = pygame.Surface((40,64),pygame.SRCALPHA)
    character.blit(spritesheet,(-310,-30))
    character = pygame.transform.scale(character, (int(40/2),int(64/2)))
    Greymatter_Attack1 = character

    character = pygame.Surface((70,64),pygame.SRCALPHA)
    character.blit(spritesheet,(-386,-31))
    character = pygame.transform.scale(character, (int(70/2),int(64/2)))
    Greymatter_Attack2 = character

    character = pygame.Surface((38,64),pygame.SRCALPHA)
    character.blit(spritesheet,(-37,-214))
    character = pygame.transform.scale(character, (int(38/2),int(64/2)))
    Greymatter_Transform = character

    character = pygame.Surface((38,64),pygame.SRCALPHA)
    character.blit(spritesheet,(-107,-214))
    character = pygame.transform.scale(character, (int(38/2),int(64/2)))
    Greymatter_Dead = character

    spritesheet = pygame.image.load("Graphics\\Diamondhead_SpriteSheet.png")

    character = pygame.Surface((39,74),pygame.SRCALPHA)
    character.blit(spritesheet,(-25,-22))
    character = pygame.transform.scale(character, (39*3,74*3))
    Diamondhead_Idle1 = character

    character = pygame.Surface((41,74),pygame.SRCALPHA)
    character.blit(spritesheet,(-80,-22))
    character = pygame.transform.scale(character, (41*3,74*3))
    Diamondhead_Idle2 = character

    character = pygame.Surface((39,74),pygame.SRCALPHA)
    character.blit(spritesheet,(-136,-22))
    character = pygame.transform.scale(character, (39*3,74*3))
    Diamondhead_Idle3 = character

    character = pygame.Surface((38,74),pygame.SRCALPHA)
    character.blit(spritesheet,(-191,-22))
    character = pygame.transform.scale(character, (38*3,74*3))
    Diamondhead_Idle4 = character

    character = pygame.Surface((38,74),pygame.SRCALPHA)
    character.blit(spritesheet,(-233,-22))
    character = pygame.transform.scale(character, (38*3,74*3))
    Diamondhead_Transform = character

    character = pygame.Surface((38,74),pygame.SRCALPHA)
    character.blit(spritesheet,(-276,-23))
    character = pygame.transform.scale(character, (38*3,74*3))
    Diamondhead_Dead = character

    character = pygame.Surface((52,74),pygame.SRCALPHA)
    character.blit(spritesheet,(-22,-118))
    character = pygame.transform.scale(character, (52*3,74*3))
    Diamondhead_Walk1 = character

    character = pygame.Surface((55,74),pygame.SRCALPHA)
    character.blit(spritesheet,(-88,-118))
    character = pygame.transform.scale(character, (55*3,74*3))
    Diamondhead_Walk2 = character

    character = pygame.Surface((33,74),pygame.SRCALPHA)
    character.blit(spritesheet,(-161,-118))
    character = pygame.transform.scale(character, (33*3,74*3))
    Diamondhead_Walk3 = character

    character = pygame.Surface((50,74),pygame.SRCALPHA)
    character.blit(spritesheet,(-217,-118))
    character = pygame.transform.scale(character, (50*3,74*3))
    Diamondhead_Walk4 = character

    character = pygame.Surface((57,74),pygame.SRCALPHA)
    character.blit(spritesheet,(-283,-118))
    character = pygame.transform.scale(character, (57*3,74*3))
    Diamondhead_Walk5 = character

    character = pygame.Surface((33,74),pygame.SRCALPHA)
    character.blit(spritesheet,(-356,-118))
    character = pygame.transform.scale(character, (33*3,74*3))
    Diamondhead_Walk6 = character

    character = pygame.Surface((62,74),pygame.SRCALPHA)
    character.blit(spritesheet,(-24,-438))
    character = pygame.transform.scale(character, (62*3,74*3))
    Diamondhead_Attack1 = character

    character = pygame.Surface((58,74),pygame.SRCALPHA)
    character.blit(spritesheet,(-104,-438))
    character = pygame.transform.scale(character, (58*3,74*3))
    Diamondhead_Attack2 = character

    character = pygame.Surface((50,74),pygame.SRCALPHA)
    character.blit(spritesheet,(-184,-438))
    character = pygame.transform.scale(character, (50*3,74*3))
    Diamondhead_Attack3 = character

    character = pygame.Surface((38,74),pygame.SRCALPHA)
    character.blit(spritesheet,(-261,-438))
    character = pygame.transform.scale(character, (38*3,74*3))
    Diamondhead_Attack4 = character

    character = pygame.Surface((58,74),pygame.SRCALPHA)
    character.blit(spritesheet,(-99,-630))
    character = pygame.transform.scale(character, (58*3,74*3))
    Diamondhead_Jump = character

    character = pygame.Surface((40,74),pygame.SRCALPHA)
    character.blit(spritesheet,(-188,-630))
    character = pygame.transform.scale(character, (40*3,74*3))
    Diamondhead_Fall = character

    spritesheet = pygame.image.load("Graphics\\Upgrade_SpriteSheet.png")

    character = pygame.Surface((67,97),pygame.SRCALPHA)
    character.blit(spritesheet,(-13,-47))
    character = pygame.transform.scale(character, (67*2,97*2))
    Upgrade_Transform = character

    character = pygame.Surface((67,97),pygame.SRCALPHA)
    character.blit(spritesheet,(-91,-47))
    character = pygame.transform.scale(character, (67*2,97*2))
    Upgrade_Dead = character

    character = pygame.Surface((67,97),pygame.SRCALPHA)
    character.blit(spritesheet,(-181,-50))
    character = pygame.transform.scale(character, (67*2,97*2))
    Upgrade_Idle = character

    character = pygame.Surface((62,97),pygame.SRCALPHA)
    character.blit(spritesheet,(-460,-50))
    character = pygame.transform.scale(character, (62*2,97*2))
    Upgrade_Walk1 = character

    character = pygame.Surface((29,97),pygame.SRCALPHA)
    character.blit(spritesheet,(-536,-50))
    character = pygame.transform.scale(character, (29*2,97*2))
    Upgrade_Walk2 = character

    character = pygame.Surface((54,97),pygame.SRCALPHA)
    character.blit(spritesheet,(-578,-50))
    character = pygame.transform.scale(character, (54*2,97*2))
    Upgrade_Walk3 = character

    character = pygame.Surface((30,97),pygame.SRCALPHA)
    character.blit(spritesheet,(-646,-50))
    character = pygame.transform.scale(character, (30*2,97*2))
    Upgrade_Walk4 = character

    character = pygame.Surface((63,97),pygame.SRCALPHA)
    character.blit(spritesheet,(-13,-193))
    character = pygame.transform.scale(character, (63*2,97*2))
    Upgrade_Attack1 = character

    character = pygame.Surface((63,97),pygame.SRCALPHA)
    character.blit(spritesheet,(-112,-189))
    character = pygame.transform.scale(character, (63*2,97*2))
    Upgrade_Attack2 = character

    character = pygame.Surface((60,97),pygame.SRCALPHA)
    character.blit(spritesheet,(-213,-192))
    character = pygame.transform.scale(character, (60*2,97*2))
    Upgrade_Attack3 = character

    character = pygame.Surface((110,97),pygame.SRCALPHA)
    character.blit(spritesheet,(-303,-191))
    character = pygame.transform.scale(character, (110*2,97*2))
    Upgrade_Attack4 = character

    character = pygame.Surface((66,97),pygame.SRCALPHA)
    character.blit(spritesheet,(-434,-190))
    character = pygame.transform.scale(character, (66*2,97*2))
    Upgrade_Attack5 = character

    character = pygame.Surface((60,97),pygame.SRCALPHA)
    character.blit(spritesheet,(-526,-189))
    character = pygame.transform.scale(character, (60*2,97*2))
    Upgrade_Attack6 = character