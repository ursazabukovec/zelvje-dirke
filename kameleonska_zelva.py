from zelva import Zelva

def naslednja(x, y, z):
    """
    Določi naslednjo vrednost barve glede na prejšnje vrednosti.
    """
    return 1 - z if x + y == 1 else x

class KameleonskaZelva(Zelva):
    """
    Želva, ki spreminja barvo in hitrost.
    """

    def __init__(self, ime='Kameleonska želva'):
        """
        Konstruira kameleonsko želvo.
        """
        self.barva = (0.0, 0.0, 1.0)
        Zelva.__init__(self, ime=ime, barva=self.barva, hitrost=1)
        self.shape('arrow')

    def posodobi(self, pozicija):
        """
        Posodobi barvo in hitrost kameleonske želve.
        """
        mod = 2 if pozicija > 0 else 4
        self.speed(self.speed() % mod + 1)
        r, g, b = self.barva
        self.barva = (naslednja(r, g, b),
                      naslednja(g, b, r),
                      naslednja(b, r, g))
        self.color(self.barva)
