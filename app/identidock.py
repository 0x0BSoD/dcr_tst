from flask import Flask, Response, request, render_template
from requests import get
import hashlib
import redis

app = Flask(__name__)
cache = redis.StrictRedis(host='redis', port=6379, db=0)
salt = "that=uniC-Secret=!"
default_name = 'Jon Doe'


@app.route('/', methods=["GET", "POST"])
def index():

    name = default_name

    if request.method == "POST":
        name = request.form["name"]
        
    salted_name = salt + name
    name_hash = hashlib.sha256(salted_name.encode()).hexdigest()

    return render_template('index.html', name=name, hash=name_hash)


@app.route('/monster/<name>')
def get_identicon(name):

    image = cache.get(name)
    if not image:
        print("Not in cache", flush=True)
        r = get('http://dnmonster:8080/monster/' + name + '?size=80')
        image = r.content
        cache.set(name, image)

    return Response(image, mimetype='image/png')


@app.route('/ping')
def pingpong():
    return "pong"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
