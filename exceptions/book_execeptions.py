class BookError(Exception):
    """Base Exception for the book-related errors"""

    pass


class BookNotFoundError(BookError):
    """Raised when a book is not found"""

    pass


class DuplicateBook(BookError):
    """Raised when there is a duplicate book"""

    pass


class InvalidBookData(BookError):
    """Raised when there is invalid data for a book"""

    pass
