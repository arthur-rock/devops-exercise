import os
from flask import Flask,request
from flask_redis import FlaskRedis

app = Flask(__name__)
app.config['REDIS_URL'] = os.getenv('REDIS_URL') or "redis://localhost:6379/0"
redis_client = FlaskRedis(app)


@app.route("/", methods = ["GET", "POST"])
def hello():
    global redis_client
    if request.method == "GET":
        redis_client.incr('counter',0)
        return ('Hello World!!! # request POSTS: {}'.format(redis_client.get('counter').decode('UTF-8')))
    if request.method == "POST":
        redis_client.incr("counter")
        return "OK! request POSTS+1"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
