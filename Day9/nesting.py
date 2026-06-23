# In Nesting, we can have a list or dictionary in the dictionary.

capitals = {
    "France": "Paris",
    "Spain": "Madrid",
    "Italy": "Rome",
}

# Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lyon", "Marseille"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "Spain": {
        "numb_time_visited": 9,
        "cities_visited": ["Madrid", "Barcelona", "Valencia"]
    }
}

print(travel_log["France"][1])
print(travel_log["Spain"]["cities_visited"])


# Nested list
nested_list = ["A", "B", ["C", "D", "E"], "F"]
print(f"Letter {nested_list[2][1]}")