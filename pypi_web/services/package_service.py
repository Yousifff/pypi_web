from sqlalchemy.orm import Session

from pypi_web.data.db_session import DBSession
from pypi_web.data.packages import Package
from pypi_web.data.releases import Release


def package_count() -> int:
    session = DBSession.factory()
    return session.query(Package).count()

def release_count() -> int:
    session = DBSession.factory()
    return session.query(Release).count()

