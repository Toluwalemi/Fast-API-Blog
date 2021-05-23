from blog.helpers.db_helpers import pwd_context


def bcrypt(password: str):
    return pwd_context.hash(password)