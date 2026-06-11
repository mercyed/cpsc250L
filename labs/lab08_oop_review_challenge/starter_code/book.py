# Lab 8: OOP Review Challenge


class Book:
    def __init__(self, title, author, year, genre, pages, rating):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages
        self.rating = rating
        self.quantity = 0

    def add_stock(self, amount):
        """
        Increase quantity by amount.
        """
        pass

    def sell_copies(self, amount):
        """
        Decrease quantity by amount if enough copies are available.

        Return True if the sale succeeds.
        Return False otherwise.
        """

        if amount <= self.quantity:
            self.quantity += amount
            return True

        return False

    def __str__(self):


    def __lt__(self, other):
        """
        Compare books alphabetically by title.
        """
        pass
