from flask import Flask
from flask import request
import json
import time

app = Flask(__name__)

SUPPORTED_PROTOCOLS = ['stratum2', 'stratum']
MINING_HOST = 'eu.slushpool.com'
MINING_PORT = 3333
EXPIRATION_SECONDS = 10


class InitMessage(object):
    def __init__(self, api_key, accepted_protocols, password=None):
        self.api_key = api_key
        self.accepted_protocols = accepted_protocols
        self.password = password


class ResponseMessage(object):
    def __init__(self, protocol, host, port):
        self.protocol = protocol
        self.host = host
        self.port = port
        self.server_time = time.time()
        self.expiration = EXPIRATION_SECONDS


@app.route('/', methods=['POST'])
def index():
    # TODO: check content type and raise corresponding HTTP error if necessary
    try:
        init_msg = InitMessage(**request.json)
    except Exception as e:
        return ('Initiation Message Error: %s' % e, 403)

    for p in SUPPORTED_PROTOCOLS:
        if p in init_msg.accepted_protocols:
            # Notify pool infrastructure (fictional pseudo code)
            # pool.submit_mining_init_request(request.remote_addr, MINING_HOST)
            response = ResponseMessage(p, MINING_HOST, MINING_PORT)
            break
    else:
        return ('No supported protocols found, choose one of: %s' % SUPPORTED_PROTOCOLS,
                403)


    return (json.dumps(response.__dict__), 200)


if __name__ == '__main__':
    app.run(debug=True)
