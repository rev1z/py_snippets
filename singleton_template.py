class Singleton:
    _inst = None

    def __new__(cls, *args, **kwargs):
        if Singleton._inst is None:
            Singleton._inst = super().__new__(cls)
        return Singleton._inst

    def __init__(self, val):
        self.val = val
