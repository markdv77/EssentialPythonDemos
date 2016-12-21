import json

from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {
        'project': 'MyPyCharmWebApp',
        'classname': 'Essential Python'
    }


@view_config(route_name='weather')
def weather(request):

    town = request.matchdict['town'].lower()
    precision = int(request.params.get('precision', 3))

    if town in ('ravenna', 'utrecht'):
        r = {
            'weather': 'Sunny',
            'founding_date': 50,
            'town': town,
            'precision': precision
        }
        return Response(json.dumps(r))
    else:
        return Response("I am sorry, I don't have a forecast for " + town)

