class Book:
    def __init__(self, title, author, year):
        """
        Constructor method. Initializes a new Book instance with the given title, author, and publication year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor method. Called when the object is about to be destroyed.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation method. Returns a readable string format for printing.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation method. Returns a string that could recreate this object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
