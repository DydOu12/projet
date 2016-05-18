 #!/usr/bin/python
 # -*- coding: utf8 -*-

import sqlite3
import csv
import hashlib
import os
import os.path
import functionDataBase

class GenerateDB:

	def __init__(self,listeAdmin):
		"""
		Ceci est un test
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

		# conn = sqlite3.connect('../../Data Base/DataBase.db')
		# c = conn.cursor()
		conn = self.db.connect()

		c = conn.cursor();


		# Creation of Activity, Equipement and Installation table

		self.db.createTableActivite(conn)
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
				sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
				# the level of the competition (with accents)
				ligne = row[9]
				j = 0
				while j < len(accent):
					# all accents are replace bu letter without accent
					ligne = ligne.replace(accent[j], sans_accent[j])
					j += 1
				# interesting data are added to the database
				self.db.addEntryActivite(i,row[2],row[4],row[5],ligne,row[0],conn)
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

		if(len(listeAdmin) != 0):

			for personne in listeAdmin:
				self.db.addEntryAdmin(personne[1],personne[2],conn)

		conn.commit()

		# All actions from SQL are closed
		self.db.close(conn)
