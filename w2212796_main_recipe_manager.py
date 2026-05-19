#This is the main file of the recipe manager program.

#Importing the necessary functions from the other python files.
from w2212796_recipe_menu_core_functions import *
from w2212796_searching_filtering import *
from w2212796_processing_statistics import *
from w2212796_file_handling import *

recipes = {}

recipe_counter = 1

#This is the main menu function.
def main_menu():
    global recipe_counter

    count = loading_from_file(recipes)

    if recipes:
        last_recipe_id = max(recipes.keys(), key=lambda x: int(x[3:]))
        recipe_counter = int(last_recipe_id[3:]) + 1

    if count:
        print(f"loaded {count} recipes successfully from the file.")
    else:
        print("No saved recipes found and loaded.")
    
    while True:
        print("\n=========================================================")
        print("     DIGITAL RECIPE BOOK MANAGER")
        print("=========================================================")
        print("1. Add Recipe")
        print("2. View All Recipes")
        print("3. View Recipes by ID")
        print("4. Search by Ingredient")
        print("5. Filter Recipes")
        print("6. Edit Recipe")
        print("7. Delete Recipe")
        print("8. View Statistics")
        print("9. Save Recipes")
        print("10. Export Recipe")
        print("11. Exit")

        try:
            choice = int(input("Enter your choice (1-11): "))

            if choice == 1:
                recipe_counter = adding_recipe(recipes, recipe_counter)
                saving_to_file(recipes)

            elif choice == 2:
                displaying_all(recipes)
            
            elif choice == 3:
                displaying_recipe(recipes)
            
            elif choice == 4:
                searching_ingrediant(recipes)

            elif choice == 5:
                filtering_recipes(recipes)

            elif choice == 6:
                editing_recipe(recipes)
            
            elif choice == 7:
                deleting_recipe(recipes)

            elif choice == 8:
                showing_statistics(recipes)

            elif choice == 9:
                saving_to_file(recipes)

            elif choice == 10:
                exporting_recipe(recipes)

            elif choice == 11:
                print("Auto Saving recipes before exiting.")
                saving_to_file(recipes)
                print("Exiting the program. Goodbye!")
                break

            else:
                print("The entered choice is invalid. Please enter a number between 1 to 11.")

        except ValueError:
            print("Enter a valid number as an input.")

        except Exception as e:
            print("An unexpected error occured.", e)


main_menu()
              
