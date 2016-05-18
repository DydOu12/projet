import sqlite3

class FunctionDataBase: 
	"""

	"""

	def __init__(self):
		self.DATA_PATH = '../../Data Base/DataBase.db' 

	def connect(self):
		return sqlite3.connect(self.DATA_PATH)

	def close(self,conn):
		return conn.close()






	# ACTIVITY
	def createTableActivite(self,conn):
		"""
		Fonction permettant de creer la table Activite avec differents parametres
		"""
		conn.execute('''CREATE TABLE Activite 
		(ID INT PRIMARY KEY,EquipementID INT, ActCode INT,ActLib TEXT,ActNivLib TEXT,ComInsee INT)''')

	"""
	Fonction permettant d'ajouter des lignes a la table Activite
	"""
	def addEntryActivite(self,ID,EquipementID,ActCode,ActLib,ActNivLib,ComInsee,conn):
		conn.execute('''INSERT INTO Activite (ID,EquipementID,ActCode,ActLib,ActNivLib,ComInsee) VALUES (?,?,?,?,?,?)''',(ID,EquipementID,ActCode,ActLib,ActNivLib,ComInsee))

	# EQUIPEMENT
	"""
	Fonction permettant de creer la table Equipement avec differents parametres
	"""
	def createTableEquipement(self,conn):
		conn.execute('''CREATE TABLE Equipement 
		(ID INT PRIMARY KEY,EquipementID INT, ComLib TEXT,InsNumeroInstall TEXT,InsNom TEXT,EquNom TEXT,EquipementTypeLib TEXT,EquGPSX REAL,EquGPSY REAL)''')

	"""
	Fonction permettant d'ajouter des lignes a la table Activite
	"""
	def addEntryEquipement(self,ID,EquipementID,ComLib,InsNumeroInstall,InsNom,EquNom,EquipementTypeLib,EquGPSX,EquGPSY,conn):
		conn.execute('''INSERT INTO Equipement (ID,EquipementID,ComLib,InsNumeroInstall,InsNom,EquNom,EquipementTypeLib,EquGPSX,EquGPSY)
		VALUES (?,?,?,?,?,?,?,?,?)''',(ID,EquipementID,ComLib,InsNumeroInstall,InsNom,EquNom,EquipementTypeLib,EquGPSX,EquGPSY))


	# INSTALLATION
	"""
	Fonction permettant de creer la table Equipement avec differents parametres
	"""
	def createTableInstallation(self,conn):
		conn.execute('''CREATE TABLE Installation 
		(ID INT PRIMARY KEY,InsNumeroInstall INT, NomVoie TEXT,AmenagementAccesHand BOOLEAN,NbrEquip INT,PlaceParking INT)''')

	"""
	Fonction permettant d'ajouter des lignes a la table Activite
	"""
	def addEntryInstallation(self,ID,InsNumeroInstall,NomVoie,AmenagementAccesHand,NbrEquip,PlaceParking,conn):
		conn.execute('''INSERT INTO Installation (ID,InsNumeroInstall,NomVoie,AmenagementAccesHand,NbrEquip,PlaceParking)
		VALUES (?,?,?,?,?,?)''',(ID,InsNumeroInstall,NomVoie,AmenagementAccesHand,NbrEquip,PlaceParking))


	# ADMINISTRATION
	"""
	"""
	def createTableAdmin(self,conn):
		conn.execute('''CREATE TABLE Admin 
		(ID INTEGER PRIMARY KEY AUTOINCREMENT,Nom TEXT, Password TEXT)''')

	
	"""
	"""
	def addEntryAdmin(self,Nom,Password,conn):
		conn.execute('''INSERT INTO Admin (Nom,Password)
		VALUES (?,?)''',(Nom,Password))




	def selectAdmin(self,conn):
		return conn.execute('SELECT * FROM Admin')

	def insertAdmin(self,nom,password,conn):
		conn.execute('''INSERT INTO Admin (Nom,Password) VALUES (?,?)''',(nom,password))
		conn.commit()

	def selectPassAdmin(self,nom,conn):
		return conn.execute('SELECT Password FROM Admin WHERE NOM=:Nom',{"Nom": nom})

	def selectIdAdmin(self,nom,conn):
		return conn.execute('SELECT ID FROM Admin WHERE NOM=:Nom',{"Nom": nom})

	def selectIdWithpassAdmin(self,nom,password,conn):
		return conn.execute('SELECT ID FROM Admin WHERE NOM=:Nom AND Password=:Password',{"Nom": nom,"Password":password})

	def updatePassAdmin(self,ids,password,conn):
		conn.execute('UPDATE Admin SET Password=:Password WHERE ID=:ID',{"Password":password,"ID":ids})		
		conn.commit()

	def selectNomAdmin(self,idSelect,conn):
		return conn.execute('SELECT Nom FROM Admin WHERE ID=:ID',{"ID":idSelect})

	def delAdmin(self,idSelect,conn):
		conn.execute('DELETE FROM Admin WHERE ID=:ID',{"ID":idSelect})
		conn.commit()


	def selectActivite(self,act,conn):
		return conn.execute('SELECT '+act+' FROM Activite')

	def listeActivite(self,activite,codePostal,niveau,handicap,conn):
		if(activite == "" and codePostal != "" and niveau != ""):
			return conn.execute("SELECT * FROM Activite WHERE ComInsee=:ComInsee AND ActNivLib=:ActNivLib", {"ComInsee":int(codePostal),"ActNivLib":niveau})
		elif(codePostal == "" and activite != "" and niveau != ""):
			return conn.execute("SELECT * FROM Activite WHERE ActLib =:ActLib AND ActNivLib=:ActNivLib", {"ActLib":activite,"ActNivLib":niveau})
		elif(niveau == "" and activite != "" and codePostal != ""):
			return conn.execute("SELECT * FROM Activite WHERE ActLib =:ActLib AND ComInsee=:ComInsee", {"ActLib":activite,"ComInsee":int(codePostal)})
		elif(activite == "" and codePostal == "" and niveau != ""):
			return conn.execute("SELECT * FROM Activite WHERE ActNivLib=:ActNivLib", {"ActNivLib":niveau})
		elif(activite == "" and niveau == "" and codePostal != ""):
			return conn.execute("SELECT * FROM Activite WHERE ComInsee=:ComInsee", {"ComInsee":int(codePostal)})
		elif(codePostal == "" and niveau == "" and activite != ""):
			return conn.execute("SELECT * FROM Activite WHERE ActLib =:ActLib", {"ActLib":activite})
		elif(activite == "" and codePostal == "" and niveau == ""):
			return conn.execute("SELECT * FROM Activite")
		else:
			return conn.execute("SELECT * FROM Activite WHERE ActLib =:ActLib AND ComInsee=:ComInsee AND ActNivLib=:ActNivLib", {"ActLib":activite,"ComInsee":int(codePostal),"ActNivLib":niveau})

	def selectEquipement(self,idEquipement,conn):
		return conn.execute("SELECT * FROM Equipement WHERE EquipementID=:EquipementID", {"EquipementID": idEquipement})

	def selectAllInstTwoArg(self,InsNumeroInstall,AmenagementAccesHand,conn):
		return conn.execute("SELECT * FROM Installation WHERE InsNumeroInstall=:InsNumeroInstall AND AmenagementAccesHand=:AmenagementAccesHand", {"InsNumeroInstall": InsNumeroInstall,"AmenagementAccesHand":AmenagementAccesHand})

	def selectAllInstOneArg(self,InsNumeroInstall,conn):
		return conn.execute("SELECT * FROM Installation WHERE InsNumeroInstall=:InsNumeroInstall", {"InsNumeroInstall": InsNumeroInstall})

	def selectAllActivite(self,id,conn):
		return conn.execute("SELECT * FROM Activite WHERE ID=:ID", {"ID":int(id)})

	def selectAllEquipement(self,EquipementID,conn):
		return conn.execute("SELECT * FROM Equipement WHERE EquipementID=:EquipementID", {"EquipementID": EquipementID})

	def selectAllInstallation(self,InsNumeroInstall,conn):
		return conn.execute("SELECT * FROM Installation WHERE InsNumeroInstall=:InsNumeroInstall ", {"InsNumeroInstall":InsNumeroInstall})



	