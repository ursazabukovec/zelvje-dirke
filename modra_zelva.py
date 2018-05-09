from zelva import Zelva

class ModraZelva(Zelva):
    """ Želva modre barve. """

    def __init__(self, ime='Modra želva'):
        """ Konstruira modro želvo. """
        Zelva.__init__(self, ime=ime, barva='dodgerblue', hitrost=7)
        self.shape('turtle')
