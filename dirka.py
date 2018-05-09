import turtle
from zelva import Zelva
from rdeca_zelva import RdecaZelva
from kameleonska_zelva import KameleonskaZelva
from modra_zelva import ModraZelva

# Barve bomo nastavljali s števili v rangu od 0.0 do 1.0
turtle.colormode(1.0)

ZELVE = [
    RdecaZelva(),
    KameleonskaZelva(),
    Zelva('Zelenka', barva='green', hitrost=1),
    ModraZelva(),
]

def dirka(zacetek, konec, visina=20, korak=10):
    """
    Funkcija, ki izvede dirko želv.
    """
    # Narišemo štartno in ciljno črto
    turtle.tracer(False)
    turtle.hideturtle()
    turtle.up()
    turtle.setpos(zacetek, 0)
    turtle.down()
    turtle.setpos(zacetek, visina * (len(ZELVE) + 1))
    turtle.up()
    turtle.setpos(konec, 0)
    turtle.down()
    turtle.setpos(konec, visina * (len(ZELVE) + 1))
    # Želve postavimo na štartno črto
    for i, zelva in enumerate(ZELVE):
        zelva.up()
        zelva.setpos(zacetek, visina * (i+1))
        zelva.write(zelva, align='right')
        zelva.down()
    turtle.tracer(True)

    prva_zelva = zacetek
    # Želve premikamo, dokler vsaj ena ne doseže ciljne črte
    while prva_zelva < konec:
        for zelva in ZELVE:
            zelva.forward(korak * zelva.speed())
            zelva.posodobi(zelva.xcor())
            prva_zelva = max(prva_zelva, zelva.xcor())
            if zelva.xcor() >= konec:
                print("{} je prišla do cilja!".format(zelva))

# Izvedemo dirko
dirka(-250, 330)
