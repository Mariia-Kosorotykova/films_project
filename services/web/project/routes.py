"""This module implements routes for project"""


from . import api
from .resources.director_resources import DirectorResource
from .resources.movie_resources import MovieResource, MovieListResource
from .resources.user_resources import UserListResource

from .resources.login_logout import LoginResource, LogoutResource

route = api.add_resource

route(UserListResource, '/users')

route(DirectorResource, '/directors/<int:director_id>')

route(MovieResource, '/movies/<int:movie_id>')
route(MovieListResource, '/movies')

route(LoginResource, '/login')
route(LogoutResource, '/logout')
