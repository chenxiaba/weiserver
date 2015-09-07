# APP   : Messnote Server v0.1 
# author: chenxiaba
# date  : 2015.09.07

from flask import Flask 
from redis import Redis 

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def main():
    redis.incr('hits')
    return 'Hello World! I have  been seen %s times' % redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)
    
