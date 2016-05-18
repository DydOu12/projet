from bottle import route, run, template, get, post, request
import bottle
import sqlite3
import os
import sys
import generateDB

sys.path.append("{}/Class_Server".format(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.dirname(os.path.realpath(__file__)))


import functionDataBase 
from accueil import Accueil
from creation import Creation
from admin import Admin
from recherche import Recherche


DATA_PATH = '../../Data Base/DataBase.db'

db = functionDataBase.FunctionDataBase()

a = Accueil()
c = Creation()
r = Recherche()
admin = Admin()


@get('/') # ==> @route('/')
def index():
	return a.get_accueil(DATA_PATH,db)


@post('/')
def index():
	return a.post_accueil(db)
	# request.forms.get('types'),request.forms.get('nomCreate'),request.forms.get('passwordCreate')

	
@get('/creation')
def index():
	return c.get_creation(DATA_PATH,db)
	


@get('/admin')
def index():
	return admin.get_admin(DATA_PATH,db)
	

@post('/admin')
def index():
	return admin.post_admin(db)

@get('/recherche') # ==> @route('/recherche')
def index():
	return r.get_recherche(db)

@post('/recherche')
def post():
	return r.post_recherche(db)

@get('/recherche/<id>')
def index(id):
	return r.get_rechercher_id(db,id)

# lauching of the server
run(host='localhost', port=8080)