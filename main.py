import json
import logging

from bottle import route, run, request
from giphypop  import Giphy
import requests

ITERATIONS = False

giphy = Giphy()

@route('/r', method=['POST', 'GET'])
def r():
    res = giphy.random_gif()
    gif_url = res['raw_data']['images']['original']['url']
    return json.dumps({"text": gif_url})

@route('/g', method=['POST'])
def g():
    search = request.forms.get('text')[3:]
    logging.info("Serving %s for user %s" % (search, request.forms.get('user_name'))
    if ITERATIONS:
        iterations = 1
        if search.endswith('.'):
            iterations = search.count('.') + 1
        for x in range(iterations):
            res = giphy.search(search.replace('.', '')).next()
    else:
        res = giphy.search(search.replace('.', '')).next()
    
    gif_url = res['raw_data']['images']['original']['url']
    
    return json.dumps({"text": gif_url})

if __name__ == '__main__':
    run(host="0.0.0.0", port=8080)
