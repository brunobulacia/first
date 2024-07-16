class Nodo:
    def __init__(self):
        self.elemento = None
        self.sig = None


class Lista:
    def __init__(self):
        self.longit = 0
        self.ptrElementos = Nodo()

    def primero(self):
        if not self.vacia():
            return self.ptrElementos

    def vacia(self):
        return self.longit == 0
    
    def fin(self):
        if not self.vacia():
            x = self.ptrElementos
            while x.sig != None:
                x = x.sig
            return x

    def inserta_primero(self, e):
        x = Nodo()
        x.elemento = e
        x.sig = self.ptrElementos
        self.longit += 1
        self.ptrElementos = x

    def primerElem(self):
        if not self.vacia():
            return self.ptrElementos.elemento

    def siguiente(self, dir):
        x = Nodo()
        dir = x
        if self.vacia():
            if not self.vacia():
                return dir.sig

l = Lista()
l.inserta_primero(9)
l.inserta_primero(222)



