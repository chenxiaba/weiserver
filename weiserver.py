# APP   : Messnote Server v0.1 
# author: chenxiaba
# date  : 2015.09.07

from flask import Flask , request
from redis import Redis 

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def index():
    redis.incr('hits')
    return 'Hello World! I have  been seen %s times' % redis.get('hits')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Login Succuss!"
    else:
        return "Please login first."

@app.route('/note/<int:note_id>')
def note(note_id):
    return "Notes page: %d" % note_id

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)
    
