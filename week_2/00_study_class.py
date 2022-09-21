class Person:
    def __init__(self, para_name):
        print("i am created!", self)
        self.name = para_name

    def talk(self):
        print('안녕하세요 제 이름은', self.name, '입니다')


person1 = Person('유재석')
print(person1.name)
person2 = Person('박명수')
print(person2.name)
person1.talk()
