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

class TestIngredient:
    def test_init_attributes(self):
        ing=Ingredient("Гуанчале",150,"г")
        assert ing.name=="Гуанчале"
        assert ing.quantity==150.0
        assert ing.unit=="г"

    def test_quantity_is_float(self):
        ing=Ingredient("Яйца",4,"шт")
        assert isinstance(ing.quantity,float)

    def test_quantity_positive_raises(self):
        with pytest.raises(ValueError,match="Количество должно быть положительным"):
            Ingredient("Пармезан",-1,"г")

    def test_quantity_zero_raises(self):
        with pytest.raises(ValueError):
            Ingredient("Пармезан",0,"г")

    def test_quantity_setter_validates(self):
        ing=Ingredient("Гуанчале",150,"г")
        with pytest.raises(ValueError):
            ing.quantity=-50

    def test_str(self):
        ing=Ingredient("Пармезан",100,"г")
        assert str(ing)=="Пармезан: 100.0 г"

    def test_repr(self):
        ing=Ingredient("Пармезан",100,"г")
        assert repr(ing)=="Ingredient('Пармезан',100.0,'г')"

    def test_eq_same_name_and_unit(self):
        a=Ingredient("Масло",50,"г")
        b=Ingredient("Масло",100,"г")
        assert a==b

    def test_eq_different_name(self):
        a=Ingredient("Масло",100,"г")
        b=Ingredient("Пармезан",100,"г")
        assert a!=b

    def test_eq_different_unit(self):
        a=Ingredient("Масло",100,"г")
        b=Ingredient("Масло",100,"мл")
        assert a!=b

