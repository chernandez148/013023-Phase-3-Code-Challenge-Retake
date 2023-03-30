class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        if not name:
            raise ValueError("Name cannot be empty.")
        self._name = name
        self._reviews = []
        self.__class__.all_restaurants.append(self)

    @property
    def name(self):
        return self._name

    @property
    def reviews(self):
        return self._reviews

    def add_review(self, review):
        from .review import Review
        if isinstance(review, Review):
            self._reviews.append(review)
        else:
            raise Exception("Review must be of type Review.")
        if review.restaurant != self:
            raise Exception("Review is not for this restaurant.")

    @property
    def customers(self):
        from .customer import Customer
        customers = set()
        for review in self._reviews:
            customers.add(review.customer)
        if customers and isinstance(next(iter(customers)), Customer):
            return list(customers)
        else:
            return []

    def average_star_rating(self):
        total_ratings = 0
        num_ratings = 0
        for review in self._reviews:
            total_ratings += review.rating
            num_ratings += 1
        if num_ratings == 0:
            return 0
        else:
            return total_ratings / num_ratings

    @classmethod
    def get_all_restaurants(cls):
        return cls.all_restaurants
