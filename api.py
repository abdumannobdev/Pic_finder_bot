import spoonacular as sp

def search_from_api(query):
    api = sp.API("668584543a0f48948d42408f93c840d7")
    response = api.search_recipes_by_ingredients()
    data = response.json()
    for recipe in data:
        title = recipe.get('title')
        img = recipe.get('image')