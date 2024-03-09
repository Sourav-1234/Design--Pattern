from abc import ABC,abstractmethod


#The Commodity that produced in the factory
#Pizza

#Abstract Class

class Pizza(ABC):
    @abstractmethod
    def make_pizza(self):
        pass


#Types of Pizza into the market 


class VegPizza(Pizza):
    def make_pizza(self):
        print("Veg Pizza is being made")

class NonVegPizza(Pizza):
    def make_pizza(self):
        print("Non Veg Pizza is being made")

class CheesePizza(Pizza):
    def make_pizza(self):
        print("Cheese pizza is being made")


#Creating a Factory for Producing the Pizza Store

#Abstract Class

class PizzaStore(ABC):
    @abstractmethod
    def create_pizza(self,pizza_type):
        pass
    def order_pizza(self,pizza_type):
        pizza=self.create_pizza(pizza_type)
        pizza.make_pizza()
        return pizza

#Adding the Concrete class for the PizzaStore

class IndianStore(PizzaStore):
    def create_pizza(self,pizza_type):
        if pizza_type=="Veg":

            return VegPizza()
        elif pizza_type=="NonVeg":
            return NonVegPizza()
        else:
            return ChessPizza()

    



class NewYorkStore(PizzaStore):
     def create_pizza(self,pizza_type):
        if pizza_type=="Veg":

            return VegPizza()
        elif pizza_type=="NonVeg":
            return NonVegPizza()
        else:
            return ChessPizza()

#Client Code 

if __name__ =='__main__':
    ny_store=NewYorkStore()
    ny_store.order_pizza("Veg")
    indian_store=IndianStore()
    indian_store.order_pizza("NonVeg")
