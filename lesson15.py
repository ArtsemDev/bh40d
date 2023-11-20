class Math(object):
    __slots__ = ("a", "b")

    def __init__(self, a, b):
        self.a = a
        self.b = b

    async def mul(self, a=None, b=None):
        if a is None and b is None:
            return self.a * self.b
        return a * b

    def sum(self):
        return self.a + self.b

    def dif(self):
        return self.a - self.b

    def divide(self):
        return self.a / self.b
