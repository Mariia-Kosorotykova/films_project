"""This module implements pagination"""


from flask import abort, jsonify, request, abort

from . import app
from .resources.movie_resources import MovieListResource

def get_paginated_list(results, url, start, limit):
    start = int(start)
    limit = int(limit)
    count = len(results)
    if count < start:
        abort(404)

    obj = {'start': start, 'limit': limit, 'count': count}

    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)

    obj['results'] = results[(start - 1):(start - 1 + limit)]
    return obj

@app.route('/movies_list', methods=['GET'])
def movies_list_pagination():
    return jsonify(get_paginated_list(
        MovieListResource.get(),
        '/movies_list',
        start=request.args.get('start', 1),
        limit=request.args.get('limit', 5)
    ))
