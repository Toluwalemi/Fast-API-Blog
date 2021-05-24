from blog.helpers.db_helpers import pwd_context


def bcrypt(password: str):
    return pwd_context.hash(password)


def verify(hashed_password, plain_password):
    return pwd_context.verify(plain_password, hashed_password)
