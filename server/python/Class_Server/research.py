# coding: utf-8

import os
from bottle import template,request
import bottle 
import generateDB

bottle.TEMPLATE_PATH.insert(0, "../template/")

class Research():
	"""
	Corresponding to actions made when the users research informations
	"""

	def get_research(self,db):
		"""
		Permit to print 4 fields allowing to the user to research what he wants
		"""

		# connexion to the database
		conn = db.connect()
	
		list = []

		# ActLib attribute is selected from Activity table
		activities = db.selectActivity('ActLib',conn)

		# all activities are traversed 
		for i in activities:
			# check if the current element is in the list
			present = i[0] in list 
			# if the current element isn't present in the list
			if(present == False):
				# it's add to the list
				list.append(i[0])
		
		# the list is sorted
		list.sort()
		# the head of the column of the CSV is removed
		list.remove('ActLib')

		training = []

		# ActLib attribute is selected from Activity table
		levAct = db.selectActivity('ActNivLib',conn)

		# all levels are traversed 
		for j in levAct:
			# check if the current element is in the list
			present = j[0] in training
			# if the current element isn't present in the list
			if(present == False):
				# it's add to the list
				training.append(j[0])

		# the head of the column of the CSV is removed
		training.remove('ActNivLib')
		# the list is sorted
		training.sort()

		return template('form',list=list, levAct=training)


	def post_research(self,db):
		"""
		Permit to treate data according to what the user is looking for
		"""

		# connexion to the database
		conn = db.connect()
		
		# each information necessary are recovered
		activity = request.forms.get('activity')
		postalCode = request.forms.get('postalCode')
		level = request.forms.get('level')
		handicap = request.forms.get('handicap')

		information = []

		# informations are selected according on what the user choose
		listActivity = db.listeActivity(activity,postalCode,level,handicap,conn)
		
		# the cursor sqlite3 object is traversed containing all informations of the research
		for i in listActivity:
			# all necessary information will be add in this array
			valuesList = []
			# all informations concerning one response of the request made by the user
			for j in i:
				# an array on these informations is created 
				valuesList.append(j)
			
			# informations linked to Equipement table are recovered (it's a cursor sqlite3 object)
			listEquipement = db.selectAllEquipement(valuesList[1],conn)

			# all informations concerning one request linked to Equipement
			for k in listEquipement:
				# in this request
				for l in k:
					# each element are add in the list
					valuesList.append(l)

			# if the user don't specify anything about handicap
			if(handicap != ""):
				listInstallation = db.selectAllInstTwoArg(valuesList[9],handicap,conn)
			# if not
			else:
				listInstallation = db.selectAllInstallation(valuesList[9],conn)

			# all informations concerning one request linked to Installation
			for m in listInstallation:
				# in this request
				for n in m:
					# each element are add in the list
					valuesList.append(n)

			# if the list length is out of 20, informations are added to the list because 
			# all informations must be taken into account
			if(len(valuesList) > 20):
				information.append(valuesList)
				
		return template('result',information = information)


	def get_research_id(self,db,id):
		"""
		Permit to zoom on accurate data in the goal to situate with GMaps the place it is 
		"""
		
		# connexion to the database
		conn = db.connect()

		information =[]

		# everything is selected with one specific ID
		listActivity = db.selectAllActivity(int(id),conn)

		# the cursor sqlite3 object is traversed containing all informations of the research
		for i in listActivity:
			# all necessary information will be add in this array
			valuesList = []
			# all informations concerning one response of the request made by the user
			for j in i:
				# an array on these informations is created 
				information.append(j)
		
			# informations linked to Equipement table are recovered (it's a cursor sqlite3 object)
			listEquipement = db.selectAllEquipement(information[1],conn)

			# all informations concerning one request linked to Equipement
			for k in listEquipement:
				# in this request
				for l in k:
					# each element are add in the list
					information.append(l)

			# informations linked to Installation table are recovered (it's a cursor sqlite3 object)
			listInstallation = db.selectAllInstallation(information[9],conn)

			# all informations concerning one request linked to Installation
			for m in listInstallation:
				# in this request
				for n in m:
					# each element are add in the list
					information.append(n)

		return template('map',information = information)