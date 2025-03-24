class Complex:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a == 0 and self.b == 0:
            return "0"
        elif self.a ==0:
            if self.b ==1:
                return "i"
            elif self.b == -1:
                return "-i"
            else:
                return f"{self.b}i"
        elif self.b == 0:
            return f"{self.a}"
        else:
            if self.b > 0:
                if self.b == 1:
                    return f"{self.a} +i"
                else:
                    return f"{self.a} + {self.b}i"
            else:
                if self.b == -1:
                    return f"{self.a} -i"
                else:
                    return f"{self.a} - {abs(self.b)}i"

    def add(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def negate(self):
        return complex(-self.a, -self.b)

    def subtract(self, other):
        return self.add(other.negate())

    def multiply(self, other):
        real = self.a * other.a - self.b * other.b
        imag = self.a * other.b + self.b * other.a
        return Complex(real, imag)

    def conjugate(self):
        return Complex(self.a, -self.b)

    def inverse(self):
        denominator = self.a**2 + self.b**2
        return Complex(self.a/denominator, -self.b/denominator)

    def divide(self, other):
        denominator = other.a**2 +other.b**2
        real = (self.a*other.a+self.b*other.b)/denominator
        imag = (self.b*other.a+self.a*other.b)/denominator
        return Complex(real,imag)

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __mul__(self, other):
        return self.multiply(other)
