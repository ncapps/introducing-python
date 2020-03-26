# 10.1
class Thing:
    pass

print(Thing)
example = Thing()
print(example)

# 10.2
class Thing2:
    letters = 'abc'
    
print(Thing2.letters)

# 10.3
class Thing3:
    def __init__(self, letters):
        self.letters = letters

example3 = Thing3('xyz')
print(example3.letters)

# 10.4
class Element:
    def __init__(self, input_name, input_symbol, input_number):
        self.__name = input_name
        self.__symbol = input_symbol
        self.__number = input_number
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number
    @name.setter
    def name(self, input_name):
        self.__name = input_name
    @symbol.setter
    def symbol(self, input_symbol):
        self.__symbol = input_symbol
    @number.setter
    def number(self, input_number):
        self.__number = input_number
    def __str__(self):
        import pprint
        return f'{vars(self)}'
    def dump(self):
        import pprint
        pprint.pprint(vars(self))


example4 = Element('Hydrogen', 'H', 1)
print(example4)

# 10.5
h_dict = {'input_name': 'Hydrogen', 'input_symbol': 'H', 'input_number': 1}
hydrogen = Element(**h_dict)
print(hydrogen)

# 10.6
hydrogen.dump()

# 10.7
print(hydrogen)

# 10.8
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

bear = Bear()
print(bear.eats())
rabbit = Rabbit()
print(rabbit.eats())
octothorpe = Octothorpe()
print(octothorpe.eats())

# 10.10
class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'

class Smartphone:
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = Smartphone()
    def does(self):
        print(f'The Laser {self.laser.does()}')
        print(f'The Claw {self.claw.does()}')
        print(f'The Smartphone {self.smartphone.does()}')

robot = Robot()
robot.does()