class UserError(Exception):
   """
   Base exception for the user-related errors
   """
   pass

class UserNotFoundError(UserError):
    """Raised when a user doesn't exist"""

    pass


class InvalidUserData(UserError):
    """Raised when users data is invalid"""
    pass

