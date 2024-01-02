from advanced.class02.class02_item import Item

#creating a separated class that inherit the functionalities
class Phone(Item):
    all = []
    def __init__(self, name: str, price: float, quantity=0, broken=0):
        #Call to super function
        super().__init__(
            name, price, quantity
        )

        #Run validations to the receiveed arguments
        assert broken >= 0, f'Broken phones {broken} is not greater than zero'

        #Assign to sefl object
        self.broken = broken

        #Actions to execute
        Phone.all.append(self)
