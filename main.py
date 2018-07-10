from dog import Dog
from cat import Cat

dog_karma = Dog("Karma", "Pitbull", "Blue and White")
print(dog_karma.name, dog_karma.breed, dog_karma.color)
dog_karma.bark()

cat_cali = Cat("Cali", "stray", "Black and Orange")
print(cat_cali.name, cat_cali.breed, cat_cali.color)
cat_cali.meow()