from pyramid.view import view_config



#https://pypi.org/project/fastapi/

#Route :  /project/{package_name}/

@view_config(route_name='package_details',renderer='pypi_web:templates/packages/details.pt')
@view_config(route_name='package_details/',renderer='pypi_web:templates/packages/details.pt')
def details(request):
    return {'message': 'Hello World'}

