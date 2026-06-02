import pytest
from recipes import Ingredient,Recipe,ShoppingList
class TestRecipe:
    def test_init_attributes(self):
        recipe=Recipe("Карбонара",[Ingredient("Спагетти",200,"г")])
        assert recipe.title=="Карбонара"
        assert len(recipe.ingredients)==1

    def test_init_empty_ingredients(self):
        recipe=Recipe("Карбонара")
        assert recipe.ingredients==[]

    def test_add_ingredient_new(self):
        recipe=Recipe("Карбонара")
        ing=Ingredient("Гуанчале",150,"г")
        recipe.add_ingredient(ing)
        assert len(recipe)==1

    def test_add_ingredient_duplicate_sums_quantity(self):
        recipe=Recipe("Карбонара")
        recipe.add_ingredient(Ingredient("Пармезан",50,"г"))
        recipe.add_ingredient(Ingredient("Пармезан",30,"г"))
        assert len(recipe)==1
        assert recipe.ingredients[0].quantity==80.0

    def test_scale_returns_new_recipe(self):
        recipe=Recipe("Карбонара",[Ingredient("Спагетти",200,"г")])
        scaled=recipe.scale(2)
        assert scaled is not recipe
        assert recipe.ingredients[0].quantity==200.0

    def test_scale_multiplies_quantities(self):
        recipe=Recipe("Карбонара",[Ingredient("Спагетти",200,"г"),Ingredient("Яйца",4,"шт")])
        scaled=recipe.scale(3)
        assert scaled.ingredients[0].quantity==600.0
        assert scaled.ingredients[1].quantity==12.0

    def test_scale_invalid_ratio_raises(self):
        recipe=Recipe("Карбонара",[Ingredient("Спагетти",200,"г")])
        with pytest.raises(ValueError):
            recipe.scale(0)
        with pytest.raises(ValueError):
            recipe.scale(-1)

    def test_scale_non_numeric_raises(self):
        recipe=Recipe("Карбонара",[Ingredient("Спагетти",200,"г")])
        with pytest.raises(ValueError):
            recipe.scale("много")

    def test_len(self):
        recipe=Recipe("Карбонара",[
            Ingredient("Спагетти",200,"г"),
            Ingredient("Гуанчале",150,"г")
        ])
        assert len(recipe)==2

    def test_is_valid_ratio_true(self):
        assert Recipe.is_valid_ratio(1) is True
        assert Recipe.is_valid_ratio(0.5) is True
        assert Recipe.is_valid_ratio(1000) is True

    def test_is_valid_ratio_false(self):
        assert Recipe.is_valid_ratio(0) is False
        assert Recipe.is_valid_ratio(-3) is False
        assert Recipe.is_valid_ratio("abc") is False
        assert Recipe.is_valid_ratio(None) is False

    def test_str(self):
        recipe=Recipe("Карбонара",[Ingredient("Спагетти",200,"г")])
        assert str(recipe)=="Рецепт: Карбонара\n  - Спагетти: 200.0 г"

    def test_init_merges_duplicate_ingredients(self):
        recipe=Recipe("Тест",[
            Ingredient("Мука",100,"г"),
            Ingredient("Мука",50,"г")
        ])
        assert len(recipe)==1
        assert recipe.ingredients[0].quantity==150.0
        