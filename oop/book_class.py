class Book:
    def __init__(self, title: str, author: str, year: int):
        """
        Initialize a Book instance with a title, author, and publication year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor that notifies when a Book instance is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self) -> str:
        """
        Human-readable string representation.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """
        Official string representation that can be used to recreate the instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
