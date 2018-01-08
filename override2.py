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
    def info(self):
        return "Cal => v1 : %d, v2 : %d"%(self.v1, self.v2)
class Calmultiply(Cal):
    def multiply(self):
        resurt = self.v1 * self.v2
        Cal._history.append('multiply : %d*%d=%d' % (self.v1, self.v2, resurt))
        return resurt
    def info(self):
        return "Calmultyply => %s"%super().info()
class Caldivide(Calmultiply):
    def divide(self):
        resurt = self.v1 / self.v2
        Cal._history.append('divide : %d/%d=%d' % (self.v1, self.v2, resurt))
        return resurt
    def info(self):
        return "Caldivide => %s"%super().info()
c0 = Cal(30, 60)
print(c0.info())
c1 = Calmultiply(10,10)
print(c1.info())
c2 = Caldivide(20,10)
print(c2.info())
Cal.history()
