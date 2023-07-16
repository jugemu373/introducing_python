"新しいクラスは最初の親クラスからすべてのものを継承している。親クラスのメソッドをオーバーライドする(置き換える)方法を示す。"


class Car():
    def exclaim(self):
        print("I'm a Car!")


class Yugo():
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish")


give_me_a_car = Car()
give_me_a_Yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_Yugo.exclaim()


"__init__()を含むあらゆるメソッドをオーバライドすることができる"


class Person():
    def __init__(self, name):
        self.name = name


class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name


class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"


person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
print(person.name)
print(doctor.name)
print(lawyer.name)
