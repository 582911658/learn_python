class Restaurant():
    """
    餐馆类
    """

    def __init__(self, restaurant_name, cuisine_type):
        """
        类的初始化
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """
        餐厅描述
        """
        print(self.restaurant_name.title())
        print(self.cuisine_type.title())

    def open_restaurant(self):
        """
        餐厅开门
        """
        print(self.restaurant_name.title()+' is now opening!')


restaurant = Restaurant('calories', 'westland')
restaurant.describe_restaurant()
restaurant = Restaurant('calo', 'wes')
restaurant.describe_restaurant()
restaurant = Restaurant('ca', 'west')
restaurant.describe_restaurant()
