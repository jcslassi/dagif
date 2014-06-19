import json

from bottle import route, run, request
from giphypop  import Giphy
import requests

giphy = Giphy()

@route('/r', method=['POST', 'GET'])
def r():
    res = giphy.random_gif().next()
    gif_url = res['raw_data']['images']['original']['url']
    return json.dumps({"text": gif_url})

@route('/g', method=['POST'])
def g():
    search = request.forms.get('text')[3:]
    res = giphy.search(search).next()
    gif_url = res['raw_data']['images']['original']['url']
    return json.dumps({"text": gif_url})

if __name__ == '__main__':
    run(host="0.0.0.0", port=8080)
