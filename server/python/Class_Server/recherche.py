# coding: utf-8

import os
from bottle import template,request
import bottle 
import generateDB

bottle.TEMPLATE_PATH.insert(0, "../template/")

class Recherche():
	"""
	Corresponding to actions made when the users research informations
	"""

	def get_recherche(self,db):
		"""
		Permit to print 4 fields allowing to the user to research what he wants
		"""

		# connexion to the database
		conn = db.connect()
	
		liste = []

		# ActLib attribute is selected from Activite table
		activites = db.selectActivite('ActLib',conn)

		# all activities are traversed 
		for i in activites:
			# check if the current element is in the list
			present = i[0] in liste 
			# if the current element isn't present in the list
			if(present == False):
				# it's add to the list
				liste.append(i[0])
		
		# the list is sorted
		liste.sort()
		# the head of the column of the CSV is removed
		liste.remove('ActLib')

		entrainement = []

		# ActLib attribute is selected from Activite table
		nivact = db.selectActivite('ActNivLib',conn)

		# all levels are traversed 
		for j in nivact:
			# check if the current element is in the list
			present = j[0] in entrainement
			# if the current element isn't present in the list
			if(present == False):
				# it's add to the list
				entrainement.append(j[0])

		# the head of the column of the CSV is removed
		entrainement.remove('ActNivLib')
		# the list is sorted
		entrainement.sort()

		return template('formulaire',liste=liste, nivact=entrainement)


	def post_recherche(self,db):
		"""
		Permit to treate data according to what the user is looking for
		"""

		# connexion to the database
		conn = db.connect()
		
		# each information necessary are recovered
		activite = request.forms.get('activite')
		codePostal = request.forms.get('codePostal')
		niveau = request.forms.get('niveau')
		handicap = request.forms.get('handicap')

		information = []

		# informations are selected according on what the user choose
		listeActivite = db.listeActivite(activite,codePostal,niveau,handicap,conn)
		
		# the cursor sqlite3 object is traversed containing all informations of the research
		for i in listeActivite:
			# all necessary information will be add in this array
			valeurListe = []
			# all informations concerning one response of the request made by the user
			for j in i:
				# an array on these informations is created 
				valeurListe.append(j)
			
			# informations linked to Equipement table are recovered (it's a cursor sqlite3 object)
			listeEquipement = db.selectEquipement(valeurListe[1],conn)

			# all informations concerning one request linked to Equipement
			for k in listeEquipement:
				# in this request
				for l in k:
					# each element are add in the list
					valeurListe.append(l)

			# if the user don't specify anything about handicap
			if(handicap != ""):
				listeInstallation = db.selectAllInstTwoArg(valeurListe[9],handicap,conn)
			# if not
			else:
				listeInstallation = db.selectAllInstOneArg(valeurListe[9],conn)

			# all informations concerning one request linked to Installation
			for m in listeInstallation:
				# in this request
				for n in m:
					# each element are add in the list
					valeurListe.append(n)

			# if the list length is out of 20, informations are added to the list because 
			# all informations must be taken into account
			if(len(valeurListe) > 20):
				information.append(valeurListe)
				
		return template('resultat',information = information)


	def get_rechercher_id(self,db,id):
		"""
		Permit to zoom on accurate data in the goal to situate with GMaps the place it is 
		"""
		
		# connexion to the database
		conn = db.connect()

		information =[]

		# everything is selected with one specific ID
		listeActivite = db.selectAllActivite(int(id),conn)

		# the cursor sqlite3 object is traversed containing all informations of the research
		for i in listeActivite:
			# all necessary information will be add in this array
			valeurListe = []
			# all informations concerning one response of the request made by the user
			for j in i:
				# an array on these informations is created 
				information.append(j)
		
			# informations linked to Equipement table are recovered (it's a cursor sqlite3 object)
			listeEquipement = db.selectAllEquipement(information[1],conn)

			# all informations concerning one request linked to Equipement
			for k in listeEquipement:
				# in this request
				for l in k:
					# each element are add in the list
					information.append(l)

			# informations linked to Installation table are recovered (it's a cursor sqlite3 object)
			listeInstallation = db.selectAllInstallation(information[9],conn)

			# all informations concerning one request linked to Installation
			for m in listeInstallation:
				# in this request
				for n in m:
					# each element are add in the list
					information.append(n)

		return template('carte',information = information)