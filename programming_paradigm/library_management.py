# library_management.py

class Book:
    """
    Represents a book with a title, author, and checkout status.
    """
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self) -> bool:
        """
        Marks the book as checked out if it isn't already.
        Returns True if successful, False if the book was already checked out.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self) -> bool:
        """
        Marks the book as returned (available) if it was checked out.
        Returns True if successful, False if the book was not checked out.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self) -> bool:
        """
        Returns True if the book is available for checkout.
        """
        return not self._is_checked_out


class Library:
    """
    Manages a collection of Book instances.
    """
    def __init__(self):
        self._books = []

    def add_book(self, book: Book) -> None:
        """
        Adds a new Book to the library's collection.
        """
        self._books.append(book)

    def check_out_book(self, title: str) -> bool:
        """
        Finds a book by title and checks it out.
        Returns True if the checkout was successful, False otherwise.
        """
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False

    def return_book(self, title: str) -> bool:
        """
        Finds a book by title and returns it.
        Returns True if the return was successful, False otherwise.
        """
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False

    def list_available_books(self) -> None:
        """
        Prints all books in the library that are currently available.
        """
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
