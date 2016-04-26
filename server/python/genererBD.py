import sqlite3
import csv
import hashlib
import os
import os.path

"""

"""
def test(listeAdmin):

	# opening of all resources files
	nameAct = "../../ressources/Activite.csv"
	fileAct = open(nameAct, "r")

	nameInst = "../../ressources/Installations.csv"
	fileInst = open(nameInst, "r")

	nameEquip = "../../ressources/Equipements.csv"
	fileEquip = open(nameEquip, "r")



	# ACTIVITY
	"""
	# Fonction permettant de créer la table Activité avec différents paramètre
	"""
	def CreateTableActivite():
		conn.execute('''CREATE TABLE Activite 
		(ID INT PRIMARY KEY,EquipementID INT, ActCode INT,ActLib TEXT,ActNivLib TEXT,ComInsee INT)''')

	"""
	# Fonction permettant d'ajouter des lignes à la table activité
	"""
	def AddEntryActivite(ID,EquipementID,ActCode,ActLib,ActNivLib,ComInsee):
		conn.execute('''INSERT INTO Activite (ID,EquipementID,ActCode,ActLib,ActNivLib,ComInsee)
		VALUES (?,?,?,?,?,?)''',(ID,EquipementID,ActCode,ActLib,ActNivLib,ComInsee))



	# EQUIPEMENT
	"""
	# Fonction permettant de créer la table Equipement avec différents paramètre
	"""
	def CreateTableEquipement():
		conn.execute('''CREATE TABLE Equipement 
		(ID INT PRIMARY KEY,EquipementID INT, ComLib TEXT,InsNumeroInstall TEXT,InsNom TEXT,EquNom TEXT,EquipementTypeLib TEXT,EquGPSX REAL,EquGPSY REAL)''')

	"""
	# Fonction permettant d'ajouter des lignes à la table activité
	"""
	def AddEntryEquipement(ID,EquipementID,ComLib,InsNumeroInstall,InsNom,EquNom,EquipementTypeLib,EquGPSX,EquGPSY):
		conn.execute('''INSERT INTO Equipement (ID,EquipementID,ComLib,InsNumeroInstall,InsNom,EquNom,EquipementTypeLib,EquGPSX,EquGPSY)
		VALUES (?,?,?,?,?,?,?,?,?)''',(ID,EquipementID,ComLib,InsNumeroInstall,InsNom,EquNom,EquipementTypeLib,EquGPSX,EquGPSY))



	# INSTALLATION
	"""
	# Fonction permettant de créer la table Equipement avec différents paramètre
	"""
	def CreateTableInstallation():
		conn.execute('''CREATE TABLE Installation 
		(ID INT PRIMARY KEY,InsNumeroInstall INT, NomVoie TEXT,AmenagementAccesHand BOOLEAN,NbrEquip INT,PlaceParking INT)''')

	"""
	# Fonction permettant d'ajouter des lignes à la table activité
	"""
	def AddEntryInstallation(ID,InsNumeroInstall,NomVoie,AmenagementAccesHand,NbrEquip,PlaceParking):
		conn.execute('''INSERT INTO Installation (ID,InsNumeroInstall,NomVoie,AmenagementAccesHand,NbrEquip,PlaceParking)
		VALUES (?,?,?,?,?,?)''',(ID,InsNumeroInstall,NomVoie,AmenagementAccesHand,NbrEquip,PlaceParking))



	# ADMINISTRATION
	"""

	"""
	def CreateTableAdmin():
		conn.execute('''CREATE TABLE Admin 
		(ID INTEGER PRIMARY KEY AUTOINCREMENT,Nom TEXT, Password TEXT)''')
	
	"""
	"""
	def AddEntryAdmin(Nom,Password):
		conn.execute('''INSERT INTO Admin (Nom,Password)
		VALUES (?,?)''',(Nom,Password))

	# Connection to the database

	conn = sqlite3.connect('../../Data Base/DataBase.db')
	c = conn.cursor()

	# Creation of Activity, Equipement and Installation table

	CreateTableActivite()
	CreateTableEquipement()
	CreateTableInstallation()

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
			AddEntryActivite(i,row[2],row[4],row[5],ligne,row[0])
		
	finally:
		# Closing of the source file
		fileAct.close()


	# Reading of CSV Equipement file
	try:
		reader = csv.reader(fileEquip)
		for i,row in enumerate(reader):
			# interesting data are added to the database
			AddEntryEquipement(i,row[4],row[1],row[2],row[3],row[5],row[7],row[180],row[181])
	finally:
		# Closing of the source file
		fileEquip.close()


	# Reading of CSV Installation file
	try:
		reader = csv.reader(fileInst)
		for i,row in enumerate(reader):
			# interesting data are added to the database
			AddEntryInstallation(i,row[1],row[7],row[12],row[26],row[17])
	finally:
		# Closing of the source file
		fileEquip.close()
		
	CreateTableAdmin()

	conn.commit()

	# All actions from SQL are closed
	conn.close()



