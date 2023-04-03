class Product:
    def __init__(self, product_id, name, price, colour_sample):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__colour_sample = colour_sample

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_name(self, name):
        self.__name = name
        
    def set_price(self, price):
        self.__price = price
        
    def set_colour_sample(self, colour_sample):
        self.__colour_sample = colour_sample

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price
    
    def get_colour_sample(self):
        return self.__colour_sample
    

class Employee:
    def __init__(self, employee_id, name, position):
        self.__employee_id = employee_id
        self.__name = name
        self.__position = position

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_name(self, name):
        self.__name = name
        
    def set_position(self, position):
        self.__position = position
        
    def get_employee_id(self):
        return self.__employee_id

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position
    
class customer:
    def __init__(self, customer_id, name, credit):
        self.__customer_id = customer_id
        self.__name = name
        self.__credit = credit

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_name(self, name):
        self.__name = name
        
    def set_credit(self, credit):
        self.__credit = credit
        
    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__credit
    
    