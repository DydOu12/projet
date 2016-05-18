import os
from bottle import template
import bottle 
import generateDB

bottle.TEMPLATE_PATH.insert(0, "../template/")

class Creation():


	def get_creation(self,DATA_PATH,db):
		# if the database already exists
		if os.path.isfile(DATA_PATH):
			return template('accueil',erreur="La base de donnée est déjà existante",bd="",admin="")
		# if not, if the database does not exist
		else:
			listeAdmin = []
			# all tables for the database are created
			generateDB.GenerateDB(listeAdmin)
			return template('accueil',erreur="La base a bien été créé",bd="",admin="True")
