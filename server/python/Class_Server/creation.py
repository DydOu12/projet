# coding: utf-8

import os
from bottle import template
import bottle 
import generateDB

bottle.TEMPLATE_PATH.insert(0, "../template/")

class Creation():
	"""
	Corresponding to the creation of the database
	"""


	def get_creation(self,DATA_PATH,db):
		"""
		Permit to create all tables in database in this does not exist
		"""
		
		# if the database already exists
		if os.path.isfile(DATA_PATH):
			return template('accueil',erreur="La base de donnée est déjà existante",bd="",admin="")
		# if not, if the database does not exist
		else:
			listeAdmin = []
			# all tables for the database are created
			generateDB.GenerateDB(listeAdmin)
			return template('accueil',erreur="La base a bien été créé",bd="",admin="True")
