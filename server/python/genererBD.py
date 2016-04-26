import sqlite3
import csv
import hashlib
import os
import os.path

if os.path.isfile('../../Data Base/DataBase.db'):
	os.remove("../../Data Base/DataBase.db")

def test(listeAdmin):

	nameAct = "../../ressources/Activite.csv"
	fileAct = open(nameAct, "r")

	nameInst = "../../ressources/Installations.csv"
	fileInst = open(nameInst, "r")

	nameEquip = "../../ressources/Equipements.csv"
	fileEquip = open(nameEquip, "r")




	# ACTIVITE
	# Fonction permettant de créer la table Activité avec différents paramètre

	def CreateTableActivite():
		conn.execute('''CREATE TABLE Activite 
		(ID INT PRIMARY KEY,EquipementID INT, ActCode INT,ActLib TEXT,ActNivLib TEXT,ComInsee INT)''')
		#id => EquipementID

	# Fonction permettant d'ajouter des lignes à la table activité

	def AddEntryActivite(ID,EquipementID,ActCode,ActLib,ActNivLib,ComInsee):
		conn.execute('''INSERT INTO Activite (ID,EquipementID,ActCode,ActLib,ActNivLib,ComInsee)
		VALUES (?,?,?,?,?,?)''',(ID,EquipementID,ActCode,ActLib,ActNivLib,ComInsee))




	# EQUIPEMENT
	# Fonction permettant de créer la table Equipement avec différents paramètre

	def CreateTableEquipement():
		conn.execute('''CREATE TABLE Equipement 
		(ID INT PRIMARY KEY,EquipementID INT, ComLib TEXT,InsNumeroInstall TEXT,InsNom TEXT,EquNom TEXT,EquipementTypeLib TEXT,EquGPSX REAL,EquGPSY REAL)''')
		#id => EquipementID

	# Fonction permettant d'ajouter des lignes à la table activité

	def AddEntryEquipement(ID,EquipementID,ComLib,InsNumeroInstall,InsNom,EquNom,EquipementTypeLib,EquGPSX,EquGPSY):
		conn.execute('''INSERT INTO Equipement (ID,EquipementID,ComLib,InsNumeroInstall,InsNom,EquNom,EquipementTypeLib,EquGPSX,EquGPSY)
		VALUES (?,?,?,?,?,?,?,?,?)''',(ID,EquipementID,ComLib,InsNumeroInstall,InsNom,EquNom,EquipementTypeLib,EquGPSX,EquGPSY))








	# INSTALLATION
	# Fonction permettant de créer la table Equipement avec différents paramètre

	def CreateTableInstallation():
		conn.execute('''CREATE TABLE Installation 
		(ID INT PRIMARY KEY,InsNumeroInstall INT, NomVoie TEXT,AmenagementAccesHand BOOLEAN,NbrEquip INT,PlaceParking INT)''')
		#id => EquipementID

	# Fonction permettant d'ajouter des lignes à la table activité

	def AddEntryInstallation(ID,InsNumeroInstall,NomVoie,AmenagementAccesHand,NbrEquip,PlaceParking):
		conn.execute('''INSERT INTO Installation (ID,InsNumeroInstall,NomVoie,AmenagementAccesHand,NbrEquip,PlaceParking)
		VALUES (?,?,?,?,?,?)''',(ID,InsNumeroInstall,NomVoie,AmenagementAccesHand,NbrEquip,PlaceParking))






	# ADMINISTRATION

	def CreateTableAdmin():
		conn.execute('''CREATE TABLE Admin 
		(ID INTEGER PRIMARY KEY AUTOINCREMENT,Nom TEXT, Password TEXT)''')
		#id => EquipementID
		
	def AddEntryAdmin(Nom,Password):
		conn.execute('''INSERT INTO Admin (Nom,Password)
		VALUES (?,?)''',(Nom,Password))



	# Entre Equipement et Activité EquipementID
	# Entre Equipement et installation NumeroInstallation


	# Enumeration i 1,2,3,4,5,6
		# for i, x in enumerate(l):
		#     print(y)


	# Création du fichier 

	conn = sqlite3.connect('../../Data Base/DataBase.db')
	c = conn.cursor()

	# Création de la table Activité, Equipement, installation

	CreateTableActivite()
	CreateTableEquipement()
	CreateTableInstallation()

	# Lecture du fichier CVS Activite

	try:
		#
		# Création du ''lecteur'' CSV.
		#
		reader = csv.reader(fileAct)
		#
		# Le ''lecteur'' est itérable, et peut être utilisé
		# dans une boucle ''for'' pour extraire les
		# lignes une par une.
		#
		for i,row in enumerate(reader):
			accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
			sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
			ligne = row[9]
			j = 0
			while j < len(accent):
				ligne = ligne.replace(accent[j], sans_accent[j])
				j += 1
			AddEntryActivite(i,row[2],row[4],row[5],ligne,row[0])
		
	finally:
		#
		# Fermeture du fichier source
		#
		fileAct.close()


	# Lecture du fichier CVS Equipement

	try:
		reader = csv.reader(fileEquip)
		for i,row in enumerate(reader):
			AddEntryEquipement(i,row[4],row[1],row[2],row[3],row[5],row[7],row[180],row[181])
			# print(row)
	finally:
		fileEquip.close()


	# Lecture du fichier CSV Installation

	try:
		reader = csv.reader(fileInst)
		for i,row in enumerate(reader):
			AddEntryInstallation(i,row[1],row[7],row[12],row[26],row[17])
			# print(row)
	finally:
		fileEquip.close()
		
	if(len(listeAdmin) != 0):
		
		CreateTableAdmin()

		for personne in listeAdmin:
					
			#Cryptage du mot de passe de l'admin grâce au SHA-1
			
			AddEntryAdmin(personne[1],personne[2])
			

		# On envoie les données dans le fichier .db
	else:
		CreateTableAdmin()

	conn.commit()

	#test = conn.execute('SELECT * FROM Activite')

	#for i in test:
	#     print("\n")
	#     phrase = ""
	#     for j in i:
	#         phrase = phrase + str(j) + " / "
	#     print(phrase)
	#phrase = ""
	#for i in test:
	#    phrase = phrase + str(i[0]) + "/"
	#print(phrase)



	# On ferme toutes les actions relative aux SQL

	conn.close()






