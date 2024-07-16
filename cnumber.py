import math
class Number:
    value = 0
    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value
    
    def get_digit(self, d):
        k = 10 ** (d-1)
        return (self.value // k) % 10
    
    def count_digits(self):
        return math.floor(math.log10(self.value)+1)

    def ins_digit(self, p, d):
        k = 10 ** (p-1)
        r = self.value % k
        self.value = ((self.value // k) * 10 + d) * k + r

    def del_digit(self, p):
        k = 10 ** (p-1)
        r = self.value % k
        self.value = ((self.value // k) // 10) * k + r

    def mod_digit(self, p, d):
        self.del_digit(p)
        self.ins_digit(p,d)

    # EJERCICIOS
    # 1. RETORNAR EL DIGITO MAYOR
    def max_digit(self):
        max = self.get_digit(1)
        for i in range(2, self.count_digits()):
            if self.get_digit(i) > max:
                max = self.get_digit(i)
        return max
    # 2. POSICION DEL MAYOR
    def max_pos(self):
        pos = 1
        max = self.get_digit(1)
        for i in range(2, self.count_digits()):
            if self.get_digit(i) > max:
                max = self.get_digit(i)
                pos = i
        return pos
    
    # 3. BORRAR EL MAYOR
    def del_max(self):
        self.del_digit(self.max_pos())

    # 4. BORRAR UN DIGITO POR PARAMETRO
    def del_dig_param(self, d):
        i = 1
        while i <= self.count_digits():
            if self.get_digit(i) == d:
                self.del_digit(i)
            else:
                i += 1

    def sort_digits(self):
        for i in range(1, self.count_digits()):
            max = self.get_digit(i)
            pos = i
            j = i+1
            while j <= self.count_digits():
                if (self.get_digit(j) > max):
                    max = self.get_digit(j)
                    pos = j
                j += 1
            self.del_digit(pos)
            self.ins_digit(i, max)

    def del_repeated(self):
        for i in range(1, self.count_digits()):
            j = i+1
            while j <= self.count_digits():
                if self.get_digit(i) == self.get_digit(j):
                    self.del_digit(j)
                else:
                    j += 1


