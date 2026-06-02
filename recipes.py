class Ingredient:
    def __init__(self,name:str,quantity:float,unit:str):
        self.name=name
        self.quantity=quantity 
        self.unit=unit

    @property
    def quantity(self) -> float:
        return self._quantity

    @quantity.setter
    def quantity(self,value):
        value=float(value)
        if value<=0:
            raise ValueError("Количество должно быть положительным")
        self._quantity=value
    
    def __str__(self) -> str:
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self) -> str:
        return f"Ingredient('{self.name}',{self.quantity},'{self.unit}')"

    def __eq__(self, other) -> bool:
        if not isinstance(other,Ingredient):
            return NotImplemented
        return self.name==other.name and self.unit==other.unit

class Recipe:
    def __init__(self,title:str,ingredients:list=None):
        self.title=title
        self.ingredients=[]
        if ingredients:
            for i in ingredients:
                self.add_ingredient(i)
 
    def add_ingredient(self, ingredient: "Ingredient") -> None:
        for i in self.ingredients:
            if i==ingredient:
                i.quantity+=ingredient.quantity
                return
        self.ingredients.append(Ingredient(ingredient.name, ingredient.quantity, ingredient.unit))
 
    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        try:
            return float(ratio)>0
        except (TypeError,ValueError):
            return False
 
    def scale(self, ratio: float) -> "Recipe":
        if not self.is_valid_ratio(ratio):
            raise ValueError("Коэффициент должен быть положительным числом")
        new_recipe=Recipe(self.title)
        for i in self.ingredients:
            new_recipe.ingredients.append(Ingredient(i.name,i.quantity*ratio,i.unit))
        return new_recipe
 
    def __len__(self) -> int:
        return len(self.ingredients)
 
    def __str__(self) -> str:
        lines=[f"Рецепт: {self.title}"]
        for i in self.ingredients:
            lines.append(f"  - {i}")
        return "\n".join(lines)
 
 