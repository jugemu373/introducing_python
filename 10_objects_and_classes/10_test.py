# 10.1
class Thing:
    pass


example = Thing()
print(Thing())
print(example)


# 10.2
class Thing2:
    letters = 'abc'


print(Thing2.letters)

# 10.3


class Thing3:
    def __init__(self):
        self.letters = 'xyz'


# 10.4
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


hydrogen = Element('Hydrogen', 'H', 1)


# 10.5
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])
print(hydrogen.name)
hydrogen = Element(**el_dict)
print(hydrogen.name)


# 10.6
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        pass
        # print(f'{name=}, {symbol=}, {number=}')


hydrogen = Element(**el_dict)
hydrogen.dump()


# 10.7
print(hydrogen)


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        pass
        # return f'{name=}, {symbol=}, {number=}'


hydrogen = Element(**el_dict)
print(hydrogen)


# 10.8
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number


hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)


# 10.9
class Bear:
    def eats(self):
        return 'berries'


class Rabbit:
    def eats(self):
        return 'clover'


class Octothorpe:
    def eats(self):
        return 'campers'


b = Bear()
r = Rabbit()
o = Octothorpe()
print(b.eats())
print(r.eats())
print(o.eats())


# 10.10
class Laser:
    def does(self):
        return 'disintegrate'


class Claw:
    def does(self):
        return 'crush'


class SmartPhone:
    def does(self):
        return 'ring'


class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        return """I have many attachments:
        My laser, to {}.
        My Claw, to {}.
        My smartphone, to {}.""".format(
            self.laser.does(),
            self.claw.does(),
            self.smartphone.does()
        )


robbie = Robot()
print(robbie.does())
