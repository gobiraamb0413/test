import os

# Saving the recipes to the file.
def saving_to_file(recipes):
    with open("w2212796_recipes.txt","w") as file:
        for recipe_id, recipe in recipes.items():
            file.write("===RECIPES===\n")
            file.write(f"ID: {recipe_id}\n")
            file.write(f"NAME: {recipe['name']}\n")
            file.write(f"CATEGORY: {recipe['category']}\n")
            file.write(f"TIME: {recipe['time']}\n")

            ingredients = "|".join([f"{ingredient[0]},{ingredient[1]},{ingredient[2]}" for ingredient in recipe["ingredients"]])
            file.write(f"INGREDIENTS: {ingredients}\n")

            tags = ",".join(recipe["tags"])
            file.write(f"TAGS: {tags}\n")

            file.write("===End===\n")

    print("Recipes are saved successfuly to the w2212796_recipes.txt file.")

# Loading the recipes from the file.
def loading_from_file(recipes):
    if not os.path.exists("w2212796_recipes.txt"):
        return 0
    
    count = 0 

    with open("w2212796_recipes.txt") as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        if "===RECIPES===" in lines[i]:

            recipe_id = lines[i+1].split(":")[1].strip()
            recipe_name = lines[i+2].split(":")[1].strip()
            cat = lines[i+3].split(":")[1].strip()
            time = lines[i+4].split(":", 1)[1].strip()

            ingredient_line = lines[i+5].split(":")[1].strip()
            ingredients = []

            if ingredient_line:
                for ing in ingredient_line.split("|"):
                    parts = ing.split(",")
                    if len(parts) == 3:
                        ingredient_name, quantity, unit = parts
                        ingredients.append((ingredient_name, float(quantity), unit))

            tag_line = lines[i+6].split(":", 1)[1].strip()
            tags = set(tag_line.split(",")) if tag_line else set()

            recipes[recipe_id] = {
                "name": recipe_name,
                "category": cat,
                "time": time,
                "ingredients": ingredients,
                "tags": tags
            }

            count = count + 1
            i = i + 8
        else:
            i = i + 1

    return count

# Exporting the recipes.
def exporting_recipe(recipes):
    recipe_id = input("Enter the recipe ID to export:")

    if recipe_id not in recipes:
        print("The recipe is not found.")
        return
    
    recipe = recipes[recipe_id]

    filename = f"recipe_{recipe["name"].replace(" ", "_")}.txt"

    try: 
        with open(filename, "w") as file:
            file.write(f"RECIPE: {recipe["name"]}\n")
            file.write("=" * 40 + "\n")
            file.write(f"Category: {recipe["category"]}\n")
            file.write(f"Time: {recipe["time"]}\n\n")

            file.write("INGREDIENTS:\n")
            for ingredient in recipe["ingredients"]:
                file.write(f"- {ingredient[0]}: {ingredient[1]} {ingredient[2]}\n")

            file.write("\nTAGS: " + ",".join(recipe["tags"]))

        print("Recipe is successfully exported.")

    except Exception as e:
        print("An error occured while exporting the recipe:", e)

     
