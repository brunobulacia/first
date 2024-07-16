class Cola:
    Ini = ""
    Fin = ""
    s = "_"
    def Primero(self):
        return self.Ini
    
    def Vacia(self):
        return self.Ini == ""
    
    def Poner(self, e):
        self.s = self.s + e + "_"
        if self.s == "":
            self.Ini = e
            self.Fin = e
        else:
            self.Fin = e

    def Sacar(self, e):
        self.s = self.s[1:]
        e = self.s[0:self.s.index("_")]
        self.s = self.s[self.s.index("_")+1:]
        if self.s != "":
            self.Ini = self.s[0:self.s.index("_")]
        else:
            self.Ini = ""
        self.s = "_" + self.s
        return e
