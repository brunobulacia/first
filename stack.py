class Stack:
    tope = ""
    s = "_"
    def cima(self):
        return self.tope
    
    def vacia(self):
        return self.tope == ""
    
    def meter(self, e):
        self.s = "_" + e + self.s
        self.tope = e

    def sacar(self, e):
        self.s = self.s[1:]
        e = self.s[0:self.s.index("_")]
        self.s = self.s[self.s.index("_")+1:]
        if self.s != "":
            self.tope = self.s[0:self.s.index("_")]
        else:
            self.tope = ""
        self.s = "_" + self.s
        return e
