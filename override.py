class c1:
    def m(self):
        return 'parent'

class c2(c1):
    def m(self):
        return super().m()  + ' child'
o = c2()
print(o.m())