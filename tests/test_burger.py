import pytest
from burger import Burger
from constants import ListIngredient
from unittest.mock import Mock,patch
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestBurger:
    def test_check_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "White bun"
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


    @pytest.mark.parametrize('name_ingredient', (
            [
                ['Соус Spicy-X'],
                ['Соус фирменный Space Sauce'],
                ['Соус традиционный галактический'],
                ['Соус с шипами Антарианского плоскоходца'],
                ['Мясо бессмертных моллюсков Protostomia'],
                ['Говяжий метеорит (отбивная)'],
                ['Биокотлета из марсианской Магнолии'],
                ['Филе Люминесцентного тетраодонтимформа'],
                ['Хрустящие минеральные кольца'],
                ['ПлодыФалленианского дерева'],
                ['Кристаллы марсианских альфа-сахаридов'],
                ['Мини-салат Экзо-Плантаго'],
                ['Сыр с астероидной плесенью']
            ]
    ))
    def test_check_add_ingredient(self,name_ingredient):
        burger = Burger()
        burger.ingredients = []
        burger.add_ingredient(name_ingredient)
        assert name_ingredient in burger.ingredients


    def test_check_remove_ingredient(self):
        burger = Burger()
        burger.ingredients = [ListIngredient.LIST_INGREDIENT_FILLINGS, ListIngredient.LIST_INGREDIENT_SAUCE]
        burger.remove_ingredient(0)
        assert 'Мясо бессмертных моллюсков Protostomia' not in burger.ingredients


    def test_move_ingredient(self):
        burger = Burger()
        burger.ingredients = [ListIngredient.LIST_INGREDIENT_FILLINGS, ListIngredient.LIST_INGREDIENT_SAUCE]
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ListIngredient.LIST_INGREDIENT_SAUCE, ListIngredient.LIST_INGREDIENT_FILLINGS]


    def test_check_get_price(self):
        burger = Burger()
        mock_price_bun = Mock()
        mock_price_bun.get_price.return_value= 300

        mock_price_sauce = Mock()
        mock_price_sauce.get_price.return_value = 200

        mock_price_filling = Mock()
        mock_price_filling.get_price.return_value = 100

        burger.bun = mock_price_bun
        burger.ingredients = [mock_price_filling, mock_price_sauce]
        assert burger.get_price() == 900


    @patch('burger.Burger.get_price', return_value=300)
    def test_check_get_receipt(self,mock_get_price):

        mock_name_bun = Mock()
        mock_name_bun.get_name.return_value = 'Краторная булка N-200i'

        mock_name_sauce = Mock()
        mock_name_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_name_sauce.get_name.return_value = 'Соус фирменный Space Sauce'

        mock_name_filling = Mock()
        mock_name_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_name_filling.get_name.return_value = 'Сыр с астероидной плесенью'

        burger = Burger()
        burger.bun = mock_name_bun
        burger.ingredients = [mock_name_sauce, mock_name_filling]

        expected_receipt = (
            '(==== Краторная булка N-200i ====)\n'
            '= sauce Соус фирменный Space Sauce =\n'
            '= filling Сыр с астероидной плесенью =\n'
            '(==== Краторная булка N-200i ====)\n'
            '\n'
            'Price: 300'
        )
        assert burger.get_receipt() == expected_receipt



