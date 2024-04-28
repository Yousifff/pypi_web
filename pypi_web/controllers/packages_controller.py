from pyramid.view import view_config
from pyramid.request import Request
from pyramid.httpexceptions import HTTPNotFound, HTTPFound


#https://pypi.org/project/fastapi/

#Route :  /project/{package_name}/

@view_config(route_name='package_details',renderer='pypi_web:templates/packages/details.pt')
@view_config(route_name='package_details/',renderer='pypi_web:templates/packages/details.pt')
def details(request: Request):
    package_name = request.matchdict.get('package_name')
    if not package_name:
        raise HTTPNotFound()
    return {'package_name': package_name}


#'/project/{package_name}/releases'
@view_config(route_name='releases',renderer='pypi_web:templates/packages/releases.pt')
@view_config(route_name='releases/',renderer='pypi_web:templates/packages/releases.pt')
def releases(request: Request):
    package_name = request.matchdict.get('package_name')
    if not package_name:
        raise HTTPNotFound()
    return {
        'package_name': package_name,
        'releases': []
    }

#/project/{package_name}/releases/{release_version}
@view_config(route_name='release_version',renderer='pypi_web:templates/packages/packages/release_version.pt')
def release_version(request: Request):
    package_name = request.matchdict.get('package_name')
    if not package_name:
        raise HTTPNotFound()
    return {
        'package_name': package_name,
        'release': []
    }


@view_config(route_name='popular',renderer='pypi_web:templates/packages/details.pt')
def popular(request: Request):
    num = int(request.matchdict.get('num',-1))
    if not (1 <= num or num <= 10):
        raise HTTPNotFound()

    return {
        'package_name': f'The  {num}th popular package'
    }