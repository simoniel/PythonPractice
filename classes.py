class Person:
    def __init__(self, n, a, c, co):
        self.name = n
        self.age = a
        self.city = c
        self.country = co

    def __str__(self):
        return f"{self.name} {self.age} {self.city} {self.country}"
    
    def print_info(self):
        print(self.name)
        print(self.age)
        print(self.city)
        print(self.country)

    def celebrate_birthday(self):
        self.age += 1
        print(f'Happy Birthday! You are now {self.age}')

class Student(Person):
    def __init__(self,n,a,c,co, y):
        #Person.__init__(self,n,a,c,co)
        super().__init__(n,a,c,co)
        self.graduation_year = y

    def __str__(self):
        return f'{super().__str__()} {self.graduation_year}' 


class Computer:
    def __init__(self, model):
        self.model = model
        self.cpu = self.CPU()
        self.ram = self.RAM()
    
    class CPU:
        def process(self):
            print ("processing data")

    class RAM:
        def store(self):
            print ("storing data")


class Playlist:
    def __init__(self, n):
        self.name = n
        self.songs = []
    
    def __str__(self):
        return f'{self.name} {self.songs}'

    def add_song(self, s):
        self.songs.append(s)
        print(f'Added {s}')

    def remove_song(self, s):
        if s in self.songs:
            self.songs.pop(s)
            print(f'Removed s')



ps1 = Playlist('Favorites')
ps1.add_song('Drones')
ps1.add_song('Give it all')
print(ps1)


c1 = Computer('IBM')
c1.cpu.process()
c1.ram.store()

    
p1 = Person('Emil', 23, 'Geneve', 'Suisse')
print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)

p2 = Person('Rosa', 55, 'Geneve', 'Suisse')
p2.print_info()
print(p2)
p2.celebrate_birthday()

p3 = Student('Aerin', 34, 'Rome', 'Italy', 2020)
print(p3)


