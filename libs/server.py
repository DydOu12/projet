from bottle import route, template, run

@route('/hello/<name>')
def index(name):
    return template('template', name=name)

run(host='localhost', port=8080)