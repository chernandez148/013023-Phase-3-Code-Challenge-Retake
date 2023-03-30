from classes.customer import Customer
from classes.restaurant import Restaurant


class Review:
    def __init__(self, customer, restaurant, rating):
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be an instance of Customer class")
        if not isinstance(restaurant, Restaurant):
            raise TypeError(
                "Restaurant must be an instance of Restaurant class")
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise ValueError("Rating must be an integer between 1 and 5")

        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

        # Associate the review with the customer and restaurant
        self.customer.reviews.append(self)
        self.restaurant.reviews.append(self)

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int) or value < 1 or value > 5:
            raise ValueError("Rating must be an integer between 1 and 5")
        self._rating = value
