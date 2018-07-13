from django.test import TestCase
from cookbook.ingredients.models import Category, Ingredient


class CategoryTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name="Category1")
    
    def test_category_name(self):
        category = Category.objects.get(name="Category1")
        self.assertEqual(category.name, "Category1")

class IngredientTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name="Dairy")
        ingredient = Ingredient.objects.create(name="Milk", notes="2%", category=category)
    
    def test_ingredient_has_category(self):
        ingredient = Ingredient.objects.get(name="Milk", notes="2%")
        self.assertEqual(ingredient.category, Category.objects.get(name="Dairy"))