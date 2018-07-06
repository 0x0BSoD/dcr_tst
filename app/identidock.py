from flask import Flask

app = Flask(__name__)
default_name = 'Jon Doe'

@app.route('/')
def index():
    name = default_name

    header = '<html><head><title>Idemtidock</title></head><body>'
    body = '''<form metho="POST">
              Hello <input type="text" name="name" value="{}">
              <input type="submit" value="submit">
              </form>
              <p>You look like a:
              <img src="/monster/monster.png"/>
              '''.format(name)
    footer = '</body></html>'

    return header + body + footer


@app.route('/ping')
def pingpong():
    return "pong"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')