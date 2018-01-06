class Cal(object):
    _history = []
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2
    def add(self):
        resurt = self.v1 + self.v2
        Cal._history.append('add : %d+%d=%d' %(self.v1, self.v2, resurt))
        return resurt
    def subtract(self):
        resurt = self.v1 - self.v2
        Cal._history.append('subtract : %d-%d=%d' % (self.v1, self.v2, resurt))
        return resurt
    def setv1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getv1(self):
        return self.v1
    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)
class Calmultiply(Cal):
    def multiply(self):
        resurt = self.v1 * self.v2
        Cal._history.append('multiply : %d*%d=%d' % (self.v1, self.v2, resurt))
        return resurt
class Caldivide(Calmultiply):
    def divide(self):
        resurt = self.v1 / self.v2
        Cal._history.append('divide : %d/%d=%d' % (self.v1, self.v2, resurt))
        return resurt
c1 = Cal(10,10)
print(c1.add())
print(c1.subtract())
c1 = Calmultiply(10, 10)
print(c1.multiply())
c1 = Caldivide(20,10)
print(c1.divide())
Cal.history()
