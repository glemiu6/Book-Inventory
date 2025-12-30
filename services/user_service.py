from database.models import User
from exceptions.user_exceptions import InvalidUserData,UserNotFoundError
from database.queries import insert_user, add_book_user


def create_user(db,user:str,email:str)->User:
    if not user.strip():
        raise InvalidUserData('Username Invalid')
    if not email.strip() or email.split('@')[1] not in ["gmail.com","yahoo.com","mail.com","outlook.com"]:
        raise InvalidUserData('Email Invalid')

    return insert_user(db,user,email)

def assign_book_to_user(db,user_id:int,book_id:int)->None:
    if not isinstance(user_id,int):
        raise InvalidUserData('User ID Invalid')
    if not isinstance(book_id,int):
        raise InvalidUserData('Book ID Invalid')
    add_book_user(db,user_id,book_id)


def get_user_books(db,user_id:int)->list:
    if not isinstance(user_id,int):
        raise InvalidUserData('User ID Invalid')
    user_books=get_user_books(db,user_id)
    if not user_books:
        raise UserNotFoundError('User Books Not Found')

    return [ub.book for ub in user_books]
