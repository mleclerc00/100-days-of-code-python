programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieve from dictionary
print(programming_dictionary["Function"])

# Add to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

# Create empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary["Bug"])

# Loop through dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting list in dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting dictionary in dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting dictionary inside list
travel_log = [
    {
      "country": "France",
      "cities_visited": ["Paris", "Lille", "Dijon"],
      "total_visits": 12
    },
    {
      "country": "Germany",
      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
      "total_visits": 5
    },
]
