import pdb
import json

from giphypop  import Giphy
from bottle import route, run, request
import requests

giphy = Giphy()

FUNCTIONS = ['random_gif']

@route('/r', method=['POST', 'GET'])
def r():
    res = getattr(globals()['giphy'], 'random_gif')()
    gif_url = res['raw_data']['images']['original']['url']
    return json.dumps({"text": gif_url})

@route('/g', method=['POST', 'GET'])
def g():
    search = request.forms.get('text')[3:]
    res = giphy.search(search).next()
    #pdb.set_trace()
    gif_url = res['raw_data']['images']['original']['url']
    return json.dumps({"text": gif_url})

run(host="0.0.0.0", port=8080)
