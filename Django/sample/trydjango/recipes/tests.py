from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
from .models import Recipe, RecipeIngredient
from django.core.exceptions import ValidationError


User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user(username="admin",password='1234')

    def test_user_pw(self):
        checked = self.user_a.check_password('1234')
        self.assertTrue(checked)

class RecipeTestCase(TestCase):

    def setUp(self):
        self.user_a = User.objects.create_user(username="admin",password='1234')
        self.recipe_a = Recipe.objects.create(
            name="Recipe 1",
            user = self.user_a,
        )
        self.recipeingredient_a = RecipeIngredient.objects.create(
            recipe = self.recipe_a,
            name = 'ingredient 1',
            quantity = '1/2',
            unit = 'pound',
        )
        self.recipeingredient_b = RecipeIngredient.objects.create(
            recipe = self.recipe_a,
            name = 'ingredient 1',
            quantity = 'a bit',
            unit = 'pound',
        )

    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)

    
    def test_user_recipe_reverse_count(self):
        user = self.user_a
        qs = user.recipe_set.all()

        self.assertEqual(qs.count(), 1)

    def test_user_recipe_forward_count(self):
        user = self.user_a
        qs = Recipe.objects.filter(user=user)

        self.assertEqual(qs.count(), 1)

    def test_recipe_ingredient_reverse_count(self):
        recipe = self.recipe_a
        qs = recipe.recipeingredient_set.all()
      
        self.assertEqual(qs.count(), 2)

    def test_recipe_ingredient_forward_count(self):
        recipe = self.recipe_a
        qs = RecipeIngredient.objects.filter(recipe=recipe)
      
        self.assertEqual(qs.count(), 2)

    def test_unit_measure_validation(self):
        valid_unit = 'pound'
        ingredient = RecipeIngredient(
            name = 'new',
            quantity = 1,
            recipe = self.recipe_a,
            unit = valid_unit
        )
        ingredient.full_clean()

    def test_unit_measure_validation_error(self):
        invalid_unit = 'nada'
        with self.assertRaises(ValidationError):
            ingredient = RecipeIngredient(
                name = 'new',
                quantity = 10,
                recipe = self.recipe_a,
                unit = invalid_unit
            )
            ingredient.full_clean()

    def test_quantity_as_float(self):
        self.assertIsNotNone(self.recipeingredient_a.quantity_as_float)
        self.assertIsNone(self.recipeingredient_b.quantity_as_float)