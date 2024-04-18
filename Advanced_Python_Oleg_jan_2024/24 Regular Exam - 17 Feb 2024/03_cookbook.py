
def cookbook(*recipes_data):

    all_recipes_dict = {}

    for recipe in recipes_data:
        name, type_cuisine, ingred = recipe

        if type_cuisine not in all_recipes_dict:
            all_recipes_dict[type_cuisine] = []
        all_recipes_dict[type_cuisine].append((name, ingred))

    sorted_all_recipes_dict = sorted(all_recipes_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""

    for type_cuisine, recipes_list in sorted_all_recipes_dict:
        result += (f"{type_cuisine} cuisine contains {len(recipes_list)} recipes:\n")

        for recipe in sorted(recipes_list):
            recipe_name, ingred = recipe
            result += (f"  * {recipe_name} -> Ingredients: {', '.join(ingred)}\n")

    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))

print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
    ))

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))

