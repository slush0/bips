# Installation

```
$ virtualenv mip-server-env --no-site-packages
$ . mip-server-env/bin/activate
(mip-server-env)$ pip install flask
```

# Simple Test

Run the server sample code:

```
(mip-server-env)$ python mip-server.py

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 599-108-277
```


## Generate Valid MIP Request

- request:
``` 
curl -H "Content-Type: application/json" -X POST -d '{"api_key":"DEADBEEF", "accepted_protocols":["stratum","gbt"], }' http://localhost:5000/
```

- response:
```
{"server_time": 1472224225.889713, "host": "eu.slushpool.com", "protocol": "stratum", "port": 3333, "expiration": 10}
```
