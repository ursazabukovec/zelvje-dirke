from zelva import Zelva

class RdecaZelva(Zelva):
    """
    Želva rdeče barve.
    """

    def __init__(self, ime='Rdeča želva'):
        """
        Konstruira rdečo želvo.
        """
        Zelva.__init__(self, ime=ime, barva='red', hitrost=2)
        self.shape('turtle')
