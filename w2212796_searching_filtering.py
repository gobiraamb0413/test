# Converting time to minutes.
def converting_time_to_minutes(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes

# Searching recipe by the ingredients.
def searching_ingrediant(recipes):
    keys = input("Enter the ingredients of the recipe that you are searching for(comma should be separated): ").lower().split(",")
    keys = [key.strip() for key in keys]

    results = []

    for recipe_id, recipe in recipes.items():
        names = [i[0].lower() for i in recipe["ingredients"]]

        if all(any(key in name for name in names) for key in keys):
            results.append((recipe_id, recipe["name"]))

    print(results if results else "No recipes are found with the given ingredients.")

# Filtering recipes.
def filtering_recipes(recipes):
    minimum_time = int(input("Enter the minimum time: "))
    maximum_time = int(input("Enter the maximum time: "))
    minimum_ingredients = int(input("Enter the minimum number of ingredients: "))
    maximum_ingredients = int(input("Enter the maximum number of ingedients: "))

    results = []

    for recipe_id, recipe in recipes.items():
        time = converting_time_to_minutes(recipe["time"])

        if minimum_time <= time <= maximum_time and minimum_ingredients <= len(recipe["ingredients"]) <= maximum_ingredients:
            results.append((recipe_id, recipe["name"]))

    print(results if results else "No recipe matches are found.")
