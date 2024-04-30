
from pypi_web.data.db_session import DBSession
from pypi_web.data.users import User


def user_count() -> int:
    session = DBSession.factory()
    return session.query(User).count()
