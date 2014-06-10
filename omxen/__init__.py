import json
from gevent import monkey; monkey.patch_all()
from gevent.queue import Queue

from collections import defaultdict
from bottle import route, run, request


@route('/')
def index():
    yield 'OMXEN SMS GATEWAY'


_SMS = defaultdict(Queue)


@route('/send', method='GET')
def send():
    # XXX not really checking those...
    api_key = request.query.get('api_key')
    api_secret = request.query.get('api_secret')

    from_ = request.query['from']
    to = request.query['to']
    text = request.query['text']
    _SMS[to].put_nowait((from_, text))
    yield 'whatever'


@route('/receive', method='GET')
def receive():
    to = request.query['to']
    res = []

    while not _SMS[to].empty():
        from_, text = _SMS[to].get()
        res.append({'from': from_, 'text': text})

    yield json.dumps(res)


def main():
    run(host='0.0.0.0', port=8080, server='gevent')
