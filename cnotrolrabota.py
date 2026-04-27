x = int(input())
a = [4, -1, 4, -3, 8, 2, 5]
sos = ["Datan", "Batan", "Tatan", "Saveliy"]

#6
x6 = (x * 9/5) + 32
print("6:", x6)

#7
y = 1
for i in range(2, x + 1):
    y *= i
print("7:", y)

#8
if x > 0:
    print("8:", '+')
elif x == 0:
    print("8:", '0')
else:
    print("8:", '-')

#9
x9 = 2 + 4 + 6 + 8
print("9:", x9)

#10
x10 = max(a)
print("10:", x10)

#11
x11 = max(sos)
print("11:", x11)

#12
a.sort()
print("12:", a)

#13
for i in a:
    if a == i:
        a.remove(i)
print("13:", a)

#14

#15 #16 #17 #18
class V1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_info(self):
        print('Name -', self.name)
        print('Age -', self.age)

class Hello:
    def __init__(self, hello):
        self.hello = hello
    def print_info(self):
        print('*V1 waves*', self.hello)

class Book:
    def __init__(self, name, avtor):
        self.name = name
        self.avtor = avtor
    def print_info(self):
        print('Name -', self.name)
        print('Avtor -', self.avtor)

v1 = V1('V1', '%*@&%$@#%*#&%&@&$')
hello = Hello('... (silence)')
book = Book('Slash Misery', 'Datan')

print('Info about it - 1', 'Say hello - 2', 'Circle S - 3', 'Book - 4')

p = int(input())
if p == 1:
    v1.print_info()
elif p == 2:
    hello.print_info()
elif p == 4:
    book.print_info()
else:
    print('no')