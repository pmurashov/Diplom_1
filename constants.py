from dataclasses import dataclass
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

class ListIngredient:

    LIST_BUNS =[
                ['Флюоресцентная булка R2-D3', 988],
                ['Краторная булка N-200i', 1255]
            ]
    LIST_INGREDIENT_FILLINGS =[
                ['Мясо бессмертных моллюсков Protostomia', 1337],
                ['Говяжий метеорит (отбивная)', 3000],
                ['Биокотлета из марсианской Магнолии', 424],
                ['Филе Люминесцентного тетраодонтимформа', 988],
                ['Хрустящие минеральные кольца', 300],
                ['ПлодыФалленианского дерева', 874],
                ['Кристаллы марсианских альфа-сахаридов', 762],
                ['Мини-салат Экзо-Плантаго', 4400],
                ['Сыр с астероидной плесенью', 4142]
            ]
    LIST_INGREDIENT_SAUCE =[
                ['Соус Spicy-X', 90],
                ['Соус фирменный Space Sauce', 80],
                ['Соус традиционный галактический', 15],
                ['Соус с шипами Антарианского плоскоходца', 88],
            ]
@dataclass
class Ingredient:
        type: str
        name: str
        price: float

filling = Ingredient(type = INGREDIENT_TYPE_FILLING, name = 'Сыр с астероидной плесенью',price = 200)
sauce = Ingredient(type = INGREDIENT_TYPE_SAUCE,name ='Соус фирменный Space Sauce',price = 100)