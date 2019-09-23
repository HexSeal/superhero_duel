# my-dogs.py
from dog import Dog

my_dog = Dog("Rex", "SuperDog")
my_dog.bark()

my_other_dog = Dog('Annie', 'SuperDog')
print(my_other_dog.name)

one_more_dog = Dog('Brutus', "NormalDog")
one_more_dog.sit(one_more_dog.name)

final_dog = Dog('Noche', 'Mutt')
final_dog.roll_over(final_dog.name)

