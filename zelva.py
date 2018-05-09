import turtle

class Zelva(turtle.Turtle):
    """
    Splošna želva.
    """

    def __init__(self, ime, barva='green', hitrost=1):
        """
        Konstruira želvo z danim imenom, barvo in hitrostjo.
        """
        turtle.Turtle.__init__(self)
        self.ime = ime
        self.color(barva)
        self.speed(hitrost)

    def posodobi(self, pozicija):
        """
        Posodobi želvo glede na njeno pozicijo.

        Privzeto ne naredi nič.
        """
        pass

    def __str__(self):
        """
        Vrne znakovno predstavitev želve z njenim imenom.
        """
        return self.ime
