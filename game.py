import pgzrun
from random import randint
from quickdraw import QuickDrawData
qd = QuickDrawData()

rnd_raccoon = qd.get_drawing("raccoon")
rnd_raccoon.image.save("images/raccoon.png")
raccoon = Actor("raccoon")
beep = tone.create('A3', 0.5)
def draw():
    screen.clear()
    screen.fill('white')
    raccoon.draw()

def place_raccoon():
    raccoon.x = randint(100, 750)
    raccoon.y = randint(100, 550)

def set_raccoon_normal():
    images.cache.clear()
    rnd_raccoon = qd.get_drawing("raccoon")
    rnd_raccoon.image.save("images/raccoon.png")
    raccoon.image = "raccoon.png"

def set_skull():
    rnd_skull = qd.get_drawing("skull")
    rnd_skull.image.save("images/skull.png")
    raccoon.image = "skull.png"

def on_mouse_down(pos):
    if raccoon.collidepoint(pos):
        rnd_lightning = qd.get_drawing("lightning")
        rnd_lightning.image.save("images/lightning.png")
        raccoon.image = "lightning.png"
        clock.schedule_unique(set_skull, 0.1)
        sounds.thunder.play()
        clock.schedule_unique(set_raccoon_normal, 0.5)
        
    else:
        beep.play()
    clock.schedule_unique(place_raccoon, 0.5)

place_raccoon()

pgzrun.go()
