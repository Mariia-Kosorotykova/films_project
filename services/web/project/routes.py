"""This module implements routes for project"""


from . import api
from .resources.director_resources import DirectorResource
from .resources.movie_resources import MovieResource, MovieListResource
from .resources.user_resources import UserListResource


route = api.add_resource

route(UserListResource, '/users')

route(DirectorResource, '/directors/<int:director_id>')

route(MovieListResource, '/movie')
route(MovieResource, '/movie/<int:movie_id>')
