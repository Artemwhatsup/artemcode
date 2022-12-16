#!/usr/bin/env python
# coding: utf-8

# In[16]:


class auto:
    def __init__(self, color, look, horsepower, wheeldrive, price):
        self.color = color
        self.look = look
        self.horsepower = horsepower
        self.wheeldrive = wheeldrive
        self.price = price

    def __str__(self):
        return f" цвет: {self.color}, комплектация: {self.look} ,  л/с {self.horsepower} , привод {self.wheeldrive} . Стоимость: {self.price} руб."
    
class bmw:
    def __init__(self, color, look, horsepower, wheeldrive, price):
        super().___init___(self, color, look, horsepower, wheeldrive, price)

bmw = auto("red", "race", 500, "RWD", 500000)
bmw.__str__()
print(bmw.__str__())


class audi:
    def __init__(self, color, look, horsepower, wheeldrive, price):
        super().___init___(self, color, look, horsepower, wheeldrive, price)

audi = auto("black", "stock", 400, "4WD", 450000)
audi.__str__()
print(audi.__str__())

class honda:
    def __init__(self, color, look, horsepower, wheeldrive, price):
        super().___init___(self, color, look, horsepower, wheeldrive, price)

honda = auto("yellow", "offroad", 350, "FWD", 650000)
honda.__str__()
print(honda.__str__())


    


# In[ ]:




