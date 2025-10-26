"""
Example usage and testing script for the Dish Carbon Calculator
"""

from app import (
    extract_ingredients, 
    calculate_carbon_footprint, 
    get_suggestions,
    CARBON_FOOTPRINT_DATA
)

def test_ingredient_extraction():
    """Test ingredient extraction from text"""
    print("=== Testing Ingredient Extraction ===")
    
    test_descriptions = [
        "a plate of beef steak with potatoes and broccoli",
        "chicken pasta with tomato sauce and cheese",
        "vegan lentil curry with rice",
        "salmon sushi with avocado"
    ]
    
    for desc in test_descriptions:
        ingredients = extract_ingredients(desc)
        print(f"\nDescription: {desc}")
        print(f"Found ingredients: {ingredients}")

def test_carbon_calculation():
    """Test carbon footprint calculation"""
    print("\n\n=== Testing Carbon Footprint Calculation ===")
    
    test_meals = [
        {
            'name': 'Beef Meal',
            'ingredients': ['beef', 'potatoes', 'broccoli']
        },
        {
            'name': 'Chicken Pasta',
            'ingredients': ['chicken', 'pasta', 'tomatoes', 'cheese']
        },
        {
            'name': 'Vegan Curry',
            'ingredients': ['lentils', 'rice', 'onions', 'carrots']
        },
        {
            'name': 'Fish Dish',
            'ingredients': ['salmon', 'rice', 'avocado']
        }
    ]
    
    for meal in test_meals:
        total, breakdown = calculate_carbon_footprint(meal['ingredients'])
        print(f"\n{meal['name']}:")
        print(f"Total CO2: {total:.2f} kg")
        print("Breakdown:")
        for item in breakdown:
            print(f"  - {item['ingredient']}: {item['total_co2']:.2f} kg CO2")
        
        suggestions = get_suggestions(total, meal['ingredients'])
        print("Suggestions:")
        for sug in suggestions:
            print(f"  {sug}")

def compare_meals():
    """Compare carbon footprint of different meal choices"""
    print("\n\n=== Meal Comparison ===")
    
    meals = {
        'Beef Burger': ['beef', 'cheese', 'bread'],
        'Chicken Sandwich': ['chicken', 'bread', 'lettuce', 'tomatoes'],
        'Veggie Burger': ['lentils', 'bread', 'lettuce', 'tomatoes']
    }
    
    results = []
    for name, ingredients in meals.items():
        total, _ = calculate_carbon_footprint(ingredients)
        results.append((name, total))
    
    # Sort by carbon footprint
    results.sort(key=lambda x: x[1])
    
    print("\nMeals ranked by carbon footprint (lowest to highest):")
    for i, (name, footprint) in enumerate(results, 1):
        print(f"{i}. {name}: {footprint:.2f} kg CO2e")
        
    print(f"\nSwitching from {results[-1][0]} to {results[0][0]} saves " 
          f"{results[-1][1] - results[0][1]:.2f} kg CO2e per meal!")

def display_ingredient_database():
    """Display all ingredients in the database"""
    print("\n\n=== Ingredient Carbon Database ===")
    print(f"Total ingredients: {len(CARBON_FOOTPRINT_DATA)}")
    
    # Sort by carbon footprint
    sorted_ingredients = sorted(
        CARBON_FOOTPRINT_DATA.items(), 
        key=lambda x: x[1], 
        reverse=True
    )
    
    print("\nTop 10 Highest Carbon Footprint Ingredients:")
    for i, (ingredient, footprint) in enumerate(sorted_ingredients[:10], 1):
        print(f"{i}. {ingredient.title()}: {footprint} kg CO2e/kg")
    
    print("\nTop 10 Lowest Carbon Footprint Ingredients:")
    for i, (ingredient, footprint) in enumerate(sorted_ingredients[-10:], 1):
        print(f"{i}. {ingredient.title()}: {footprint} kg CO2e/kg")

if __name__ == "__main__":
    print("🌱 Dish Carbon Calculator - Testing Suite\n")
    
    test_ingredient_extraction()
    test_carbon_calculation()
    compare_meals()
    display_ingredient_database()
    
    print("\n\n✅ All tests completed!")
    print("\nTo run the full application, use: streamlit run app.py")
