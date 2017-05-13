import random

health = 50
difficulty = 1

potion_value = int(random.randint(25,50)/difficulty)

health += potion_value

print(health)
