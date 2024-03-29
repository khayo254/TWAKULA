from flask import Blueprint, request, jsonify


recipebp = Blueprint('recipe', __name__)

recipes = []

@recipebp.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.json
    
    name = data.get('name')
    ingredients = data.get('ingredients')
    instructions = data.get('instructions')
    
    if not name or not instructions or not ingredients:
        return jsonify({"error": "Name, ingredients, and instructionsare cannot be empty"}), 400
    
    recipe = {"id": len(recipes) + 1,"name": name, "ingredients": ingredients, "instructions": instructions}
    recipes.append(recipe)
    
    return jsonify({"message": "Recipe created sucessfully", "recipe": recipe}), 201

@recipebp.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    data = request.json
    
    new_name = data.get('name')
    new_ingredients = data.get('ingredients')
    new_instructions = data.get('instructions')
    
    recipe = next((r for r in recipes if r['id']) == recipe_id, None)
    
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404
    
    if new_name:
        recipe['name'] = new_name
    if new_ingredients:
        recipe['ingredients'] = new_ingredients
    if new_instructions:
        recipe['instructions'] = new_instructions
        
    return jsonify({"message": f"Recipe {recipe_id} updated successfully", "recipe": recipe}), 200

@recipebp.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404
    
    return jsonify({"recipe": recipe}), 200

@recipebp.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = next((r for r in recipes if r['id'] == recipe_id), None)
    
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404
    
    recipes.remove(recipe)
    
    return jsonify({"message": f"Recipe {recipe_id} deleted successfully"}), 200