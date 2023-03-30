from classes.restaurant import Restaurant
from classes.customer import Customer
from classes.review import Review
import pytest


class TestCustomer:
    '''Customer in customer.py'''

    def test_has_name(self):
        '''sets first and last name properties on init, validates, and returns full name.'''
        with pytest.raises(Exception):
            Customer(43)
        customer = Customer('Bruce', 'Wayne')
        assert (customer.first_name == "Bruce")
        assert (customer.last_name == "Wayne")
        assert (customer.full_name == 'Bruce Wayne')
        with pytest.raises(Exception):
            customer.first_name = True
        with pytest.raises(Exception):
            customer.first_name = "a"*26
        with pytest.raises(Exception):
            customer.first_name = ""
        customer.first_name = "Bat"
        customer.last_name = "Man"
        assert (customer.first_name == "Bat")
        assert (customer.last_name == "Man")
        assert (customer.full_name == "Bat Man")

    def test_has_many_reviews(self):
        '''customer has many reviews'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert (len(restaurant.reviews) == 2)
        assert (review_1 in customer.reviews)
        assert (review_2 in customer.reviews)

    def test_has_many_restaurants(self):
        '''customer has many restaurants.'''
        restaurant = Restaurant("Mels")
        restaurant_2 = Restaurant("Chipotle")

        customer = Customer('Steve', 'Wayne')
        customer_2 = Customer('Dima', 'Bay')
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant_2, 5)

        assert (restaurant in customer.restaurants)
        assert (restaurant_2 in customer.restaurants)

    def test_get_number_of_reviews(self):
        '''test get_number_of_reviews()'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert (customer.get_num_reviews() == 2)

    def test_create_review(self):
        '''test create_review()'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert (customer.get_num_reviews() == 2)
        customer.create_review(restaurant, 1)
        assert (len(customer.reviews) == 4)
        assert (customer.reviews[2].rating == 1)
        assert (customer.reviews[2].restaurant == restaurant)
