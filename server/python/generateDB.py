 #!/usr/bin/python
 # -*- coding: utf8 -*-

import sqlite3
import csv
import hashlib
import os
import os.path
import functionDataBase

class GenerateDB:
	"""
	Corresponding to actions made at the begining to initialize all that needs to be
	"""

	def __init__(self,listAdmin):
		"""
		Constructor allowing to initialize all tables in database
		"""
		self.db = functionDataBase.FunctionDataBase()


		# opening of all resources files
		
		ACTPATH = "../../ressources/Activite.csv"
		INSTPATH = "../../ressources/Installations.csv"
		EQUIPPATH = "../../ressources/Equipements.csv"
		fileAct = open(ACTPATH, "r")
		fileInst = open(INSTPATH, "r")
		fileEquip = open(EQUIPPATH, "r")


		# Connection to the database
		conn = self.db.connect()
		c = conn.cursor();


		# Creation of Activity, Equipement and Installation table

		self.db.createTableActivity(conn)
		self.db.createTableEquipement(conn)
		self.db.createTableInstallation(conn)


		# Reading of CSV Activity file 
		try:
			# Creation of ''reader'' CSV.
			reader = csv.reader(fileAct)
			# The ''reader'' is iterable, and can be used
			# in a for loop to extract lines one by one
			for i,row in enumerate(reader):
				accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
				without_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
				# the level of the competition (with accents)
				line = row[9]
				j = 0
				while j < len(accent):
					# all accents are replace bu letter without accent
					line = line.replace(accent[j], without_accent[j])
					j += 1
				# interesting data are added to the database
				self.db.addEntryActivity(i,row[2],row[4],row[5],line,row[0],conn)
		finally:
			# Closing of the source file
			fileAct.close()



		# Reading of CSV Equipement file
		try:
			reader = csv.reader(fileEquip)
			for i,row in enumerate(reader):
				# interesting data are added to the database
				self.db.addEntryEquipement(i,row[4],row[1],row[2],row[3],row[5],row[7],row[180],row[181],conn)
		finally:
			# Closing of the source file
			fileEquip.close()

		# Reading of CSV Installation file
		try:
			reader = csv.reader(fileInst)
			for i,row in enumerate(reader):
				# interesting data are added to the database
				self.db.addEntryInstallation(i,row[1],row[7],row[12],row[26],row[17],conn)
		finally:
			# Closing of the source file
			fileEquip.close()
			
		self.db.createTableAdmin(conn)

		if(len(listAdmin) != 0):

			for person in listAdmin:
				self.db.addEntryAdmin(person[1],person[2],conn)

		conn.commit()

		# All actions from SQL are closed
		self.db.close(conn)
