class Ingredient:
    def __innit__(self,name:str,quantity:float,unit:str):
        self.name=name
        self.quantity=quantity 
        self.unit=unit

    @property
    def quantity(self) -> float:
        return self._quantity

    @quantity.setter
    def quantity(self,value):
        if float(value)<=0:
            raise ValueError("Количество должно быть положительным")
        self._quantity=float(value)
    
    def __str__(self) -> str:
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self) -> str:
        return f"Ingredient('{self.name}',{self.quantity},'{self.unit}')"

    def __eq__(self, other) -> bool:
        if not isinstance(other,Ingredient):
            return NotImplemented
        return self.name==other.name and self.unit==other.unit