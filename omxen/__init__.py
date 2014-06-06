from gevent import monkey; monkey.patch_all()
from bottle import route, run


@route('/')
def index():
    yield 'OMXEN SMS GATEWAY'


def main():
    run(host='0.0.0.0', port=8080, server='gevent')
