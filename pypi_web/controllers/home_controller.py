from pyramid.view import view_config
from pypi_web.services import package_service, user_service

def get_packages():
    return [
        {'name': 'FASTAPI', 'version': '2.0.0'},
        {'name': 'sqlalchmey', 'version': '1.2.0'},
        {'name': 'sqlite', 'version': ''}
    ]


@view_config(route_name='home', renderer='pypi_web:templates/home/home_index.pt')
def home_index(request):
    return {
        'packages': get_packages(),
        'package_count': package_service.package_count(),
        'release_count' : package_service.release_count(),
        'user_count': user_service.user_count()
    }


@view_config(route_name='about', renderer='pypi_web:templates/home/home_about.pt')
def about(request):
    return {'message': 'About PyPI!'}