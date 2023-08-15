################### Scope ####################

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# not in scope
# print(potion_strength)

# Global scope
player_health = 10


def game():
    def drink_potion2():
        potion_strength = 2
        print(player_health)

    drink_potion2()


# There is no block scope
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)


# Modifying global scope
# Only use when the situation is correct, i.e examples below
enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Return instead
enemies = 1


def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


print(f"enemies from return: {increase_enemies()}")
print(f"enemies outside function: {enemies}")


# Global constants (good use)
# variables that will never change
# naming convention all uppercase

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"
