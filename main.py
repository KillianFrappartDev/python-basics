# Dictionnaries
tech_dictionnary = {
    "React": "Library for building user interfaces.",
    "Node": "JavaScript runtime.",
    "C#": "Strongly typed programming language",
}

# Retrieve data
tech_dictionnary["Node"]

# Add data
tech_dictionnary["SQL"] = "Query language used to build databases."

# Remove data
tech_dictionnary.pop("React")

# Copy a dictionnary
copied_dictionnary = tech_dictionnary.copy()

# Declared in the global context
API_KEY = "ABCDEF1234"


def demo():
    global API_KEY
    API_KEY = "CHANGED"


# Changed
print(API_KEY)
demo()
print(API_KEY)

print("C++" in tech_dictionnary)

# OOP


class Car:

    # Constructor
    def __init__(self, color):

        # Àttributes
        self.color = color

    # Methods
    def info(self):
        print(self.color)


car = Car("Red")

car.info()

# Packages
# python3 -m venv .venv
# source .venv/bin/activate

import heroes

print(heroes.gen())