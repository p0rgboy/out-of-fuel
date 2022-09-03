@namespace
class SpriteKind:
    Gas = SpriteKind.create()

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        Dart1
    """), mySprite, 0, -100)
    projectile.start_effect(effects.fire)
    mySprite.say_text("pew")
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    global enemySpeed
    sprite.destroy(effects.ashes, 100)
    otherSprite.destroy()
    info.change_score_by(1)
    if info.score() == 10:
        info.change_score_by(5)
        mySprite.say_text("+ level-up bonus", 2000, False)
        enemySpeed = 70
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap)

def on_on_zero(status):
    game.over(False)
statusbars.on_zero(StatusBarKind.health, on_on_zero)

def on_on_overlap2(sprite2, otherSprite2):
    statusbar.value = 100
    otherSprite2.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Gas, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    info.change_life_by(-1)
    otherSprite3.destroy(effects.spray, 500)
    scene.camera_shake(4, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

myEnemy: Sprite = None
myFuel: Sprite = None
projectile: Sprite = None
enemySpeed = 0
statusbar: StatusBarSprite = None
mySprite: Sprite = None
scene.set_background_image(assets.image("""
    Galaxy
"""))
scroller.scroll_background_with_speed(0, 10)
mySprite = sprites.create(img("""
        ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ................................
            ..............1.................
            .............111................
            ............11111...............
            ...........1111111..............
            ...........11111111.............
            ...........11111111.............
            ...........11111111.............
            ...........11111911.............
            ...........11119111.............
            ...........11191111.............
            ...........11911111.............
            ...........11911111.............
            ...........11191111.............
            ...........11119111.............
            ...........11111911.............
            ...........11119111.............
            ...........11191111.............
            ...........11911111.............
            ...........11911111.............
            ...........11191111.............
            ...........11119111.............
            ...........11111911.............
            ...........11111111.............
            .............4444...............
            ............4....4..............
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
mySprite.set_stay_in_screen(True)
animation.run_image_animation(mySprite,
    assets.animation("""
        Flying Rocket
    """),
    100,
    True)
statusbar = statusbars.create(20, 4, StatusBarKind.health)
statusbar.attach_to_sprite(mySprite, 30, 0)
enemySpeed = 50
mySprite.say_text("i am going to run out of fuel soon", 1000, False)
effects.star_field.start_screen_effect()
music.play_melody("E D G F B A C5 B ", 120)

def on_update_interval():
    global myFuel
    myFuel = sprites.create_projectile_from_sprite(assets.image("""
            Fuel
        """),
        mySprite,
        randint(100, 50),
        80)
    myFuel.x = randint(5, 155)
    myFuel.set_kind(SpriteKind.Gas)
game.on_update_interval(5000, on_update_interval)

def on_update_interval2():
    global myEnemy
    myEnemy = sprites.create_projectile_from_side(assets.image("""
        Spider
    """), 0, 40)
    myEnemy.x = randint(10, 155)
    myEnemy.set_kind(SpriteKind.enemy)
    animation.run_image_animation(myEnemy,
        assets.animation("""
            Flying Spider
        """),
        100,
        True)
game.on_update_interval(2000, on_update_interval2)

def on_update_interval3():
    global myEnemy
    myEnemy = sprites.create_projectile_from_side(assets.image("""
        UFO
    """), 0, 30)
    myEnemy.x = randint(10, 155)
    myEnemy.set_kind(SpriteKind.enemy)
    animation.run_image_animation(myEnemy, assets.animation("""
        Flying UFO
    """), 200, True)
game.on_update_interval(2000, on_update_interval3)

def on_update_interval4():
    global myEnemy
    myEnemy = sprites.create_projectile_from_side(assets.image("""
        Stealth
    """), 0, 50)
    myEnemy.x = randint(10, 155)
    myEnemy.set_kind(SpriteKind.enemy)
    animation.run_image_animation(myEnemy,
        assets.animation("""
            Flying Stealth
        """),
        100,
        True)
game.on_update_interval(2000, on_update_interval4)

def on_update_interval5():
    statusbar.value += -1
game.on_update_interval(300, on_update_interval5)
