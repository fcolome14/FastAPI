from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(pwd: str):
    """Creates encrypted password

    Args:
        pwd (str): _description_

    Returns:
        _type_: _description_
    """
    return pwd_context.hash(pwd)

def verify(plain_password, hash_password):
    return pwd_context.verify(plain_password, hash_password)