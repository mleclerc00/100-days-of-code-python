# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello")
    print("World")
    print("!")

greet()

def greet_with_name(name):
    print(f"Hello {name}")

greet_with_name("Angela")
greet_with_name("matt")

# positional arguments
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Jack Bauer", "Nowhere")

# keyword arguments
greet_with(location="London", name="Angela")