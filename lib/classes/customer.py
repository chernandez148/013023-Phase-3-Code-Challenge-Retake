class Customer:
    def __init__(self, first_name, last_name):
        if not isinstance(first_name, str) or first_name == "":
            raise ValueError("First name must be a non-empty string")
        if not isinstance(last_name, str):
            raise ValueError("Last name must be a string")
        if not 1 <= len(first_name) <= 25 or not 1 <= len(last_name) <= 25:
            raise Exception(
                "First name and last name must be between 1 and 25 characters.")
        self._first_name = first_name
        self._last_name = last_name
        self._reviews = []

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str) or value == "":
            raise ValueError("First name must be a non-empty string")
        if not 1 <= len(value) <= 25:
            raise ValueError("First name must be between 1 and 25 characters.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Last name must be a string")
        if not 1 <= len(value) <= 25:
            raise ValueError("Last name must be between 1 and 25 characters.")
        self._last_name = value

    def get_num_reviews(self):
        return len(self._reviews)

    def create_review(self, restaurant, rating):
        from classes.review import Review
        review = Review(self, restaurant, rating)
        restaurant.add_review(review)
        self._reviews.append(review)

    @property
    def restaurants(self):
        return list(set([review.restaurant for review in self._reviews]))

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, reviews):
        self._reviews = reviews
