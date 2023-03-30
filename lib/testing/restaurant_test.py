from classes.restaurant import Restaurant
from classes.customer import Customer
from classes.review import Review
import pytest


class TestRestaurant:
    '''Restaurant in restaurant.py'''

    def test_has_name(self):
        '''has the name passed into __init__'''
        restaurant = Restaurant("Mels")
        assert (restaurant.name == "Mels")
        with pytest.raises(Exception):
            Restaurant(False)

    def test_name_setter(self):
        '''cannot change name'''
        restaurant = Restaurant("Mels")
        with pytest.raises(Exception):
            restaurant.name = 'Chipotle'
        assert (restaurant.name == "Mels")

    def test_has_many_reviews(self):
        '''restaurant has many reviews .'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert (len(restaurant.reviews) == 2)
        assert (review_1 in restaurant.reviews)
        assert (review_2 in restaurant.reviews)

    def test_has_many_customers(self):
        '''restaurant has many customers.'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        customer_2 = Customer('Dima', 'Bay')
        Review(customer, restaurant, 2)
        Review(customer_2, restaurant, 5)

        assert (len(restaurant.reviews) == 2)
        assert (customer in restaurant.customers)
        assert (customer_2 in restaurant.customers)

    def test_average(self):
        '''test average_star_rating()'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        customer_2 = Customer('Dima', 'Bay')
        Review(customer, restaurant, 2)
        Review(customer_2, restaurant, 5)

        assert (restaurant.average_star_rating() == 3.5)

    def test_get_all_restaurants(self):
        '''test get_all_restaurants() class method'''
        Restaurant.all = []
        Restaurant("Mel's")
        Restaurant("Arnold's")

        assert (len(Restaurant.get_all_restaurants()) == 12)
