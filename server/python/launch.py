# coding: utf-8

from bottle import route, run, template, get, post, request
import bottle
import sqlite3
import os
import sys
import generateDB

sys.path.append("{}/Class_Server".format(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.dirname(os.path.realpath(__file__)))


from functionDataBase import FunctionDataBase 
from accueil import Accueil
from creation import Creation
from admin import Admin
from recherche import Recherche


DATA_PATH = '../../Data Base/DataBase.db'

db = FunctionDataBase()
a = Accueil()
c = Creation()
r = Recherche()
admin = Admin()


@get('/') 
def printHome():
	"""
	Permit to redirect if 
		nobody is in database
		or to authenticate
	"""
	return a.get_accueil(DATA_PATH,db)

@post('/')
def treatAuthCreate():
	"""
	Permit to trate the case of 
		the click on the button allowing the creation of an administrator  
		or to check authentication
	"""
	return a.post_accueil(db)

	
@get('/creation')
def createDataBase():
	"""
	Permit to create all tables in database in this does not exist
	"""
	return c.get_creation(DATA_PATH,db)

	
@get('/admin')
def checkAuth():
	"""
	Permit to know if administrators already exist
	"""
	return admin.get_admin(DATA_PATH,db)	

@post('/admin')
def panelAdmin():
	"""
	Permit to treate the cases of delete, add, update an administrator
	and update the database (regeneration)
	"""
	return admin.post_admin(DATA_PATH, db)


@get('/recherche') 
def printDataResearch():
	"""
	Permit to print 4 fields allowing to the user to research what he wants
	"""
	return r.get_recherche(db)

@post('/recherche')
def treatDataResearch():
	"""
	Permit to treate data according to what the user is looking for
	"""
	return r.post_recherche(db)

@get('/recherche/<id>')
def detailDataResearch(id):
	"""
	Permit to zoom on accurate data in the goal to situate with GMaps the place it is 
	"""
	return r.get_rechercher_id(db,id)


# lauching of the server
run(host='localhost', port=8080)