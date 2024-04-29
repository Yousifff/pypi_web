import os

import pypi_web
from pypi_web.data.db_session import DBSession
from pypi_web.data.packages import Package
from pypi_web.data.releases import Release


def main():
    init_db()

    while True:
        insert_a_package()
        break


def insert_a_package():
    p = Package()
    p.id = input("Enter Package Name: ")
    p.summary = input("Enter Package Summary: ")
    p.author = input("Enter Package Author: ")
    p.email = input("Enter Package Author Email: ")
    p.license = input("Enter Package License: ")

    r1 = Release()
    r1.major = input("Enter Package Major: ")
    r1.minor = input("Enter Package Minor: ")
    r1.build = input("Enter Package Build Version: ")
    r1.size = input("Enter Package Size: ")

    r2 = Release()
    r2.major = input("Enter Package Major: ")
    r2.minor = input("Enter Package Minor: ")
    r2.build = input("Enter Package Build Version: ")
    r2.size = input("Enter Package Size: ")


    p.releases.append(r1)
    p.releases.append(r2)

    session = DBSession.factory()

    session.add(p)

    session.commit()


def init_db():
    top_folder = os.path.dirname(pypi_web.__file__)
    rel_file = os.path.join('db', 'pypi.sqlite')
    db_file = os.path.join(top_folder, rel_file)
    DBSession.global_init(db_file)


if __name__ == '__main__':
    main()
