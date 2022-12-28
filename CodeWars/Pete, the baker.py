# Find out how many cakes Pete could bake considering his recipes.

def cakes(recipe, available):
    whole_cake = []
    for ingredient in recipe:
        if ingredient in available:
            whole_cake.append(ingredient)
        else:
            return 0
    max_ingredients = [(available[key] // recipe[key]) for key in whole_cake]
    return min(max_ingredients)

print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))