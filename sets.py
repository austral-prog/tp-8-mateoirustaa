from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    for element in dish_ingredients:
        set_ingredients = set(dish_ingredients)
        return (dish_name, set_ingredients)


def check_drinks(drink_name, drink_ingredients):
    set_ingredients = set(drink_ingredients)
    interseccion = set_ingredients.intersection(ALCOHOLS)
    print(interseccion)
    if interseccion != set():
        return (f"{drink_name} Cocktail")
    else:
        return (f"{drink_name} Mocktail")
    
print(check_drinks('Bannana Punch', ['banana', 'ginger ale', 'lemonade', 'orange juice', 'pineapple juice', 'sugar', 'water']))
