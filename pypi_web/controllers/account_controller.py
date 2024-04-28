

from pyramid.view import view_config



####################### Account Index #######################
@view_config(route_name='account_home', renderer='pypi_web:templates/account/index.pt')
def index(request):
    return {}

################### LOGIN ########################
@view_config(route_name='login', renderer='pypi_web:templates/account/login.pt',request_method='GET')
def login_get(request):
    return {}

@view_config(route_name='login', renderer='pypi_web:templates/account/login.pt',request_method='POST')
def login_post(request):
    return {}

####################### REGISTER ################
@view_config(route_name='register', renderer='pypi_web:templates/account/register.pt',request_method='GET')
def register_get(request):
    return {}

@view_config(route_name='register', renderer='pypi_web:templates/account/register.pt',request_method='POST')
def register_post(request):
    return {}

################## LOGOUT #####################
@view_config(route_name='logout', renderer='pypi_web:templates/account/logout.pt')
def logout(request):
    return {}