from pyramid.view import view_config
from pyramid.request import Request
from pyramid.httpexceptions import HTTPNotFound

#https://pypi.org/project/fastapi/

#Route :  /project/{package_name}/

@view_config(route_name='package_details',renderer='pypi_web:templates/packages/details.pt')
@view_config(route_name='package_details/',renderer='pypi_web:templates/packages/details.pt')
def details(request: Request):
    package_name = request.matchdict.get('package_name')
    if not package_name or package_name == 'gone':
        raise HTTPNotFound()
    return {'message': 'Hello World'}

