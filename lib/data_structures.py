spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return[food["name"]for food in spicy_foods]
print(get_names(spicy_foods))


def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods
print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        # Extract information about the food
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]

        # Create the heat level emojis
        heat_emojis = "🌶" * heat_level

        # Print the formatted output
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return next((food for food in spicy_foods if food["cuisine"] == cuisine), None)

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        #extract information about the food
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]

        #create the heat level emojis
        heat_emojis = "🌶" * heat_level

        if heat_level > 5:
            print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

def get_average_heat_level(spicy_foods):
   total_heat_level = sum(food["heat_level"] for food in spicy_foods)
   num_len = len(spicy_foods)
   if num_len == 0:
       return 0
   else:
       return total_heat_level / num_len

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
