import os.path

from pypi_web.data.db_session import DBSession


def includeme(config):
    db_file = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            'db',
            'pypi.sqlite'
        ))

    DBSession.global_init(db_file)

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('about', '/about')
    config.add_route('package_details', '/project/{package_name}')
    config.add_route('package_details/', '/project/{package_name}/')

    config.add_route('popular', '/{num}', custom_predicates=[
        lambda info, _: info['match'].get('num', '').isdigit()
    ])
    config.add_route('releases', '/project/{package_name}/releases')
    config.add_route('releases/', '/project/{package_name}/releases/')
    config.add_route('release_version', '/project/{package_name}/releases/{release_version}')

    # Account controllers
    config.add_route('account_home', '/account/')
    config.add_route('login', '/account/login')
    config.add_route('register', '/account/register')
    config.add_route('logout', '/account/logout')

    config.add_route('cms_page', '*subpath')
