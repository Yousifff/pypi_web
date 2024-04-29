
import json
import os
import sys
import time
from typing import List, Optional, Dict

# noinspection PyPackageRequirements
import progressbar
from dateutil.parser import parse
from sqlalchemy.orm import Session, subqueryload

import pypi_web
from pypi_web.data.db_session import DBSession
from pypi_web.data.languages import ProgrammingLanguage
from pypi_web.data.licenses import License
from pypi_web.data.maintainers import Maintainer
from pypi_web.data.packages import Package
from pypi_web.data.releases import Release
from pypi_web.data.users import User
def main():
    pass