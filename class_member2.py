class cs:
    count = 0
    def __init__(self):
        cs.count = cs.count + 1
    @classmethod
    def getCount(cls):
        return cs.count

i1 = cs()
i2 = cs()
i3 = cs()
i4 = cs()
print(cs.getCount())